import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikasverma"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")



