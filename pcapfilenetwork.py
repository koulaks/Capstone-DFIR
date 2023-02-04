import scapy 
import sys
from scapy.all import *
packets = rdpcap(r'C:\Users\aksha\OneDrive\Desktop\Tools\testpcpap.pcap')
#packets.summary()  
#for packet in packets:
 #   if packet.haslayer(UDP):
        #print(packet.summary())  
  #  if packet.haslayer(TCP):
       #print(packet.show())  
capture= sniff(count=50)
#capture.summary()
for packet in capture:
    if packet.haslayer(UDP):
        print(packet.summary())  
    if packet.haslayer(TCP):
       print(packet.show())
