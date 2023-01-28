import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")
print(f"DNS Hostname: {my_system.DNSHostName}")
print(f"Domain: {my_system.Domain}")
print(f"UserName: {my_system.UserName}")
print(f"Total Physical Memory: {int(my_system.TotalPhysicalMemory)//(1024*1024*1024)} GB")
print(f"Workgroup: {my_system.Workgroup}")
