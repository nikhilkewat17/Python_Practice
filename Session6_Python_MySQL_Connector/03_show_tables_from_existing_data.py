import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)

cursor = connection.cursor()

cursor.execute("show tables ;")


tables = cursor.fetchall()
for i in tables:
    print("Tables in your database : " , i)

cursor.close()

connection.close()