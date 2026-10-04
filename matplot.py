import mysqlconn
import pandas as pd
import matplotlib.pyplot as plt

mycursor= mysqlconn.conn.cursor()
mycursor.execute("SELECT Batch_ID, Total_student from batch_management;")
DATA = mycursor.fetchall()
df = pd.DataFrame(DATA, columns=['Batch_ID', 'Total_students'])
print(df)
arr1 = df['Batch_ID'].values
arr2= df['Total_students'].values
arr3=["#ADD8E6","#1E90FF", "#0000FF", "#191970" ]
arr4=[f'{arr1} ({arr2})' for arr1, arr2 in zip(arr1, arr2)]
Y= arr2
plt.pie(Y, labels= arr4,colors=arr3)
plt.title("No. Of students:")
plt.legend(title="Batch_ID",loc='upper left', bbox_to_anchor=(1,1.1))
plt.show()