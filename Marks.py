import mysqlconn
import imp
import pandas as pd

mycursor=mysqlconn.conn.cursor()

def SHOW():
    mycursor.execute("SELECT*FROM Test;")
    Data = mycursor.fetchall()
    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Test_ID', 'Marks', 'Total_Marks'])
    print(df)

def ADD():
    Val = []
    addsql = """
    INSERT INTO Marks (Enrollment_No, Test_ID, Marks, Total_Marks)
    VALUES (%s, %s, %s, %s)
    """

    n = int(input("Enter the number of entries you want to add= "))

    for i in range(n):
        entry = input("enter the details separated with comma -> \n(Enrollment_No, Test_ID, Marks, Total_Marks)= ")
        Check = tuple(x.strip() for x in entry.split(','))

        if Check[0] not in imp.en:
            print(" Cant go further, this does not Exist")
        else:
            Val.append(tuple(x.strip() for x in entry.split(',')))

    mycursor.executemany(addsql, Val)
    mysqlconn.conn.commit()

    showsql = """
    SELECT * FROM Marks;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Test_ID', 'Marks', 'Total_Marks'])
    print(df)

def EDIT():
    
    Enrollment_No = int(input("Enter the Enrollment_No of record you want to edit= "))
    if Enrollment_No not in imp.en:
        print("This Enrollment_No does not exist")
        Enrollment_No = int(input("Enter the correct Enrollment_No of record you want to edit= "))
    else:
        Choice3 = int(input("Enter\n1 for changing Test_ID\n2 for changing Marks\n3 for changing Total_Marks= "))
        
        if Choice3 == 1:
            ctest = input("Enter the correct Test_ID= ")
            editqery = """UPDATE Marks
            SET Test_ID=%s
            WHERE Enrollment_No=%s;"""
            mycursor.execute(editqery, (ctest, Enrollment_No))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            cmarks = int(input("Enter the correct Marks= "))
            editqery = """UPDATE Marks
            SET Marks=%s
            WHERE Enrollment_No=%s;"""
            mycursor.execute(editqery, (cmarks, Enrollment_No))
            mysqlconn.conn.commit()

        elif Choice3 == 3:
            ctotal = int(input("Enter the correct Total_Marks= "))
            editqery = """UPDATE Marks
            SET Total_Marks=%s
            WHERE Enrollment_No=%s;"""
            mycursor.execute(editqery, (ctotal, Enrollment_No))
            mysqlconn.conn.commit()

        else:
            print("INVALID CHOICE")

    showsql = """
    SELECT * FROM Marks;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Test_ID', 'Marks', 'Total_Marks'])
    print(df)

def DELETE():
    Enrollment_No = int(input("Enter Enrollment_No= "))

    while Enrollment_No not in imp.en:
        Enrollment_No = int(input("Enter the existing Enrollment_No= "))

    delsql = "DELETE FROM Marks WHERE Enrollment_No=%s"
    mycursor.execute(delsql, (Enrollment_No,))
    mysqlconn.conn.commit()
    print("Record deleted successfully ")

    showsql = """
    SELECT * FROM Marks;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Test_ID', 'Marks', 'Total_Marks'])
    print(df)

def SEARCH():
    
    Enrollment_No = int(input("Enter the Enrollment_No= "))

    while Enrollment_No not in imp.en:
        Enrollment_No = int(input("Enter the existing Enrollment_No= "))

    searchsql = "SELECT * FROM Marks WHERE Enrollment_No=%s"
    mycursor.execute(searchsql, (Enrollment_No,))
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Enrollment_No', 'Test_ID', 'Marks', 'Total_Marks'])
    print(df)