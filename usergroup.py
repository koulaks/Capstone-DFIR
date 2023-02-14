import wmi
conn = wmi.WMI()
#alluserdetails
print("Users\n")
for user in conn.Win32_UserAccount(): 
   print(user) 
print("\nUser Groups\n")
for group in conn.Win32_Group():
 print(group.Caption)
for user in group.associators(wmi_result_class="Win32_UserAccount"):
 print(" [+]", user.Caption)

