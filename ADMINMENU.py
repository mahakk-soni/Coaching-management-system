import imp
import LOGINDATA
import Teacher_details

def MENU():
    def OPTION():
        print("ENTER \n 1 for New SIGN UP, \n 2 for Working on TEACHER DETAILS:= ")
        CHOICE=int(input("ENTER THE NUMBER= "))
        if CHOICE==1:
                def SIGNUP():
                    ROLE= input("ENTER THE ROLE (STUDENTS, TEACHERS, ADMINS)=")
                    role=ROLE.lower()
                    username=input("Enter the new username= ")
                    while username in (LOGINDATA.students or LOGINDATA.teachers or LOGINDATA.admins):
                            print("THIS USERNAME ALREADY EXISTS")
                            username=input("Enter the new username= ")
                    password=input("ENTER THE PASSWORD= ")
                    CONFIRM=input("CONFIRM YOUR PASSWORD= ")
                    for i in range(2):
                        while CONFIRM==password:
                            print("YOUR PASSWORD AND CONFIRMED PASSWORD WAS DIFFERENT")
                            password=input("ENTER THE PASSWORD AGAIN= ")
                            CONFIRM=input("CONFIRM YOUR PASSWORD AGAIN= ")
                        if i==1:
                                print("THEY ARE STILL DIFFERENT, EXITING DE TO SECURITY ISSUES")
                                exit()
                    if role=="students":
                            LOGINDATA.students[username]=password
                            print("SIGN UP SUCCESSFUL as a student")
                    elif role=="teachers":
                            LOGINDATA.teachers[username]=password
                            print("SIGN UP SUCCESSFUL as a teacher")
                    elif role=="admins":
                            LOGINDATA.admins[username]=password
                            print("SIGN UP SUCCESSFUL as an admin")
                    else:
                            print(" ENTER FROM (STUDENTS, TEACHERS, ADMINS)")
                            SIGNUP()
                SIGNUP()
                

        elif CHOICE==2:
                print("Enter\n1 for SHOWING ALL DETAILS\n2 for ADDING DETAILS\n3 for EDITING DETAILS\n4 for DELETING DETAILS\n5 for SEARCHING DETAILS from teacher_details= ")
                CRUDCHOICE= int(input("Enter The number=  \n"))
                return CRUDCHOICE
        else:
                print("INVALID CHOICE")
                OPTION()


    x=OPTION()

    print("Column Existing= ",imp.Teacher_columns)
    if x==1:
                        Teacher_details.SHOW()
                        print("TASK COMPLETES\n\n")
                        x=OPTION()
    elif x==2:
                        Teacher_details.details.ADD()
                        print("TASK COMPLETES\n\n")
                        x=OPTION()
    elif x==3:
                        Teacher_details.details.EDIT()
                        print("TASK COMPLETES\n\n")
                        x=OPTION()
    elif x==4:
                        Teacher_details.DELETE()
                        print("TASK COMPLETES\n\n")
                        x=OPTION()
    elif x==5:
                        Teacher_details.SEARCH()
                        print("TASK COMPLETES\n\n")
                        x=OPTION()
    else:
                        print("INVALID CHOICE\n")
                        print("TASK COMPLETES\n\n")
                        x=OPTION()