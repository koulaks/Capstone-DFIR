import subprocess
print("------------Devices on Local Network------------")

# Use arp to determine devices on the local network
arp_result = subprocess.run(["arp", "-v"], capture_output=True, text=True)
print("Local network devices:")
print(arp_result.stdout)
