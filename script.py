import wmi,psutil,socket,uuid,re,dns,platform,os,nmap3,nmap
from dns import *
from datetime import datetime
import dns.resolver
import pwnedpasswords
import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror

def General_Information():
        #General Information of the System
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
        print(f"IP Address :{socket.gethostbyname(socket.gethostname())}")
        print(f"MAC Address:{':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

        #Missing network interfaces with last connected Time


def Network_Info():
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
    #Port Scanner script
    #Packet Analysis Script
    #Devices on Local Network Script

def Process_Analysis():
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
    #Recently running and MRU Script

def Memory_Analysis():
        print("---------Virtual Memory-------")
        cpu=psutil.virtual_memory()
        print(f"Total Memory :{cpu[0]/pow(10,9)} GB")
        print(f"Available :{cpu[1]/pow(10,9)} GB")
        print(f"Percent :{cpu[2]}%")
        print(f"Used :{cpu[3]/pow(10,9)} GB")
        print(f"Free :{cpu[4]/pow(10,9)} GB")

        print("-----Disks Usage--------")
        disk_usage=psutil.disk_usage("/")
        print(f"Total Memory :{disk_usage[0]/pow(10,9)} GB")
        print(f"Used :{disk_usage[1]/pow(10,9)} GB")
        print(f"Available :{disk_usage[2]/pow(10,9)} GB")
        print(f"Percent :{disk_usage[3]}%")

        print("------Disk Partition-------")
        disk_partition=psutil.disk_partitions(all=True)
        for i in disk_partition:
            print(i)
        
        print("--------CPU Usage----------")
        print(f"CPU Used in %: {psutil.cpu_percent(interval=None, percpu=False)} %")
        print("---------RAM Usage-----------")

        print('RAM memory % used:', psutil.virtual_memory()[2])

        print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)



def Folder_File():
        counter = 0
        print("Search for all files with a certain file type")
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
        #File path and size


def Account_Details():
        conn = wmi.WMI()
        #alluserdetails
        print("--------------Users----------------\n")
        for user in conn.Win32_UserAccount(): 
            print(user) 
        print("\n------------User Groups----------------\n")
        for group in conn.Win32_Group():
            print(group)
        print("---------------User Groups L--------------------")
        for group in conn.Win32_Group():
            print(group.Caption)
        for user in group.associators(wmi_result_class="Win32_UserAccount"):
            print(" [+]", user.Caption)

    #Login time of user , User password info , Reset Date

def External_devices():
         c = wmi.WMI()
         usb_devices = c.Win32_USBControllerDevice()

         for usb_device in usb_devices:
             device = usb_device.Dependent
             print(f"{device.Caption} connected at {datetime.datetime.now()}")


def Additional():
        print("-------Check if password is Pwned-------------")
        p=input("Enter the password being used for the organization: ")
        check=pwnedpasswords.check(p)

        if(check>0):
            print("You have been Pwned !! Change password")
        else:
            print("You havent been Pwned yet")

def getAllEvents(server, logtypes, basePath):
    """
    """
    if not server:
        serverName = "localhost"
    else: 
        serverName = server
    for logtype in logtypes:
        path = os.path.join(basePath, "%s_%s_log.log" % (serverName, logtype))
        getEventLogs(server, logtype, path)

#----------------------------------------------------------------------
def getEventLogs(server, logtype, logPath):
    """
    Get the event logs from the specified machine according to the
    logtype (Example: Application) and save it to the appropriately
    named log file
    """
    print ("Logging %s events" % logtype)
    log = codecs.open(logPath, encoding='utf-8', mode='w')
    line_break = '-' * 80
    
    log.write("\n%s Log of %s Events\n" % (server, logtype))
    log.write("Created: %s\n\n" % time.ctime())
    log.write("\n" + line_break + "\n")
    hand = win32evtlog.OpenEventLog(server,logtype)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    print ("Total events in %s = %s" % (logtype, total))
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand,flags,0)
    evt_dict={win32con.EVENTLOG_AUDIT_FAILURE:'EVENTLOG_AUDIT_FAILURE',
              win32con.EVENTLOG_AUDIT_SUCCESS:'EVENTLOG_AUDIT_SUCCESS',
              win32con.EVENTLOG_INFORMATION_TYPE:'EVENTLOG_INFORMATION_TYPE',
              win32con.EVENTLOG_WARNING_TYPE:'EVENTLOG_WARNING_TYPE',
              win32con.EVENTLOG_ERROR_TYPE:'EVENTLOG_ERROR_TYPE'}
    
    try:
        events=1
        while events:
            events=win32evtlog.ReadEventLog(hand,flags,0)
        
            for ev_obj in events:
                the_time = ev_obj.TimeGenerated.Format() #'12/23/99 15:54:09'
                evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID))
                computer = str(ev_obj.ComputerName)
                cat = ev_obj.EventCategory
                record = ev_obj.RecordNumber
                msg = win32evtlogutil.SafeFormatMessage(ev_obj, logtype)
                
                source = str(ev_obj.SourceName)
                if not ev_obj.EventType in evt_dict.keys():
                    evt_type = "unknown"
                else:
                    evt_type = str(evt_dict[ev_obj.EventType])
                log.write("Event Date/Time: %s\n" % the_time)
                log.write("Event ID / Type: %s / %s\n" % (evt_id, evt_type))
                log.write("Record #%s\n" % record)
                log.write("Source: %s\n\n" % source)
                log.write(msg)
                log.write("\n\n")
                log.write(line_break)
                log.write("\n\n")
    except:
        print (traceback.print_exc(sys.exc_info()))
                
    print ("Log creation finished. Location of log is %s" % logPath)
     
            
            


def main():

    print("Welcome to Digital Forensics and Incident Response Script")
    print("Press 1 for the General Information of the System")
    print("Press 2 for Network Information of the System")
    print("Press 3 for Process Analysis")
    print("Press 4 for Memory Analysis")
    print("Press 5 for File and Folder Analysis")
    print("Press 6 for Account Activities")
    print("Press 7 for External Devices analysis")
    print("Press 8 for Check Password Pwned or not")
    print("Press 9 to Save windows logs in a desired location")

    choice=int(input("Enter your choice :")) 
    server = None  # None = local machine
    logTypes = ["System", "Application", "Security"]
    
    if(choice==1):
        General_Information()
    elif(choice==2):
        Network_Info()
    elif(choice==3):
         Process_Analysis()
    elif(choice==4):
         Memory_Analysis()
    elif(choice==5):
         Folder_File()
    elif(choice==6):
         Account_Details()
    elif(choice==7):
         External_devices()
    elif(choice==8):
         Additional()
    elif(choice==9):
        getAllEvents(server, logTypes, input("Enter path for saving logs: "))




if __name__=='__main__':
    main()
