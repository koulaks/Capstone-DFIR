import wmi
import datetime

# create a WMI object
wmi_obj = wmi.WMI()

# retrieve the network interface device details
net_iface = wmi_obj.Win32_NetworkAdapterConfiguration(IPEnabled=True)

# iterate through the network interface devices and print their details
for iface in net_iface:
    print("Device: {}".format(iface.Description))
    print("MAC Address: {}".format(iface.MACAddress))
    print("IP Address(es): {}".format(iface.IPAddress))
    print("Connection Status: {}".format(iface.IPConnectionMetric))
    print("Connection Time: {}".format(datetime.datetime.fromtimestamp(int(iface.IPConnectionMetric)).strftime('%Y-%m-%d %H:%M:%S')))
    print("\n")
