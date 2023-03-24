import psutil
import wmi 
conn = wmi.WMI()
 
# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
print('The CPU usage is: ', psutil.cpu_percent(4))
for disk in conn.Win32_LogicalDisk():
 if disk.size != None:
    print(disk.Caption, "is {0:.2f}% free".format(
    100*float(disk.FreeSpace)/float(disk.Size))
 )