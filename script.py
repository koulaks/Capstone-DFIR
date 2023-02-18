import wmi,psutil,socket,uuid,re,dns,platform,os,nmap3
from dns import *
from datetime import datetime

import dns.resolver

def Genral_Info():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    print("-------GENERAL INFORMATION--------")
    print(f"Manufacturer: {my_system.Manufacturer}")
    print(f"Model: {my_system. Model}")
    print(f"Name: {my_system.Name}")
    print(f"Processor Name :{platform.processor()}")
    print(f"Number Of Processors: {my_system.NumberOfProcessors}")
    print(f"System Type: {my_system.SystemType}")
    print(f"System Family: {my_system.SystemFamily}")
    print(f"User Name: {my_system.UserName}")
    print(f"Total RAM: {round(int(my_system.TotalPhysicalMemory)/(1024*1024*1024))} GB")
    print(f"Workgroup: {my_system.Workgroup}")
    unaware = datetime.now()
    print('Timezone native:', unaware)
    f=open("Process.xls","w+")
    conn = wmi.WMI()
    print("Running Processes exported to Process.xlss\n")
    for process in conn.Win32_Process():
        f.write("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
        process.ProcessId, process.HandleCount, process.Name
    ) )
    f.close()
    f=open("Services.xls","w+")

    print("\n Running Services exported to Services.xls\n")
    for s in conn.Win32_Service(StartMode="Auto", State="Running"):
        f.write(f"{s.State, s.StartMode, s.Name, s.DisplayName}\n")
    f.close()
    print("\n Stopped Services exported to Stopped_Services.xls\n")
    f=open("Stopped_Services.xls","w+")
    for s in conn.Win32_Service(StartMode="Auto", State="Stopped"):
        f.write(f"{s.State, s.StartMode, s.Name, s.DisplayName}\n")
    f.close()
    print("User Groups")
    for group in conn.Win32_Group():
        print(group.Caption)
    for user in group.associators(wmi_result_class="Win32_UserAccount"):
        print(" [+]", user.Caption)

def Network_info():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    print("--------NETWORK INFORMATION--------")
    print(f"IP Address :{socket.gethostbyname(socket.gethostname())}")
    print(f"MAC Address:{':'.join(re.findall('..', '%012x' % uuid.getnode()))}")
    dns_resolver = dns.resolver.Resolver()
    dns_connected = dns_resolver.nameservers[0]
    print(f"DNS IP Address :{dns_connected}")
    dns_name=socket.gethostbyaddr(dns_connected)
    print(f"DNS Name :{dns_name[0]}")
    print(f"DNS Hostname: {my_system.DNSHostName}")
    print(f"Domain: {my_system.Domain}")
    print(f"Hostname :{socket.gethostname()}")

def User_Info():
    conn = wmi.WMI()
    #alluserdetails
    print("Users\n")
    for user in conn.Win32_UserAccount(): 
        print(user) 
    print("\nUser Groups\n")
    for group in conn.Win32_Group():
        print(group)
    for user in group.associators(wmi_result_class="Win32_UserAccount"):
     print(" [+]",group.name, ">", user.Caption)

def Type_File():
    counter = 0
    print("If you want all the excel file, for example write .xlsx")
    inp = input("What are you looking for?:> ")
    thisdir = os.getcwd()
    for r, d, f in os.walk("C:\\"): # change the hard drive, if you want
        for file in f:
            filepath = os.path.join(r, file)
            if inp in file:
                counter += 1
                print(os.path.join(r, file))
    print(f"Total {counter} files.")

def DHCP_Info():
    nmap=nmap3.Nmap()
    os.system('''ipconfig /all | findstr "DHCP" > dhcp.txt''')
    f=open("dhcp.txt","r+")
    g=f.read()
    matches = re.findall("(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", g)
    print(matches)
    for i in matches:
        print(f"------------Information about {i}--------------------")
        s=nmap.nmap_os_detection(i)
        print(s)

def Pwned():
        import pwnedpasswords
        p=input("Enter the password being used for the organization: ")
        check=pwnedpasswords.check(p)

        if(check>0):
            print("You have been Pwned !! Change password")
        else:
            print("You havent been Pwned yet")



def main():
    print("Welcome to Digital Forensics and Incidee Snt Responscript")
    print("Press 1 for General information of the System")
    print("Press 2 for Network Information of the System")
    print("Press 3 for User Information")
    print("Press 4 for Listing files based on filetype")
    print("Press 5 for Information about DHCP Server")
    print("Press 6 for Checking whether password has been Pwned")

    choice=int(input("Enter your choice :")) 

    if(choice==1):
        Genral_Info()
    elif(choice==2):
        Network_info()
    elif(choice==3):
        User_Info()
    elif(choice==4):
        Type_File()
    elif(choice==5):
        DHCP_Info()
    elif(choice==6):
        Pwned()
    else:
        print("Wrong choice")
if __name__=='__main__':
    main()
