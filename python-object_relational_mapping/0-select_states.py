#!/usr/bin/python3
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', password='root', db='hbtn_0e_0_usa')

cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()

conn.close()