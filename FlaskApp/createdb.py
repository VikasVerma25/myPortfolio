import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="######",
  password="######"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")



