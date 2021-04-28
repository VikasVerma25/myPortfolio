import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vikasverma",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE comments (name VARCHAR(50), time VARCHAR(35), comment VARCHAR(1000))")
