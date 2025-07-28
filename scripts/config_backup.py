import yaml
from netmiko import ConnectHandler

# Load devices
with open('../data/devices.yml') as file:
    devices = yaml.safe_load(file)['devices']

for device in devices:
    try:
        print(f"\n🔌 Connecting to {device['ip']} to backup config...")
        ssh = ConnectHandler(
            device_type=device['device_type'],
            ip=device['ip'],
            username=device['username'],
            password=device['password']
        )

        config = ssh.send_command("show running-config")
        file_path = f"../backups/{device['name']}_config.txt"

        with open(file_path, "w") as f:
            f.write(config)

        print(f"✅ Config saved: {file_path}")

    except Exception as e:
        print(f"❌ Failed to backup {device['ip']}: {e}")
