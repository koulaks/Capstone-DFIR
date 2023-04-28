import subprocess

# Get network interface information using ifconfig
ifconfig_result = subprocess.run(["ifconfig"], capture_output=True, text=True)
print("Network Interfaces:")
print(ifconfig_result.stdout)


