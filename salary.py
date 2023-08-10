# coding: utf-8
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
    print(i) 
    
for i in cur:  
    lst=i 
    lst_1.extend(lst) 
    
lst_1
i 
lst 
lst_1 
for i in cur:
    lst=i 
    lst_1.extend(lst) 
    
lst_1 
try:
    dbs=cur.execute("show tables") 
except:  
    conn.rollback() 
    
for i in cur: 
    lst=i 
    lst_1.extend(lst) 
    
lst_1
try:
    dbs=cur.execute("select * from salary") 
except:   
    conn.rollback() 
    
for i in cur:
    lst=i 
    lst_1.extend(lst) 
    
lst_1
lst_1.remove[3] 
lst_1.pop[3] 
get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('save', 'mysqli.py ')
get_ipython().run_line_magic('clear', '')
lst_1.pop(3) 
lst_1 
lst_1.pop(1) 
lst_1
for i in range(0,6) 
for i in range(0,6):
    lst_1.pop(i) 
    
lst_1 
for i in range(0,3):
    lst_1.pop(i) 
    
lst_1
