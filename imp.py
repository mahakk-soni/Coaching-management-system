import mysqlconn

mycursor=mysqlconn.conn.cursor()
# information schema for Student details table
stdquery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'student_details'
AND table_schema = 'coaching_management';
"""
mycursor.execute(stdquery1)
std_columns = [x[0] for x in mycursor]
# print(std_columns)

stdquery2="""
SELECT DISTINCT Student_ID
FROM student_details;
"""
mycursor.execute(stdquery2)
std_ID=[x[0] for x in mycursor]
# print(std_ID)

stdquery3="""
SELECT DISTINCT Enrollment_No
FROM student_details;
"""
mycursor.execute(stdquery3)
en=[x[0] for x in mycursor]
# print(en)

stdquery4="""
SELECT DISTINCT Name
FROM student_details;
"""
mycursor.execute(stdquery4)
Name=[x[0] for x in mycursor]
# print(Name)


# information schema for batch management table
btcquery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'Batch_Management'
AND table_schema = 'coaching_management';
"""
mycursor.execute(btcquery1)
Batch_columns = [x[0] for x in mycursor]
# print(Batch_columns)

btcquery2="""
SELECT DISTINCT Batch_ID
FROM Batch_management;
"""
mycursor.execute(btcquery2)
Btc_ID=[x[0] for x in mycursor]
# print(Btc_ID)


# information schema for fees management table
feequery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'fees_management'
AND table_schema = 'coaching_management';
"""
mycursor.execute(feequery1)
fee_columns = [x[0] for x in mycursor]
# print(fee_columns)


# information schema for test table
testquery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'test'
AND table_schema = 'coaching_management';
"""
mycursor.execute(testquery1)
tst_columns = [x[0] for x in mycursor]
# print(tst_columns)

testquery2="""
SELECT DISTINCT Test_ID
FROM Test;
"""
mycursor.execute(testquery2)
tst_ID=[x[0] for x in mycursor]
# print(tst_ID)

testquery3="""
SELECT DISTINCT Test_Name
FROM Test;
"""
mycursor.execute(testquery3)
tstname=[x[0] for x in mycursor]
print(tstname)

# information schema for marks table
marksquery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'Marks'
AND table_schema = 'coaching_management';
"""
mycursor.execute(marksquery1)
marks_columns = [x[0] for x in mycursor]
#print(marks_columns)

# information schema for Teacher_details
tdquery1="""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'Teacher_details'
AND table_schema = 'coaching_management';
"""
mycursor.execute(tdquery1)
Teacher_columns = [x[0] for x in mycursor]
#print(Teacher_columns)

tchquery2="""
SELECT DISTINCT Teacher_ID
FROM Teacher_details;
"""
mycursor.execute(tchquery2)
tch_ID=[x[0] for x in mycursor]
# print(tch_ID)

