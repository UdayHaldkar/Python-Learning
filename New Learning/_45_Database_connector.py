import mysql.connector

mydb =mysql.connector.connect(host="localhost", user="root",passwd="1234",database="uday")

my_cursor= mydb.cursor()

my_cursor.execute("show Databases")

for i in my_cursor:
    print(i)
