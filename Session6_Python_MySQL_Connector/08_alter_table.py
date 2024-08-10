import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)

cursor = connection.cursor()

# fetch data or retrive data .
sql = "alter table employee add city varchar(30)"

# execute query
cursor.execute(sql)

# if any changes in database then commit it
connection.commit()



cursor.close()
connection.close()

