import sqlite3

con = sqlite3.connect(r"c:\users\ujhwal\desktop\python\programs\database\employees.db")
cur = con.cursor()
cur.execute("select * from employees")

for n in cur.fetchall():
    print(f"{n[0]} {n[1]:10} {n[2]:10} {n[3]:10}")

x = input("\nEnter ID :")

try:
    cur.execute("delete from employees where ID = ?", x)
    print("DELETED...")
    con.commit()
except:
    print("ID NOT FOUND...")

con.close()
