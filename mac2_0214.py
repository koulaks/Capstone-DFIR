import subprocess
import scapy
from scapy.all import sniff, rdpcap
from scapy.all import *
import psutil
import platform
import psutil
import platform
import os


# save to file
def save_to_file(output, file_name):
    with open(file_name, "w") as f:
        f.write(output)

def save_to_file(process_txt, file_name):
    with open(file_name, "w") as f:
        f.write(process_txt)

def show_menu():
    print("---------------------------")
    print("   Main Menu")
    print("---------------------------")
    print("1. Operating system and system info")
    print("2. Network and DNS info")
    print("3. Process info")
    print("4. Memory analysis")
    print("5. Files and Folder Analysis")
    print("6. Free and used memory info")
    print("7. PCAP file information")
    print("8. IP Addresses info")
    print("9. Acquisition")
    print("10. exit")


def get_ip_address():
    result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    result_string = result.stdout.decode("utf-8")
    for line in result_string.split("\n"):
        if "inet " in line:
            return line.split(" ")[1]
    return None


def os_and_system_info():
    result = subprocess.run(["sw_vers"], stdout=subprocess.PIPE)
    print("#################################")
    print(" Operating System Information:")
    print("#################################")
    print(result.stdout.decode("utf-8"))
 
    print("#################################")
    print("   System Information:")
    print("#################################")
    print("Manufacturer: Apple Inc.")
    print("Model: " + platform.mac_ver()[0])
    print("System: MacOS")
    print("Processor Name: " + platform.processor())
    print("Number of processors: " + str(psutil.cpu_count()))
    print("Total RAM: " + str(round(psutil.virtual_memory().total / (1024*1024*1024))) + " GB")
    print("Hostname: " + platform.node())
    print("IP Address: " + get_ip_address())
    print("MAC Address: " + ':'.join(re.findall('..', '%012x' % uuid.getnode())))
    print("\n")


def network_and_dns_info():
    # I am missing protocols here
    # I am also missing devices on local network -- arp subprocesses
    result = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    print("#################################")
    print("   Network Information")
    print("#################################")
    print(result.stdout.decode("utf-8"))

    print("#################################")
    print("   DNS Information")
    print("#################################")
    result = subprocess.run(["scutil","--dns"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8")) 
    print("\n")


def process_info():
    #I want to add infor gathered from ps aux
    # I want to have startup proceeses AND these are the most recent processes
    print("#################################")
    print("   Process Information")
    print("#################################")
    print("The output is too long to print. Transfering to a textfile")
    output = subprocess.check_output(['sudo', 'launchctl', 'list'])
    print(output.decode('utf-8'))
    print("\n")
   

def memory_analysis():
    print("####################################################")
    print("   Memory analysis")
    print("####################################################")
    memory = psutil.virtual_memory()
    print("Total: ")
    print(memory.total / (1024.0 ** 3))
    print("Available: " + str(memory.available / (1024.0 ** 3)))
    print("Used: " + str(memory.used / (1024.0 ** 3)))
    print("Percent: " + str(memory.percent))

    print("####################################################")
    print("   Free and Used Memory")
    print("####################################################")
    result = subprocess.run(["top", "-l", "1"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))
    print("\n")
    
    
def file_and_folder_analysis():
    print("####################################################")
    print("   File and Folder Analysis")
    print("####################################################")
    
    for root, dirs, files in os.walk("/Users/"):
        for file in files:
            file_path = os.path.join(root, file)
    print("The output is too long to print. Transfering to a textfile")   
    print("\n")     
  


def account_activities():
    #User information/Account activities
    print("####################################################")
    print("   The following user(s) are currently online")
    print("####################################################")
    result = subprocess.run(["who"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

    print("####################################################")
    print("   Last logged in users")
    print("####################################################")
    result = subprocess.run(["last"], stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))
    print("\n")


def analyze_pcap_file():
    print("####################################################")
    print("   Pcap file analysis")
    print("Please have the pcap file in the same location as this python file")
    print("####################################################")
    packets = rdpcap("testpcap.pcap")
    capture = sniff(count=50)
    for packet in capture:
        if packet.haslayer(UDP):
            print(packet.summary())  
        if packet.haslayer(TCP):
            print(packet.summary())
    print("\n")        


def acquisition():
    print("Working on updating this")
    print("\n")
  

def main():
    while True:
        show_menu()
        option = int(input("Enter your choice [1-9]: "))
        if option == 1:
            os_and_system_info()
        elif option == 2:
            network_and_dns_info()
        elif option == 3:
            process_info()
        elif option == 4:
            memory_analysis()
        elif option == 5:
            file_and_folder_analysis()
        elif option == 6:
            account_activities()
        elif option == 7:
            analyze_pcap_file()
        elif option == 8:
            more_info()
        elif option ==9:
            acqusition()
        elif option ==10:
            break
        else:
            print("Invalid option, try again")


if __name__ == '__main__':
    main()