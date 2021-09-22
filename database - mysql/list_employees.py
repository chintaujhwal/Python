import mysql.connector
import json

f = open("connection.json")  # Open connection properties
config = json.loads(f.read())  # Convert JSON to dict

try:
    con = mysql.connector.connect(**config)
    cur = con.cursor()
    cur.execute("select * from employees")
    for i in cur.fetchall():
        print(f"{i[0]:2} {i[1]:20} {i[2]:10} {i[3]:10}")
    cur.close()
except Exception as ex:
    print("Error : ", ex)