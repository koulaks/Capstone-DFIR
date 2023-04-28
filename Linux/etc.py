import os

etc_dir = '/etc'

# Get all files in etc directory
files = os.listdir(etc_dir)

# Print the full path of each file
for file in files:
    file_path = os.path.join(etc_dir, file)
    print(file_path)
