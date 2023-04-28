import subprocess

# Run the systemctl command to list recent services
command = "systemctl list-units --type=service --state=running --no-pager --no-legend "
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

# Read the output of the command and print it
output, error = process.communicate()
print(output.decode())
