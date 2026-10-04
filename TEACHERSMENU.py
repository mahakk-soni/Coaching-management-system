import imp
import details
import Batch
import Fees
import Test 
import Marks
import Authentication

def MENU():
    def OPTION():
            print("Enter\n1 for Student_details\n2 for Batch_Management\n3 for Fees_Management\n4 for Test\n5 for Marks")
            CHOICE=int(input("Enter The number=  \n"))
            while CHOICE not in range(1,6):
                CHOICE=int(input("Enter The Correct number=  \n"))
            print("Enter\n1for SHOWING ALL DETAILS\n2 for ADDING DETAILS\n3 for EDITING DETAILS\n4 for DELETING DETAILS\n5 for SEARCHING DETAILS")
            CRUDCHOICE= int(input("Enter The number=  \n"))
            return CHOICE,CRUDCHOICE
    
    def taskcomplete():
            
            if EXIT.upper()=="YES":
                    x,y=OPTION()

            elif EXIT.upper=="NO":
                  Authentication.Login()
            else:
                    print("Wrong option selected") 
                    EXIT=input("Task completed, enter YES for contuing\n enter NO for exiting or LOGOUT= ") 

    x,y=OPTION()
    if x==1:
        print("Column Existing= ",imp.std_columns)
        if y==1:
                    details.SHOW()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==2:
                    details.ADD()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==3:
                    details.EDIT()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==4:
                    details.DELETE()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==5:
                    details.SEARCH()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        else:
                    print("INVALID CHOICE\n")
                    taskcomplete()


    elif x==2:
        print("Column Existing= ",imp.Batch_columns)
        if y==1:
                    Batch.SHOW()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==2:
                    Batch.ADD()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==3:
                    Batch.EDIT()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==4:
                    Batch.DELETE()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==5:
                    Batch.SEARCH()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        else:
                    print("INVALID CHOICE\n")
                    taskcomplete()

    elif x==3:
        print("Column Existing= ",imp.fee_columns)
        if y==1:
                    Fees.SHOW()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==2:
                    Fees.ADD()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==3:
                    Fees.EDIT()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==4:
                    Fees.DELETE()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==5:
                    Fees.SEARCH()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        else:
                    print("INVALID CHOICE\n")
                    taskcomplete()

    elif x==4:
        print("Column Existing= ",imp.tst_columns)
        if y==1:
                    Test.SHOW()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==2:
                    Test.ADD()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==3:
                    Test.EDIT()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==4:
                    Test.DELETE()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==5:
                    Test.SEARCH()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        else:
                    print("INVALID CHOICE\n")
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
    elif x==5:
        print("Column Existing= ",imp.marks_columns)
        if y==1:
                    Marks.SHOW()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==2:
                    Marks.ADD()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==3:
                    Marks.EDIT()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==4:
                    Marks.DELETE()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        elif y==5:
                    Marks.SEARCH()
                    print("TASK COMPLETES\n\n")
                    taskcomplete()
        else:
                    print("INVALID CHOICE\n")
                    taskcomplete()
    else:
            print("INVALID CHOICE")
            exit()
