import mysqlconn
import imp
import pandas as pd

mycursor=mysqlconn.conn.cursor()


def SHOW():
    mycursor.execute("SELECT*FROM Test;")
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Test_ID', 'Test_Name', 'Course'])
    print(df)

def ADD():
    Val = []
    addsql = """
    INSERT INTO Test (Test_ID, Test_Name, Course)
    VALUES (%s, %s, %s)
    """

    n = int(input("Enter the number of entries you want to add= "))

    for i in range(n):
        entry = input("enter the details separated with comma -> \n(Test_ID, Test_Name, Course)= ")
        Check = tuple(x.strip() for x in entry.split(','))

        if Check[0] in imp.tst_ID:
            print(" Cant go further, this already Exist")
        else:
            Val.append(tuple(x.strip() for x in entry.split(',')))

    mycursor.executemany(addsql, Val)
    mysqlconn.conn.commit()

    showsql = """
    SELECT * FROM Test;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Test_ID', 'Test_Name', 'Course'])
    print(df)

def EDIT():
    
    Test_ID = input("Enter the Test_ID of record you want to edit= ")
    if Test_ID not in imp.tst_ID:
        print("This Test_ID does not exist")
        Test_ID = input("Enter the correct Test_ID of record you want to edit= ")
    else:
        Choice3 = int(input("Enter\n1 for changing Test_Name\n2 for changing Course= "))
        
        if Choice3 == 1:
            cname = input("Enter the correct Test_Name= ")
            editqery = """UPDATE Test
            SET Test_Name=%s
            WHERE Test_ID=%s;"""
            mycursor.execute(editqery, (cname, Test_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            ccourse = input("Enter the correct Course= ")
            editqery = """UPDATE Test
            SET Course=%s
            WHERE Test_ID=%s;"""
            mycursor.execute(editqery, (ccourse, Test_ID))
            mysqlconn.conn.commit()

        else:
            print("INVALID CHOICE")

    showsql = """
    SELECT * FROM Test;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Test_ID', 'Test_Name', 'Course'])
    print(df)

def DELETE():

    Test_ID = input("Enter Test_ID= ")

    while Test_ID not in imp.tst_ID:
        Test_ID = input("Enter the existing Test_ID= ")

    delsql = "DELETE FROM Test WHERE Test_ID=%s"
    mycursor.execute(delsql, (Test_ID,))
    mysqlconn.conn.commit()
    print("Record deleted successfully ")

    showsql = """
    SELECT * FROM Test;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Test_ID', 'Test_Name', 'Course'])
    print(df)

def SEARCH():
    Test_ID = input("Enter the Test_ID= ")

    while Test_ID not in imp.tst_ID:
        Test_ID = input("Enter the existing Test_ID= ")

    searchsql = "SELECT * FROM Test WHERE Test_ID=%s"
    mycursor.execute(searchsql, (Test_ID,))
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Test_ID', 'Test_Name', 'Course'])
    print(df)

    