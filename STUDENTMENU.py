import imp
import details
import Batch
import Fees
import Test 
import Marks



def MENU():
    def OPTION():
        print("Enter\n1 for VIEWING YOUR PERSONAL DETAILS AND ATTENDANCE\n2 for VIEWING BATCH DETAILS\n3 for FEES DETAILS\n4 for MARKS")
        CHOICE=int(input("Enter The number=  \n"))
        while CHOICE not in range(1,5):
            CHOICE=int(input("Enter The Correct number=  \n"))
        
        return CHOICE

            
    x=OPTION()

    if x==1:
                details.SEARCH()
                print("TASK COMPLETES\n\n")
                x=OPTION()

    elif x==2:
                
                Batch.SEARCH()
                print("TASK COMPLETES\n\n")
                x=OPTION()

    elif x==3:
            
                Fees.SEARCH()
                print("TASK COMPLETES\n\n")
                x=OPTION()
                
    elif x==4:
                    
                Marks.SEARCH()
                print("TASK COMPLETES\n\n")
                x=OPTION()
    else:
            print("INVALID CHOICE")
            exit()
