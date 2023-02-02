import wmi,psutil,socket,uuid,re,dns,platform
from dns import *
from datetime import datetime
import pytz
import dns.resolver

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Model: {my_system. Model}")
print(f"Name: {my_system.Name}")
print(f"Processor Name :{platform.processor()}")
print(f"Number Of Processors: {my_system.NumberOfProcessors}")
print(f"System Type: {my_system.SystemType}")
print(f"System Family: {my_system.SystemFamily}")
print(f"DNS Hostname: {my_system.DNSHostName}")
print(f"Domain: {my_system.Domain}")
print(f"User Name: {my_system.UserName}")
print(f"Total RAM: {round(int(my_system.TotalPhysicalMemory)/(1024*1024*1024))} GB")
print(f"Workgroup: {my_system.Workgroup}")
print(f"Hostname :{socket.gethostname()}")
print(f"IP Address :{socket.gethostbyname(socket.gethostname())}")
print(f"MAC Address:{':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

# current Datetime
unaware = datetime.now()
print('Timezone native:', unaware)
dns_resolver = dns.resolver.Resolver()
dns_connected = dns_resolver.nameservers[0]
print(f"DNS IP Address :{dns_connected}")
dns_name=socket.gethostbyaddr(dns_connected)
print(f"DNS Name :{dns_name[0]}")
