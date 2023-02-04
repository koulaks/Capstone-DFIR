import platform
import os
import psutil
import socket
import datetime

# save to file
def save_to_file(output, file_name):
    with open(file_name, "w") as f:
        f.write(output)


def main():
    # General info (host name, timestamp, cpu, ram, etc.)
    output = "\nGeneral Info\n"
    output += "============\n"
    hostname = platform.node()
    timestamp = datetime.datetime.now()
    cpu = platform.processor()
    ram = psutil.virtual_memory().total / (1024.0 ** 3)
    
    output += "Host Name: " + hostname + "\n"
    output += "Timestamp: " + str(timestamp) + "\n"
    output += "RAM: " + str(ram) + "\n"
    output += "CPU: " + cpu + "\n"

    # Network analysis (ports, protocols, ip, etc.)
    ip = socket.gethostbyname(socket.gethostname())
    port_status = {}
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            port_status[port] = "OPEN"
        else:
            port_status[port] = "CLOSED"
        sock.close()
    
    output += "\nNetwork Info\n"
    output += "============\n"
    output += "Host IP: " + ip + "\n"
    output += "Port Status: " + str(port_status) + "\n"


    # Save to file
    save_to_file(output, "macos_output.txt")

if __name__ == "__main__":
    main()
