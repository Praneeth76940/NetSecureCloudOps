import yaml
import pynetbox
from netmiko import ConnectHandler

NETBOX_URL = "http://192.168.206.139:8000"
NETBOX_TOKEN = "bfcfee365ff4f6f62201326e6c1a3e76e7c06ea3"
nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)

with open('../data/devices.yml') as file:
    devices = yaml.safe_load(file)['devices']

for device in devices:
    try:
        print(f"\n🔌 Connecting to {device['ip']}...")
        ssh = ConnectHandler(
            device_type=device["device_type"],
            ip=device["ip"],
            username=device["username"],
            password=device["password"]
        )

        hostname_line = ssh.send_command("show run | include hostname")
        hostname = hostname_line.split()[1]

        output = ssh.send_command("show ip interface brief")
        lines = output.splitlines()[1:]  # skip header

        # Get device ID from NetBox
        nb_device = nb.dcim.devices.get(name=hostname)
        if not nb_device:
            print(f"❌ Device {hostname} not found in NetBox.")
            continue

        for line in lines:
            parts = line.split()
            if len(parts) < 6:
                continue  # Skip invalid lines

            iface_name = parts[0]
            ip_addr = parts[1] if parts[1] != 'unassigned' else None

            # Push interface
            intf = nb.dcim.interfaces.create({
                "device": nb_device.id,
                "name": iface_name,
                "type": "1000base-t",  # Default type
                "enabled": True
            })

            print(f"  ✅ Interface {iface_name} added to {hostname}")

            # Add IP address (if available)
            if ip_addr:
                nb.ipam.ip_addresses.create({
                    "address": f"{ip_addr}/24",
                    "assigned_object_type": "dcim.interface",
                    "assigned_object_id": intf.id,
                    "status": "active"
                })
                print(f"    🌐 IP {ip_addr} assigned to {iface_name}")

    except Exception as e:
        print(f"❌ Error for {device['ip']}: {e}")
