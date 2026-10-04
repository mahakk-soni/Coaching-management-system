
import imp
import STUDENTMENU
import TEACHERSMENU
import ADMINMENU
import LOGINDATA



def Login():

    Role = int(input("Enter\n1 for login as STUDENTS\n2 for login as TEACHERS\n3 for login as ADMINS= "))

    if Role == 1:
        Username = input("Enter Your Username= ")
        while Username not in LOGINDATA.students:
            print("This Username Does not exist")
            Username = input("Enter Your Username= ")

        for i in range(3):
            password = input("Enter password: ")
            if password == LOGINDATA.students[Username]:
                print("Login successful!\n")
                STUDENTMENU.MENU()
                break
            else:
                print("Incorrect password.\n")

            if i == 2:
                print("Too many failed attempts. Exiting.")
                exit()

    elif Role == 2:
        Username = input("Enter Your Username= ")
        while Username not in LOGINDATA.teachers:   
            print("This Username Does not exist")
            Username = input("Enter Your Username= ")

        for i in range(3):
            password = input("Enter password: ")
            if password == LOGINDATA.teachers[Username]:  
                print("Login successful!\n")
                TEACHERSMENU.MENU()
                break
            else:
                print("Incorrect password.\n")

            if i == 2:
                print("Too many failed attempts. Exiting.")
                exit()

    elif Role == 3:
        Username = input("Enter Your Username= ")
        while Username not in LOGINDATA.admins:
            print("This Username Does not exist")
            Username = input("Enter Your Username= ")

        for i in range(3):
            password = input("Enter password: ")
            if password == LOGINDATA.admins[Username]:   
                print("Login successful!\n")
                ADMINMENU.MENU()
                break
            else:
                print("Incorrect password.\n")

            if i == 2:
                print("Too many failed attempts. Exiting.")
                exit()

    else:
        print("INVALID CHOICE")
        Role = int(input("Enter\n1 for login as STUDENTS\n2 for login as TEACHERS\n3 for login as ADMINS= "))

Login()