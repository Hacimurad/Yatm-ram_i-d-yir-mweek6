global studentlist
studentlist = ["1,Hacimurad,Azizov,murad.azizov.99@mail.ru,553915277",
               "2,Turan,Nesirzade,turan.nesirzade.99@mail.ru,554445566",
               "3,Ramiz,Osmanov,ramiz.osmanov.99@mail.ru,557435454",
               "4,Orxan,Eliyev,orxan.eliyev.99@mail.ru,553435465",
               "5,Haci,Tehmezov,haci.azizov.99@mail.ru,553915567",
               "6,Eli,Eliyev,eli.eliyev.99@mail.ru,553956777",
               "7,Anar,Baxisov,anar.baxisov.99@mail.ru,553915487",
               "8,Ferid,Gulum,ferid.gulum.99@mail.ru,553917897",
               "9,Mehman,Mehmanov,mehman.mehmanov.99@mail.ru,553915697",
               "10,Selim,Azizov,selim.azizov.99@mail.ru,553917656",]

def studentmanagement():
#secenekler
	print("\n++++++ Welcome to Pragmatech Student Management System ++++++\n")
	print("[Choice 1: Showing the List of Student]")
	print("[Choice 2: Add New Student]")
	print("]Choice 3: Searching Student]")
	print("[Choice 4: Deleting a Student]\n")

	try:
		x = int(input("Enter a choice: "))
	except ValueError:
		exit("\nHy! This is not a Number")
	else:
		print("\n")
#1 ci secim ucun
	if(x==1):
		print("Student List\n")
		for students in studentlist:
			print("++ {} ++".format(students))
#2ci secim ucen
	elif(x==2):
		studentnew = input("Enter New Student: ")
		if(studentnew in studentlist):
			print("\nThis Student {} Already In The Table".format(studentnew))
		else:
			studentlist.append(studentnew)
			print("\n++ New Student {} Added Successfully ++\n".format(studentnew))
			for students in studentlist:
				print("++ {} ++".format(students))
#3 cu secim ucun
	elif(x==3):

		studentsearching = input("Choose Student Name To Search: ")
		if(studentsearching in studentlist):
			print("\n++ There is a Record Found of this Student {} ++".format(studentsearching))
		else:
			print("\n++ There is No Record Found Of this Student {} ++".format(studentsearching))
# 4cu secim ucun
	elif(x==4):
		studentdelete = input("Choose a Student Name To Delete: ")
		if(studentdelete in studentlist):
			studentlist.remove(studentdelete)
			for students in studentlist:
				print("++ {} ++".format(students))
		else:
			print("\n++ There is No Record Found of This Student {} ++".format(studentdelete))

	elif(x < 1 or x > 4):
		print("Please Enter Valid Choice")

studentmanagement()

def continueAgain():
	runningagain = input("\nWant to continue the process yes/no?: ")
	if(runningagain.lower() == 'yes'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		quit()

continueAgain()