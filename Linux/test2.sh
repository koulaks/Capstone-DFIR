echo "______________________________Kernel information___________________________"
uname -v 
uname -r
echo "__________________________Network Hostname________________________"
uname -n
echo "___________________________Machine Hardware name___________________"
uname -a
echo "________________________CPU information__________________________"
 lscpu
echo "_______________________Linux blockdevice information____________"
lsblk -a
echo "_________________________USB controller information_____________"
lsusb 
echo "____________________________PCI device information_____________"
lspci -v
echo "____________________________Hardware components info_________"
sudo dmidecode -t memory


