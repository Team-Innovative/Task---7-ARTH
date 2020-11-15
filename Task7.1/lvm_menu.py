import os
while True:
	os.system("clear")
	os.system("tput setaf 6")
	print("\t\t\t\tWelcome to the LVM Menu...\n\n")
	print("""Press 1 to setup the NameNode
Press 2 to setup the DataNode
Press 3 to setup the LVM for DataNode
Press 4 to see the hadoop report
Press 5 to exit the program\n\n
""")

	ch = int(input("Enter your choice: "))

	if ch == 1:
		os.system("clear")
		print("You are now in name node\n")
		ip_address = input("Please Enter the Namenode IP: \n")
		input("NameNode IP: {}".format(ip_address))
		while True:
			os.system("clear")
			print("""\nPress 1 to setup hdfs file,
Press 2 to setup core.xml file,
Press 3 to format name node,
Press 4 to start Name Node,
Press 5 to check Name Node is running or not,
Press 6 to stop Name Node,
Press 7 to exit\n\n""")
			
			c = int(input("Enter your choice: "))
			if c == 1:
				os.system("scp name_hdfs_file.py root@{}:/root/".format(ip_address))
				os.system("ssh root@{} 'python3 name_hdfs_file.py'".format(ip_address))						
			elif c == 2:
				os.system("scp name_core_file.py root@{}:/root/".format(ip_address))
				os.system("ssh root@{} 'python3 name_core_file.py'".format(ip_address))						
			elif c == 3:
				os.system("ssh root@{} 'hadoop namenode -format'".format(ip_address))
			elif c == 4:
				os.system("ssh root@{} 'hadoop-daemon.sh start namenode'".format(ip_address))
			elif c == 5:
				os.system("ssh root@{} 'jps'".format(ip_address))
			elif c == 6:
				os.system("ssh root@{} 'hadoop-daemon.sh stop namenode'".format(ip_address))
			elif c == 7:
				break
			else:
				print("Please select correct Input from the given" )
			input("Press Enter to Continue...")
	elif ch == 2:
		os.system("clear")
		print("You are now in Data Node\n")
		ip_address = input("Please Enter the DataNode IP: \n")
		input("Datanode IP: {}".format(ip_address))
		while True:
			os.system("clear")
			print("""\nPress 1 to setup hdfs file,
Press 2 to setup core.xml file,
Press 3 to start Data Node,
Press 4 to check Data Node is running or not,
Press 5 to stop Data Node,
Press 6 to exit\n\n""")

			c = int(input("Enter the choice: "))
			if c == 1:
				os.system("scp data_hdfs_file.py root@{}:/root/".format(ip_address))
				os.system("ssh root@{} 'python3 data_hdfs_file.py'".format(ip_address))
			elif c == 2:
				os.system("scp data_core_file.py root@{}:/root/".format(ip_address))
				os.system("ssh root@{} 'python3 data_core_file.py'".format(ip_address))
			elif c == 3:
				os.system("ssh root@{} 'hadoop-daemon.sh start datanode'".format(ip_address))
			elif c == 4:
				os.system("ssh root@{} 'jps'".format(ip_address))
			elif c == 5:
				os.system("ssh root@{} 'hadoop-daemon.sh stop datanode'".format(ip_address))
			elif c == 6:
				break
			input("Press Enter to Continue..")
	elif ch == 3:
		os.system("clear")
		ip_address = input("Enter the Datanode IP: \n\n")
		input("Datanode IP: {}".format(ip_address))
		while True:
			os.system("clear")
			print("\t\t\t\tWelcome to the LVM Parititon Menu\n\n")
			print("""Press 1 for see the all disks
Press 2 (create/delete) a physical volume
Press 3 display the physical volume
Press 4 (create/delete) the volume group
Press 5 display the volume group
Press 6 (create/delete) the logical volume
Press 7 display the logical volume
Press 8 extend the logical volume
Press 9 (format/continue-format) the logical volume
Press 10 display the filesystem
Press 11 (mount/umount) the logical volume to that datanode folder
Press 12 exit the program
\n\n""")
			c = int(input("Enter your choice: "))
			if c == 1:
				os.system("ssh {} 'fdisk -l'".format(ip_address))
			elif c == 2:
				disk = input("What you want (create/delete): ")
				if disk == "create":
					physical = input("Enter your disk name: ")
					os.system("ssh root@{} 'pvcreate {}'".format(ip_address,physical))
				elif disk == "delete":
					physical = input("Enter your disk name: ")
					os.system("ssh root@{} 'pvremove {}'".format(ip_address,physical))
				else:
					print("Not Found")
			elif c == 3:
				physical = input("Enter your disk name: ")
				os.system("ssh root@{} 'pvdisplay {}'".format(ip_address,physical))
			elif c == 4:
				disk = input("What you want (create/delete): ")
				if disk == "create":
					volume = input("Enter your volume group name: ")
					physical1 = input("Enter your 1st physical disk name: ")
					physical2 = input("Enter your 2nd physical disk name: ")
					os.system("ssh root@{} 'vgcreate {} {} {}'".format(ip_address,volume,physical1,physical2))
				elif disk == "delete":
					volume = input("Enter your volume group name: ")
					os.system("ssh root@{} 'vgchange -an {}'".format(ip_address,volume))
					os.system("ssh root@{} 'vgremove {}'".format(ip_address,volume))
				else:
					print("Not Found")
			elif c == 5:
				volume = input("Enter your volume group name: ")
				os.system("ssh root@{} 'vgdisplay {}'".format(ip_address,volume))
			elif c == 6:
				disk = input("What you want (create/delete): ")
				if disk == "create":
					logical = input("Enter your logical volume name: ")
					volume = input("Enter your volume group name: ")
					size = input("Enter the size of logical volume (in G): ")
					os.system("ssh root@{} 'lvcreate --size {} --name {} {}'".format(ip_address,size,logical,volume))
				elif disk == "delete":
					logical = input("Enter your logical volume name: ")
					volume = input("Enter your volume group name: ")
					os.system("ssh root@{} 'lvchange -an /dev/{}/{}'".format(ip_address,volume,logical))
				else:
					print("Not Found")
			elif c == 7:
				logical = input("Enter your volume group name: ")
				os.system("ssh root@{} 'lvdisplay {}'".format(ip_address,logical))
			elif c == 8:
				volume = input("Enter your volume group name: ")
				logical = input("Enter your logical volume name: ")
				size = input("Enter the size of logical volume (in G): ")
				os.system("ssh root@{} 'lvextend --size +{} /dev/{}/{}'".format(ip_address,size,volume,logical))
			elif c == 9:
				disk = input("What do you want (format/continue-format): ")
				if disk == "format":
					volume = input("Enter your volume group name: ")
					logical = input("Enter your logical volume name: ")
					os.system("ssh root@{} 'mkfs.ext4 /dev/{}/{}'".format(ip_address,volume,logical))
				elif disk == "continue-format":
					volume = input("Enter your volume group name: ")
					logical = input("Enter your logical volume name: ")
					os.system("ssh root@{} 'resize2fs /dev/{}/{}'".format(ip_address,volume,logical))
				else:
					print("Not Found")
			elif c == 10:
				os.system("ssh root@{} 'df -h'".format(ip_address))
			elif c == 11:
				disk = input("What do you want (mount/umount): ")
				if disk == "mount":
					volume = input("Enter your volume group name: ")
					logical = input("Enter your logical volume name: ")
					datanode = input("Enter your datanode folder name: ")
					os.system("ssh root@{} 'mount /dev/{}/{}  /{}'".format(ip_address,volume,logical,datanode))
					print("Mounted Successfully")
				elif disk == "umount":
					datanode = input("Enter your datanode folder name: ")
					os.system("ssh root@{} 'umount /{}'".format(ip_address,datanode))
					print("Umounted Successfuly")
				else:
					print("Not Found")
			elif c == 12:
				break
			else:
				print("Choose different option")
			input("Press Enter to Continue...")
	elif ch == 4:
		ip_address = input("Enter (Namenode/Datanode) IP: \n\n")
		os.system("ssh root@{} hadoop dfsadmin -report".format(ip_address))
		input()
	elif ch == 5:
		print("Thank You for Using our Menu System\n")
		print("Created by Prabhjeet, Pallavi, Sadiya, Saurabh")
		exit()
	else:
		print("Please give correct input : Press 1,2,3,4 or 5 only")
	input("Please Enter to Continue...")

