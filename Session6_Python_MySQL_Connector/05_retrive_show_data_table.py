import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)

cursor = connection.cursor()

# fetch data or retrive data .
sql = "select * from employee ;"

cursor.execute(sql)

show = cursor.fetchall()
for i in show:
    print(i)

cursor.close()

connection.close()

