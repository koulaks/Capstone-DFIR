passwd_file = "/etc/passwd"

with open(passwd_file) as f:
    for line in f:
        # Split the line into fields
        fields = line.strip().split(":")
        # Extract the relevant fields
        username = fields[0]
        uid = fields[2]
        gid = fields[3]
        home_dir = fields[5]
        shell = fields[6]
        # Print the information
        print("Username:", username)
        print("UID:", uid)
        print("GID:", gid)
        print("Home directory:", home_dir)
        print("Shell:", shell)
        print()
