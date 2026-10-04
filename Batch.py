import mysqlconn
import imp
import pandas as pd

mycursor=mysqlconn.conn.cursor()

def SHOW():
    mycursor.execute("SELECT*FROM Batch_Management;")
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Batch_ID', 'Total_students', 'Starting_Date', 'Ending_Date'])
    print(df)

def ADD():
    Val=[]
    addsql="""
    INSERT INTO Batch_Management(Batch_ID, Starting_Date, Ending_Date)
    Values (%s,%s, %s) """
    n=int(input("Enter the number of entries you want to add= "))
    for i in range(n):
        entry= input("enter the deatils about a student separated with comma in a sequence-> \n(Batch_ID,\nStarting_Date( IN FORMAT YYYY-MM-DD ),\nEnding_Date( IN FORMAT YYYY-MM-DD ))= ")
        Check=tuple(x.strip() for x in entry.split(','))
        if Check[0] in imp.std_ID:
            print(" Cant go further, this Student_ID Already Exist")
        elif Check[1] in imp.en:
            print(" Cant go further, this Enrollment_NO. Already Exist")
        else:
            Val.append(tuple(x.strip() for x in entry.split(',')))
 
    mycursor.executemany(addsql,Val)
    mysqlconn.conn.commit()
    tsquery="""UPDATE Batch_Management b
    SET Total_student = (
    SELECT COUNT(*)
    FROM student_details s
    WHERE s.Batch_ID = b.Batch_ID
    );"""
    mycursor.execute(tsquery)
    mysqlconn.conn.commit()

    showsql="""
    SELECT*FROM Batch_Management;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Batch_ID', 'Total_students', 'Starting_Date', 'Ending_Date'])
    print(df)

def EDIT():

    Choice2=int(input("Enter\n1 for changing Starting_Date\n2 for changing Ending_Date= "))
    Batch_ID=input("Enter The Batch_ID of the Batch= ")
    if Batch_ID not in imp.Btc_ID:
        print("this Batch_ID does not exist")
        Batch_ID=input("Enter The Batch_ID of the Batch= ")
    else:
        if Choice2==1:
            Csdate=input("Enter the correct Starting_Date(IN FORMAT YYYY-MM-DD)= ")
            editqery="""UPDATE Batch_Management
            SET Starting_Date=%s
            WHERE Batch_ID=%s;"""
            mycursor.execute(editqery,(Csdate,Batch_ID))
            mysqlconn.conn.commit()

        elif Choice2==2:
            Cedate=input("Enter the correct Ending_Date(IN FORMAT YYYY-MM-DD)= ")
            editqery="""UPDATE Batch_Management
            SET Ending_Date=%s
            WHERE Batch_ID=%s;"""
            mycursor.execute(editqery,(Cedate,Batch_ID))
            mysqlconn.conn.commit()

        else:
            print("INVALID CHOICE")
            return
    

    showsql = "SELECT * FROM Batch_Management;"
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Batch_ID', 'Total_student','Starting_Date','Ending_Date'])
    print(df)

def DELETE():
    Batch_ID=input("enter the Batch_ID of the record you want to delete= ")
    if Batch_ID not in imp.Btc_ID:
        print("this Batch_ID does not exist")
        Batch_ID=input("Enter The Batch_ID of the Batch= ")
        x=1
    else:
        delquery="""DELETE FROM Batch_Management
        WHERE Batch_ID=%s"""
        mycursor.execute(delquery,(Batch_ID,))
    showsql = "SELECT * FROM Batch_Management;"
    mycursor.execute(showsql)
    
    Data = mycursor.fetchall()
    mysqlconn.conn.commit()

    df = pd.DataFrame(Data, columns=['Batch_ID', 'Total_student','Starting_Date','Ending_Date'])
    print(df) 

def SEARCH():
    Batch_ID=input("enter the Batch_ID of the record you want to view details about= ")
    if Batch_ID not in imp.Btc_ID:
        print("this Batch_ID does not exist")
        Batch_ID=input("Enter The Batch_ID of the Batch= ")
        x=1
    else:
        searchsql="""SELECT*FROM Batch_Management
        WHERE Batch_ID=%s"""
        mycursor.execute(searchsql,(Batch_ID,))
        Data=mycursor.fetchall()
    df = pd.DataFrame(Data, columns=['Batch_ID', 'Total_student','Starting_Date','Ending_Date'])
    print(df) 

