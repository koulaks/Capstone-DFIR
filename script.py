#!/usr/local/bin/python
import os

def General_Info():
	os.system("./test.sh")
	os.system("./test2.sh")

def Network_Info():
	os.system("python3 networkinfo.py")
	os.system("./net_info.sh")
	os.system("./openports.sh")
	os.system("python3 arp.py")
def Process():
	print("----------Autostart Services--------------")
	os.system("./autostart.sh")
	print("-----------Currently Running Services-------------")
	os.system("python3 running.py")
	print("-----------Stopped Services--------------------")
	os.system("./stoppedservices.sh")

def User_Info():
	os.system("python3 passwd.py")

def Files():
	os.system("python3 files.py")
	os.system("python3 etc.py")
	os.system("python3 bin.py")
	os.system("python3 boot.py")
	os.system("python3 opt.py")
	
def Browser():
	print("-----------Browser Analysis------------------")
	os.system("python3 browser.py")

def Logs():
	print("----------------Boot Logs-----------------")
	os.system("cat /var/log/boot.log")
	print("-----------------Syslog-------------------")
	os.system("cat /var/log/syslog")
	print("----------------User logs---------------")
	os.system("cat /var/log/user.log")


def main():
	print("Press 1 for General Information")
	print("Press 2 for Network Information")
	print("Press 3 for Process Analysis")
	print("Press 4 for Users Information")
	print("Press 5 for File & Folders in the System")
	print("Press 6 for Browser Analysis")
	print("Press 7 for Logs ")

	choice=int(input("Enter your choice: "))
	if(choice==1):
		General_Info()
	elif(choice==2):
		Network_Info()
	elif(choice==3):
		Process()
	elif(choice==4):
		User_Info()
	elif(choice==5):
		Files()
	elif(choice==6):
		Browser()
	elif(choice==7):
		Logs()
	else:
		print("Wrong Choice!!! ")

if __name__ == "__main__":
    main()

