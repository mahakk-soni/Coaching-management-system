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

        mycursor.execute("SELECT * FROM student_details WHERE Batch_ID = %s",(BI,))
        Data = mycursor.fetchall()

        df = pd.DataFrame(Data, columns=['Student_ID', 'Enrollment_No', 'Batch_ID', 'Name', 'Course', 'Contact_No', 'Email', 'Attendance'])
        print(df)
    
    elif show==2:
        mycursor.execute("SELECT * FROM student_details")
        Data = mycursor.fetchall()

        df = pd.DataFrame(Data, columns=['Student_ID', 'Enrollment_No', 'Batch_ID', 'Name', 'Course', 'Contact_No', 'Email', 'Attendance'])
        print(df)
    
    else:
        print("INVALID CHOICE")
        show=int(input("ENTER 1 FOR SEEING DETAILS FOR ONE BATCH\n ENTER 2 FOR ALL BATCHES= "))

def ADD():
    Val=[]
    addsql="""
    INSERT INTO student_details(Student_ID, Enrollment_No, Name, Course, Contact_No, Email, Attendance)
    Values (%s, %s, %s, %s, %s, %s, %s) """
    n=int(input("Enter the number of entries you want to add= "))
    for i in range(n):
        entry= input("enter the deatils about a student separated with comma in a sequence-> \n(Student_ID, Enrollment_No, Name, Course, Contact_No, Email, Attendance)= ")
        Check=tuple(x.strip() for x in entry.split(','))
        if Check[0] in imp.std_ID:
            print(" Cant go further, this Student_ID Already Exist")
        elif Check[1] in imp.en:
            print(" Cant go further, this Enrollment_NO. Already Exist")
        else:
            Val.append(tuple(x.strip() for x in entry.split(',')))
        
    mycursor.executemany(addsql,Val)
    mysqlconn.conn.commit()

    showsql="""
    SELECT*FROM student_details;
    """
    mycursor.execute(showsql)
    Data = mycursor.fetchall()
    print("ENTRY ADDED SUCCESSFULLY")

    # df = pd.DataFrame(Data, columns=['Student_ID', 'Enrollment_No', 'Batch_ID', 'Name', 'Course', 'Contact_No', 'Email', 'Attendance'])
    # print(df)

def EDIT():
    Choice2 = int(input("enter\n1 for name\n2 for Course\n3 for Contact details\n4 for email\n5 for attendance= "))
    Choice3 = int(input("if you want to continue with \n student_ID enter 1\n or for enrollment_no enter 2 ="))

    if Choice2 == 1:
        if Choice3 == 1:
            Student_ID = input("Enter the student ID= ")
            Cname = input("enter the correct name= ")
            editsql = "UPDATE student_details SET Name=%s WHERE Student_ID=%s"
            mycursor.execute(editsql, (Cname, Student_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            Enrollment_No = int(input("Enter the student ID= "))
            Cname = input("enter the correct name= ")
            editsql = "UPDATE student_details SET Name=%s WHERE Enrollment_No=%s"
            mycursor.execute(editsql, (Cname, Enrollment_No))
            mysqlconn.conn.commit()

    elif Choice2 == 2:
        if Choice3 == 1:
            Student_ID = input("Enter the student ID= ")
            Ccourse = input("enter the correct Course= ")
            editsql = "UPDATE student_details SET Course=%s WHERE Student_ID=%s"
            mycursor.execute(editsql, (Ccourse, Student_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            Enrollment_No = int(input("Enter the student ID= "))
            Ccourse = input("enter the correct Course= ")
            editsql = "UPDATE student_details SET Course=%s WHERE Enrollment_No=%s"
            mycursor.execute(editsql, (Ccourse, Enrollment_No))
            mysqlconn.conn.commit()

    elif Choice2 == 3:
        if Choice3 == 1:
            Student_ID = input("Enter the student ID= ")
            Ccontact = int(input("enter the correct contact number= "))
            editsql = "UPDATE student_details SET Contact_No=%s WHERE Student_ID=%s"
            mycursor.execute(editsql, (Ccontact, Student_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            Enrollment_No = int(input("Enter the student ID= "))
            Ccontact = int(input("enter the correct contact number= "))
            editsql = "UPDATE student_details SET Contact_No=%s WHERE Enrollment_No=%s"
            mycursor.execute(editsql, (Ccontact, Enrollment_No))
            mysqlconn.conn.commit()

    elif Choice2 == 4:
        if Choice3 == 1:
            Student_ID = input("Enter the student ID= ")
            Cemail = input("enter the correct email= ")
            editsql = "UPDATE student_details SET Email=%s WHERE Student_ID=%s"
            mycursor.execute(editsql, (Cemail, Student_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            Enrollment_No = int(input("Enter the student ID= "))
            Cemail = input("enter the correct email= ")
            editsql = "UPDATE student_details SET Email=%s WHERE Enrollment_No=%s"
            mycursor.execute(editsql, (Cemail, Enrollment_No))
            mysqlconn.conn.commit()

    elif Choice2 == 5:
        if Choice3 == 1:
            Student_ID = input("Enter the student ID= ")
            Cattendance = int(input("enter the correct Attendance= "))
            editsql = "UPDATE student_details SET Attendance=%s WHERE Student_ID=%s"
            mycursor.execute(editsql, (Cattendance, Student_ID))
            mysqlconn.conn.commit()

        elif Choice3 == 2:
            Enrollment_No = int(input("Enter the student ID= "))
            Cattendance = int(input("enter the correct Attendace= "))
            editsql = "UPDATE student_details SET Attendance=%s WHERE Enrollment_No=%s"
            mycursor.execute(editsql, (Cattendance, Enrollment_No))
            mysqlconn.conn.commit()
    else:
        print("INVALID CHOICE")
        return

    showsql = "SELECT * FROM student_details"
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=['Student_ID', 'Enrollment_No', 'Batch_ID', 'Name', 'Course', 'Contact_No', 'Email', 'Attendance'])
    print(df)

def DELETE():
    Choice3 = int(input("1 Student_ID\n2 Enrollment_No\n"))

    if Choice3 == 1:

        if not imp.std_ID:
            print("No student ID available")
            return

        Student_ID = input("Enter the student ID= ")

        while Student_ID not in imp.std_ID:
            Student_ID = input("Enter the existing student ID= ")

        delsql = "DELETE FROM student_details WHERE Student_ID=%s"
        mycursor.execute(delsql, (Student_ID,))
        mysqlconn.conn.commit()

        print("Record deleted successfully ")

    elif Choice3 == 2:

        if not imp.en:
            print("No Enrollment Number available")
            return

        Enrollment_No = int(input("Enter Enrollment No= "))

        while Enrollment_No not in imp.en:
            Enrollment_No = int(input("Enter the existing Enrollment No= "))

        delsql = "DELETE FROM student_details WHERE Enrollment_No=%s"
        mycursor.execute(delsql, (Enrollment_No,))
        mysqlconn.conn.commit()

        print("Record deleted successfully ")

    else:
        print("Invalid choice")
        return

    showsql = "SELECT * FROM student_details"
    mycursor.execute(showsql)
    Data = mycursor.fetchall()

    df = pd.DataFrame(Data, columns=[
        'Student_ID', 'Enrollment_No', 'Batch_ID',
        'Name', 'Course', 'Contact_No', 'Email', 'Attendance'
    ])
    print(df)

def SEARCH():
    Choice3 = int(input("if you want to continue with \n student_ID enter 1\n or for enrollment_no enter 2 ="))

    if Choice3 == 1:
        if not imp.std_ID:
            print("No student ID available")
            return

        Student_ID = input("Enter the student ID= ")

        while Student_ID not in imp.std_ID:
            Student_ID = input("Enter the existing student ID= ")

        searchsql = "SELECT * FROM student_details WHERE Student_ID=%s"
        mycursor.execute(searchsql, (Student_ID,))
        Data = mycursor.fetchall()

    elif Choice3 == 2:
        if not imp.en:
            print("No Enrollment Number available")
            return

        Enrollment_No = int(input("Enter the Enrollment_No= "))

        while Enrollment_No not in imp.en:
            Enrollment_No = int(input("Enter the existing Enrollment No= "))

        searchsql = "SELECT * FROM student_details WHERE Enrollment_No=%s"
        mycursor.execute(searchsql, (Enrollment_No,))
        Data = mycursor.fetchall()

    else:
        print("Invalid choice")
        return

    df = pd.DataFrame(Data, columns=[
        'Student_ID', 'Enrollment_No', 'Batch_ID',
        'Name', 'Course', 'Contact_No', 'Email', 'Attendance'
    ])
    print(df)


