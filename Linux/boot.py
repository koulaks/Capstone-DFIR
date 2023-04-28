import os

boot_dir = "/boot"

print("--------------Files in Boot Folder--------------")

for filename in os.listdir(boot_dir):
    filepath = os.path.join(boot_dir, filename)
    if os.path.isfile(filepath):
        print("File name:", filename)
        print("File path:", filepath)
        print("File size:", os.path.getsize(filepath), "bytes")
        print("File modified:", os.path.getmtime(filepath))
