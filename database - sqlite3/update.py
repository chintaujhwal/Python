import sqlite3

con = sqlite3.connect(r"c:\users\ujhwal\desktop\python\programs\database\employees.db")
cur = con.cursor()

x = int(input("Enter ID :"))
y = int(input("Enter SALARY :"))

try:
    cur.execute("update employees set SALARY = ? where ID = ?", (y, x))
    print("UPDATED...")
    con.commit()
except:
    print("ID NOT FOUND...")

con.close()
