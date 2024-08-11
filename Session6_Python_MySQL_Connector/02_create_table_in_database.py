import mysql.connector

# make connection with database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nik358",
    database="nikcodermysqlpython"
)
# create cursor
cursor = connection.cursor()

# create table in database
table = "create table if not exists employee(id int not null primary key , name varchar(50), age int , dept varchar(30) , salary int ;)"
cursor.execute(table)


# commit data to database
connection.commit()
# close cursorh
cursor.close()

# close connection
connection.close()
