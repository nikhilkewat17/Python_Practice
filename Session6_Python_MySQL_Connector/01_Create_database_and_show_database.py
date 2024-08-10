# Let's connect to SQL.
# step1: Installed the required mysql connection.
# step2: Import the library.
# step3: Pass the encrypted password , username to make connection.
# step4: Create database in mysql.
# step5: create table in mysql.
# step6: Insert data into the created table.
# step7: create cursor.
# step8: Use cursor to query the data.
# step9: Do some CRUD operations.
# step10: Commit the changes to databases.


# First
# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password="nik358"
)
cursor = connection.cursor()
# sql = "show databases"
cursor.execute("create database if not exists nikcodermysqlpython ;")
cursor.execute("show databases ;")
res=cursor.fetchall()
for i in res:
    print(i)






