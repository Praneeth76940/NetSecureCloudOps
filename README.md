# NetSecureCloudOps – Automated Network Discovery & NetBox Integration

## 🔧 Project Overview

**NetSecureCloudOps** is a real-time Python automation framework designed to:
- Automatically discover network devices using SSH
- Extract device information (hostname, interfaces, IPs, and configuration)
- Push the discovered data into **NetBox** (an open-source Source of Truth)
- Perform config backups for auditing and disaster recovery

This solution is built using:
- **Python + Netmiko** for device communication
- **NetBox API (via pynetbox)** for pushing data
- **YAML-based inventory** for extensibility

---

## 🎯 Real-World Use Case

In large enterprises with hundreds or thousands of routers and switches:
- Manual tracking of devices becomes error-prone
- Device misconfiguration and inventory drift becomes a risk
- Compliance auditing and config history is difficult to maintain

This project **automates** that entire workflow by:
- Dynamically discovering devices
- Syncing inventory into NetBox (used as the Source of Truth)
- Backing up configurations regularly
- Laying the foundation for compliance, visualization, and automation

---

## 💡 Key Benefits

- ✅ Eliminates manual inventory updates
- ✅ Provides centralized visibility via NetBox
- ✅ Ensures audit-ready device configuration backups
- ✅ Enables network compliance, change tracking, and automation workflows
- ✅ Can be extended to cloud environments, SD-WAN, firewalls, etc.

---

## 🏢 Where It's Used in Enterprises

- **Data Center Operations:** Automate discovery, backup, and documentation of critical core switches and routers.
- **Security Compliance Teams:** Maintain config snapshots for rollback, auditing, and SOC reviews.
- **Network Engineering Teams:** Automatically visualize topology in NetBox, integrate with CI/CD for zero-touch provisioning.
- **M&A and Onboarding Scenarios:** Rapidly discover and document newly acquired networks.

---

## 📁 Folder Structure

```
NetSecureCloudOps/
├── scripts/                        # All Python automation scripts
│   ├── discovery_and_push.py       # Discover devices & push them to NetBox
│   ├── config_backup.py            # Backup running configurations from devices
│   └── push_interfaces.py          # Push interface and IP details to NetBox
├── data/
│   └── devices.yml                 # YAML inventory of network devices (IP, credentials, type)
├── backups/
│   └── R1_config.txt               # Sample configuration backup of a device
├── requirements.txt                # Python dependencies to run the scripts
├── README.md                       # Project documentation and usage instructions
└── output_samples/                 # Sample visual outputs (GNS3 diagram, IPAM views, interfaces)
    ├── Netboxproject.gns3
    ├── gns_netops.png
    ├── Netops_Interfaceshtml
    ├── Netops_Ipam.html
    └── Netops_Pushinterfaces.html

```

---

## 🚀 How to Run

```bash
cd scripts/
python3 discovery_and_push.py     # Discover devices & sync with NetBox
python3 config_backup.py          # Backup running-configs
python3 push_interfaces.py        # Push interfaces and IPs
```

---

## 🔗 Requirements

- Python 3.8+
- NetBox up and running (Docker or production setup)
- SSH reachability to Cisco IOS devices
- Installed Python libraries:
  - `pynetbox`
  - `netmiko`
  - `pyyaml`
  - `packaging`

Install them all using:

```bash
pip3 install -r requirements.txt
```

---

## 📌 Roadmap (Next Phases)

- [ ] Config Compliance Checker (intended vs actual)
- [ ] Automatic Scheduled Backups
- [ ] Device Topology Mapping
- [ ] NetBox + Grafana Visualization
- [ ] AI-powered Config Insights (Phase 4)

---

## 🤝 Contribute / Extend

This project can be extended to:
- Palo Alto, Juniper, Arista devices
- SNMP-based discovery
- Integration with Ansible for automated remediation
- Web dashboard for change tracking

---

## 👨‍💻 Author

**Praneeth Reddy**  
Network Engineer & Automation Enthusiast  
> *This project is built to reflect what top companies like Meta, Amazon, and Cisco implement in real-time enterprise networks.*
