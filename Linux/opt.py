import os

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print("----------Files in /opt folder ----------------")
for root, dirs, files in os.walk('/opt'):
    for name in files + dirs:
        path = os.path.join(root, name)
        if os.path.islink(path):
            print(f"{path} -> {os.readlink(path)}")
        else:
            print(f"{path} ({'dir' if os.path.isdir(path) else 'file'}) - {get_size(path)} bytes")
