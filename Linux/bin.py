import os

bin_dir = "/bin"
print(" -----------Executable Files in /bin folder-----------")
# Loop through each file in the bin directory
for filename in os.listdir(bin_dir):
    # Get the full path of the file
    file_path = os.path.join(bin_dir, filename)
    # Check if the file is a regular file and is executable
    if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
        # Print the file name and full path
        print(f"Executable file: {filename} ({file_path})")
