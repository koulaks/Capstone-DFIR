import scapy 
import sys
from scapy.all import *

capture = sniff(count=20)
with open("Networkanalysis.txt", "w") as f:
    for packet in capture:
        if packet.haslayer(UDP):
            f.write("UDP Packets\n")
            f.write(str(packet))
            f.write("\n\n")
        elif packet.haslayer(TCP):
            f.write("TCP Packets\n")
            f.write(str(packet))
            f.write("\n\n")
        else:
            f.write("All other packets\n")
            f.write(str(packet))
            f.write("\n\n")
