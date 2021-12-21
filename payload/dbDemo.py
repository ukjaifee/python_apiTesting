import mysql.connector

from utilities.configuration import get_connection


conn = mysql.connector.connect(host='localhost', database='apidevelop', user='root', password='root')
print(conn.is_connected())

cursor = conn.cursor()  # cursor is used form a steam line between python and database
cursor.execute('select * from Books')
r = cursor.fetchone()
print(r)
# row = cursor.fetchall()  # If we are using fetchone befor that then it will skip first row as cursor is now on 1st when we say fetch all it will all remaining records, so if we want to print all then we have to comment fetchone
# print(row)
# print(row[1])
'''
'''
r1 = cursor.fetchall()
# print(r1)
m = 0
for row in r1:
    #print(rr[2])
    m = m + row[2]
print(m)
'''

'''''
query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()


conn.close()

con = get_connection()
print(con.is_connected())
cur = con.cursor()
cur.execute('select * from Books')
r = cur.fetchone()
print(r)
