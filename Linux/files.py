import os

# Define the directory to list
directory = '/bin'

# Get a list of all files and directories in the specified directory
files_and_dirs = os.listdir(directory)

# Print the list
print("Files and directories in {} directory:".format(directory))
for item in files_and_dirs:
    print(item)
