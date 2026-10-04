import mysqlconn
import imp
import pandas as pd

mycursor=mysqlconn.conn.cursor()

def SHOW():
    mycursor.execute("SELECT * FROM Teacher_details;")
    Data = mycursor.fetchall()

    df = pd.DataFrame(
        Data,
        columns=[
            'Teacher_ID',
            'Name',
            'Gender',
            'Contact_No',
            'Email',
            'Joining_Date',
            'Subject',
            'Salary'
        ]
    )
    
    print(df)

def ADD():

    Val = []
    addsql = """
    INSERT INTO Teacher_details
    (Teacher_ID, Name, Gender, Contact_No, Email, Joining_Date, Subject, Salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    n = int(input("Enter the number of entries you want to add= "))

    for i in range(n):
        entry = input(
            "Enter details separated by comma ->\n"
            "(Teacher_ID, Name, Gender, Contact_No, Email, Joining_Date (in FORMAT YYYY-MM-DD), Subject, Salary)= "
        )

        Check = tuple(x.strip() for x in entry.split(','))

      
        if Check[0] in imp.tch_ID:  
            print("Can't go further, this Teacher_ID already exists")
        else:
            Val.append(Check)

    mycursor.executemany(addsql, Val)
    mysqlconn.conn.commit()

   
    showsql = "SELECT * FROM Teacher_details;"
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(
        Data,
        columns=[
            'Teacher_ID',
            'Name',
            'Gender',
            'Contact_No',
            'Email',
            'Joining_Date',
            'Subject',
            'Salary'
        ]
    )
    print(df)  

def EDIT():

    Choice2 = int(input(
        "enter\n"
        "1 for EDITING Gender\n"
        "2 for EDITING Contact details\n"
        "3 for EDITING Email\n"
        "4 for EDITING Joining Date\n"
        "5 for EDITING Subject\n"
        "6 for EDITITNG Salary\n= "
    ))

    Teacher_ID = input("Enter the Teacher ID= ")

    while Teacher_ID not in imp.tch_ID:
        Teacher_ID = input("Enter the existing Teacher ID= ")

    if Choice2 == 1:
        Cgender = input("Enter correct Gender= ")
        editsql = "UPDATE Teacher_details SET Gender=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Cgender, Teacher_ID))

    elif Choice2 == 2:
        Ccontact = int(input("Enter correct Contact Number= "))
        editsql = "UPDATE Teacher_details SET Contact_No=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Ccontact, Teacher_ID))

    elif Choice2 == 3:
        Cemail = input("Enter correct Email= ")
        editsql = "UPDATE Teacher_details SET Email=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Cemail, Teacher_ID))

    elif Choice2 == 4:
        Cdate = input("Enter correct Joining Date (YYYY-MM-DD)= ")
        editsql = "UPDATE Teacher_details SET Joining_Date=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Cdate, Teacher_ID))

    elif Choice2 == 5:
        Csubject = input("Enter correct Subject= ")
        editsql = "UPDATE Teacher_details SET Subject=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Csubject, Teacher_ID))

    elif Choice2 == 6:
        Csalary = int(input("Enter correct Salary= "))
        editsql = "UPDATE Teacher_details SET Salary=%s WHERE Teacher_ID=%s"
        mycursor.execute(editsql, (Csalary, Teacher_ID))

    else:
        print("INVALID CHOICE")
        return

    mysqlconn.conn.commit()

    # Show updated table
    mycursor.execute("SELECT * FROM Teacher_details")
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=[
        'Teacher_ID',
        'Name',
        'Gender',
        'Contact_No',
        'Email',
        'Joining_Date',
        'Subject',
        'Salary'
    ])
    print(df)

def DELETE():
    if not imp.tch_ID:
        print("No Teacher ID available")
        return

    Teacher_ID = input("Enter the Teacher ID you want to delete Record of= ")

    while Teacher_ID not in imp.tch_ID:
        Teacher_ID = input("Enter the existing Teacher ID= ")

    delsql = "DELETE FROM Teacher_details WHERE Teacher_ID=%s"
    mycursor.execute(delsql, (Teacher_ID,))
    mysqlconn.conn.commit()

    print("Record deleted successfully ")

    showsql = "SELECT * FROM Teacher_details"
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=[
        'Teacher_ID',
        'Name',
        'Gender',
        'Contact_No',
        'Email',
        'Joining_Date',
        'Subject',
        'Salary'
    ])
    print(df)

