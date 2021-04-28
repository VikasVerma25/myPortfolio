import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikasverma",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM comments")
mydb.commit()

