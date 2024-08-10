import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)

cursor = connection.cursor()

# fetch data or retrive data .
#sql = "update employee set name = 'Nikhil Kewat' where id = 1 ;"

sql = "update employee set city = 'Aurangabad' where id = 1 ;"

# execute query
cursor.execute(sql)

# if any changes in database then commit it
connection.commit()



cursor.close()
connection.close()

