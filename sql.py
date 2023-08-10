import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",passwd="NULL",database="btti")
cur=conn.cursor()
print(cur)
lst=[]
lst_1=[]
try:
    dbs=cur.execute("select * from student ")
except:
    conn.rollback()
for i in cur:
    lst=i
    lst_1.extend(lst)
print(" \n") 
print(lst_1) 
print(type(lst_1))
import pandas as pd
df=pd.DataFrame(lst_1)
#print(df)
