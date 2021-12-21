import mysql.connector

conn = mysql.connector.connect(host='localhost', database='apidevelop', user='root', password='root')
print(conn.is_connected())

cursor = conn.cursor()  # cursor is used form a steam line between python and database
cursor.execute('select * from apidevelop.customerinfo')
r = cursor.fetchone()
print(r)