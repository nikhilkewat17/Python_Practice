import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)

cursor = connection.cursor()

# insert single row data in table
insert_data = '''insert into employee(id,name,age,dept,salary)values(1,"Nikhil",26,"IT",900000);'''

cursor.execute(insert_data)


# insert multiple records in table using SQL injection.
insert = "insert into employee(id,name,age,dept,salary)values( %s , %s , %s , %s , %s)"
val = [
    (3,"Tejas",27,"IT",400000),
    (4,"Akash",27,"IT",450000),
    (5,"Aniket",21,"HR",20000)]

cursor.executemany(insert,val) # executemany when execute query multiple time.

connection.commit()

cursor.close()
connection.close()