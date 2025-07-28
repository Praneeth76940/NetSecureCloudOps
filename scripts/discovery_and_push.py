import yaml
import pynetbox
from netmiko import ConnectHandler

# Load devices from YAML
with open('../data/devices.yml') as file:
    devices = yaml.safe_load(file)['devices']

# Connect to NetBox
NETBOX_URL = "http://192.168.206.139:8000"
NETBOX_TOKEN = "bfcfee365ff4f6f62201326e6c1a3e76e7c06ea3"
nb = pynetbox.api(NETBOX_URL, token=NETBOX_TOKEN)

# Push each device
for device in devices:
    try:
        print(f"\n🔌 Connecting to {device['ip']}...")
        ssh = ConnectHandler(
            device_type=device['device_type'],
            ip=device['ip'],
            username=device['username'],
            password=device['password']
        )

        hostname = ssh.send_command("show run | include hostname").split()[1]
        interfaces = ssh.send_command("show ip interface brief")

        print(f"✅ {hostname} discovered. Interfaces:\n{interfaces}")

        # ✅ Check if device already exists
        existing_device = nb.dcim.devices.get(name=hostname)
        if existing_device:
            print(f"🔁 Device '{hostname}' already exists in NetBox. Skipping creation.")
        else:
            result = nb.dcim.devices.create({
                "name": hostname,
                "device_type": 3,  # Your actual Device Type ID
                "role": 2,         # Your actual Device Role ID
                "site": 2,         # Your actual Site ID
                "status": "active"
            })
            print(f"📦 Device '{hostname}' pushed to NetBox.\nResult: {result}")

    except Exception as e:
        print(f"❌ Failed for {device['ip']}: {e}")

