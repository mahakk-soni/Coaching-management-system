import mysqlconn
import imp
import pandas as pd

mycursor=mysqlconn.conn.cursor()

def SHOW():
    show=int(input("ENTER 1 FOR SEEING DETAILS FOR ONE BATCH\n ENTER 2 FOR ALL BATCHES= "))
    if show==1:
        BI=input("Enter the Batch_ID of the students= ")
        
        while BI not in imp.Btc_ID:
            BI=input("Enter the Existing Batch_ID of the students= ")

        mycursor.execute("SELECT * FROM fees_management WHERE Batch_ID = %s",(BI,))
        Data = mycursor.fetchall()

        df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
        print(df)
    
    elif show==2:
        mycursor.execute("SELECT * FROM fees_management")
        Data = mycursor.fetchall()
        df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
        print(df)
    
    else:
        print("INVALID CHOICE")
        show=int(input("ENTER 1 FOR SEEING DETAILS FOR ONE BATCH\n ENTER 2 FOR ALL BATCHES= "))
   

def ADD():
    Val=[]
    addsql="""
    INSERT INTO fees_management(Enrollment_No, Total_fees, Amount_paid)
    Values (%s,%s, %s) """
    n=int(input("Enter the number of entries you want to add= "))
    for i in range(n):
        entry= input("enter the deatils about a student separated with comma in a sequence-> \nEnrollment_No, Total_fees, Amount_paid= ")
        Check=tuple(x.strip() for x in entry.split(','))
        if Check[0] in imp.en:
            print(" Cant go further, this Enrollment_No already exist")
        else:
            Val.append(tuple(x.strip() for x in entry.split(',')))
 
    mycursor.executemany(addsql,Val)
    mysqlconn.conn.commit()

    showsql="""
    SELECT*FROM fees_management;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
    print(df)

def EDIT():
    
    Enrollment_No=int(input("Enter the enrollment_no of student whoose record you want to edit="))
    if Enrollment_No not in imp.en:
        print("This Enrollment_No does not exist")
        Enrollment_No=int(input("Enter the correct enrollment_no of student whoose record you want to edit="))
    else:
        Choice3=int(input("Enter\n1 for changing Total_fees\n2 for changing Amount_paid= "))
        if Choice3==1:
            ctotal=int(input("Enter the correct Total_fees= "))
            editqery="""UPDATE fees_management
            SET Total_fees=%s
            WHERE Enrollment_No=%s;"""
            mycursor.execute(editqery,(ctotal,Enrollment_No))
            mysqlconn.conn.commit()
        elif Choice3==2:
            cpaid=int(input("Enter the correct Amount paid= "))
            editqery="""UPDATE fees_management
            SET Amount_paid=%s
            WHERE Enrollment_No=%s;"""
            mycursor.execute(editqery,(cpaid,Enrollment_No))
            mysqlconn.conn.commit()
        else:
            print("INVALID CHOICE")
    showsql="""
    SELECT*FROM fees_management;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
    print(df)

def DELETE():

    Enrollment_No = int(input("Enter Enrollment No= "))

    while Enrollment_No not in imp.en:
        Enrollment_No = int(input("Enter the existing Enrollment No= "))

    delsql = "DELETE FROM fees_management WHERE Enrollment_No=%s"
    mycursor.execute(delsql, (Enrollment_No,))
    mysqlconn.conn.commit()
    print("Record deleted successfully ")

    showsql="""
    SELECT*FROM fees_management;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
    print(df)

def SEARCH():
    Enrollment_No = int(input("Enter the Enrollment_No= "))

    while Enrollment_No not in imp.en:
        Enrollment_No = int(input("Enter the existing Enrollment No= "))

    searchsql = "SELECT * FROM fees_management WHERE Enrollment_No=%s"
    mycursor.execute(searchsql, (Enrollment_No,))
    Data = mycursor.fetchall()
    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Total_fees', 'Amount_paid', 'Amount_left'])
    print(df)

SEARCH()



    


