import wmi
conn = wmi.WMI()
print("Running Processes\n")
for process in conn.Win32_Process():
 print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(
 process.ProcessId, process.HandleCount, process.Name
 ) )
print("\n Running Services\n")
for s in conn.Win32_Service(StartMode="Auto", State="Running"):
 print(s.State, s.StartMode, s.Name, s.DisplayName)
print("\n Stopped Services\n")
for s in conn.Win32_Service(StartMode="Auto", State="Stopped"):
 print(s.State, s.StartMode, s.Name, s.DisplayName)
print("User Groups")
for group in conn.Win32_Group():
 print(group.Caption)
for user in group.associators(wmi_result_class="Win32_UserAccount"):
 print(" [+]", user.Caption)
