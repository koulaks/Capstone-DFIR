import subprocess
import scapy
from scapy.all import sniff, rdpcap
from scapy.all import *
import psutil
import platform
import getmac
from scapy.all import *
import grp
import os
import psutil
import platform
#Added this for browser history
#from browserhistory import browser_history
#import browser_history

def show_menu():
    print("1. General Information")
    print("2. Network Information")
    print("3. Process Analysis")
    print("4. Memory Analysis")
    print("5. Files and Folder Analysis")
    print("6. Account Details")
    print("7. External Devices")
    print("8. PCAP file Analysis")
    print("9. Browser History")
    print("10. exit")

def operating_system_info():
    result = subprocess.run(["sw_vers"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))


def handle_packet(packet):
    # display the contents of the packet
    print(packet.summary())

def get_system_info():
    print("Manufacturer: Apple Inc.")
    print("Model: " + platform.mac_ver()[0])
    print("System: MacOS")
    print("Processor Name: " + platform.processor())
    print("Number of processors: " + str(psutil.cpu_count()))
    print("Total RAM: " + str(round(psutil.virtual_memory().total / (1024*1024*1024))) + " GB")
    print("Hostname: " + platform.node())
    print("IP Address: " + get_ip_address())
    #mac_address = getmac.get_mac_address(ip='192.168.1.1')
    # print("MAC Address: " + mac_address)
    

    # get a list of all network interfaces
    interfaces = psutil.net_if_stats().keys()

    # print the last time each interface was active
    print('Last time each network interface was active:')
    for interface in interfaces:
        stats = psutil.net_if_stats()[interface]
        last_time_active = stats.isup 
        print(f'  {interface}: {last_time_active}')

def account_activities():

    # get a list of all groups on the system
    groups = grp.getgrall()

    # iterate over the groups and print their details
    for group in groups:
        print(f"Group name: {group.gr_name}")
        print(f"Group ID: {group.gr_gid}")
        print(f"Group members: {group.gr_mem}")

    # define the dscl command to retrieve all users
    dscl_cmd = "dscl . -list /Users"

    # execute the dscl command and capture the output
    output = subprocess.check_output(dscl_cmd, shell=True)

    # decode the output from bytes to string
    output_str = output.decode("utf-8")

    # split the output into a list of lines and remove the first line
    user_names = output_str.split("\n")[1:-1]

    # iterate over the user names and print their details
    for user_name in user_names:
        # define the dscl command to retrieve user details
        dscl_cmd = f"dscl . -read /Users/{user_name}"
        
        # execute the dscl command and capture the output
        output = subprocess.check_output(dscl_cmd, shell=True)
        
        # decode the output from bytes to string
        output_str = output.decode("utf-8")
        
        # split the output into a list of lines
        output_lines = output_str.split("\n")
        
        # retrieve the user ID and group ID from the output
        uid_line = [line for line in output_lines if line.startswith("UniqueID:")]
        uid = uid_line[0].split(":")[1].strip()
        gid_line = [line for line in output_lines if line.startswith("PrimaryGroupID:")]
        gid = gid_line[0].split(":")[1].strip()
        
        # retrieve the login time of the user
        last_login_cmd = f"last -1 -t console {user_name}"
        last_login_output = subprocess.check_output(last_login_cmd, shell=True)
        last_login_str = last_login_output.decode("utf-8").split("\n")[0]
        last_login_time_str = " ".join(last_login_str.split()[5:10])
        
        # print the user information
        print(f"User name: {user_name}")
        print(f"User UID: {uid}")
        print(f"User group: {gid}")
        print(f"Last login time: {last_login_time_str}")
        
        print("")



def get_ip_address():
    result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    result_string = result.stdout.decode("utf-8")
    for line in result_string.split("\n"):
        if "inet " in line:
            return line.split(" ")[1]
    return None


def hostname_and_dns_info():
    result = subprocess.run(["scutil","--dns"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

def network_info():
    result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

def who_is_online():
    result = subprocess.run(["who"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

def list_disks():
    # Run shell command to list external devices
    cmd = "diskutil list"
    output = subprocess.check_output(cmd, shell=True)

    # Parse the output to get the list of external devices
    devices = output.decode('utf-8').strip().split('\n')

    # Iterate through each device and get the last connected time
    for device in devices:
        print(device)

def last_logged_in_users():
    result = subprocess.run(["last"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

def free_and_used_memory_info():
    result = subprocess.run(["top", "-l", "1"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

    print("mounted device\n")
    # Run shell command to list mounted devices
    cmd = "df -H"
    output = subprocess.check_output(cmd, shell=True)

    # Parse the output to get the list of mounted devices
    devices = output.decode('utf-8').strip().split('\n')[1:]

    # Iterate through each device and get its details
    for device in devices:
        # Extract the device details from the df output
        device_info = device.split()
        device_name = device_info[0]
        device_size = device_info[1]
        device_used = device_info[2]
        device_avail = device_info[3]
        device_mount = device_info[5]
        
        # Print the device details
        print(f"{device_name} ({device_size}) - {device_mount}")

def analyze_pcap_file():
    ##Please edit the pcap file name and save it on the same folder as this script.
    packets = rdpcap("testpcap0214.pcap")

    capture = sniff(count=50)
    for packet in capture:
        if packet.haslayer(UDP):
            print(packet.summary())  
        if packet.haslayer(TCP):
            print(packet.summary())

def process_info():
    #I want to add infor gathered from ps aux
    # I want to have startup proceeses AND the most recent processes
    print("#################################")
    print("   Process Information")
    print("#################################")
    print("The output is too long to print. Transfering to a textfile")
    output = subprocess.check_output(['sudo', 'launchctl', 'list'])
    print(output.decode('utf-8'))

def process_analysis():

    print("auto start service:\n")
        # Run launchctl command to get list of autostart services
    output = subprocess.check_output(["launchctl", "list"]).decode("utf-8")

    # Split the output by new lines to get each service as an item in a list
    services = output.strip().split("\n")

    # Print the list of services
    for service in services:
        print(service)


    # Run ps command to list all processes
    output = subprocess.check_output(["ps", "-eo", "pid,ppid,comm,state"]).decode("utf-8")

    # Split the output by new lines to get each process as an item in a list
    processes = output.strip().split("\n")

    # Remove the first line of the output (header)
    header = processes.pop(0)
    
    print("stopped service:\n")
    # Create a list of stopped processes

    stopped_processes = []
    for process in processes:
        # Split each process into a list of values
        values = process.split()
        # Check if the 'state' value is 'T' or 'Z'
        if values[3] in ["T", "Z"]:
            # Append the process name to the list of stopped processes
            stopped_processes.append(values[2])

    # Print the list of stopped processes

    print(stopped_processes)

def folders_and_files():
    ###Change this to not provide the path######

    # Get the directory path from the user
    search_dir = input("Enter the directory path to search in: ")

    # Get the file type/extension from the user
    file_type = input("Enter the file type/extension to search for (e.g. .txt): ")

    # Iterate through each file in the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(search_dir):
        for filename in filenames:
            # Check if the file has the desired file type/extension
            if filename.endswith(file_type):
                # Get the file path and size
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                
                # Print the file path and size
                print(f"{file_path} - {file_size} bytes")


#def browser_history():
    #print("\nFirefox Browsing History:")
    #print(browser_history -b Firefox)

    #print("\nChrome Browsing History:")
    #print(browser_history -b Chrome)

    #print("\nSafari Browsing History:")
    #print(browser_history -b Safari) 




def main():
    while True:
        show_menu()
        option = int(input("Enter your choice [1-10]: "))
        if option == 1:
            print("#################################")
            print(" Operating System Information:")
            print("#################################")
            operating_system_info()
            print("#################################")
            print("IP address and hostname info")
            print("#################################")
            hostname_and_dns_info()
        elif option == 2:
            print("#################################")
            print("Network info")
            print("#################################")
            network_info()
            # define a function to handle each packet that is captured
            # start capturing packets on the network interface for 30 seconds
            sniff(timeout=30, prn=handle_packet)
        elif option == 3:
            print("#################################")
            print("Process analysis")
            print("#################################")
            process_analysis()
            print("#################################")
            print("Auto start service")
            print("#################################")
            process_info()    
        elif option == 4:
            print("#################################")
            print("Memory Analysis")
            print("#################################")
            free_and_used_memory_info()    
        elif option ==5:
            print("#################################")
            print("Files and Folder Analysis")
            print("#################################")
            folders_and_files() 
        elif option == 6:
            print("#################################")
            print("List account activities")
            print("#################################")
            account_activities() 
            print("#################################")
            print("Who is online")
            print("#################################")
            who_is_online() 
            print("#################################")
            print("Last logged in users")
            print("#################################")
            last_logged_in_users()
        elif option ==7:
            print("#################################")
            print("External Devices/List disks")
            print("#################################")
            list_disks()     
        elif option == 8:
            print("#################################")
            print("Analyze pcap file")
            print("#################################")
            analyze_pcap_file()
        elif option == 9:
            print("#################################")
            print("Browser History")
            print("#################################")
            #browser_history()    
        elif option ==10:
            print("Exit")
            break
        else:
            print("Invalid option, try again")

if __name__ == '__main__':
    main()
