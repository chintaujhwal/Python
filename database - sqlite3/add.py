import sqlite3

con = sqlite3.connect(r"c:\users\ujhwal\desktop\python\programs\database\employees.db")
cur = con.cursor()

x = input("Enter NAME :")
y = input("Enter JOB :")
z = int(input("Enter SALARY :"))

try:
    cur.execute("insert into employees(NAME,JOB,SALARY) values(?,?,?)", (x, y, z))
    print("ADDED...")
    con.commit()
except:
    print("ERROR...")

con.close()