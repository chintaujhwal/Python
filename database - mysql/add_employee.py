import mysql.connector
import json

f = open("connection.json")  # Open connection properties
config = json.loads(f.read())  # Convert JSON to dict

try:
    con = mysql.connector.connect(**config)
    cur = con.cursor()
    cur.execute("insert into employees(fullname,job,salary) values(%s,%s,%s)", ("Miranda", "DBA", "20000"))
    con.commit()
    cur.close()
except Exception as ex:
    print("Error : ", ex)
