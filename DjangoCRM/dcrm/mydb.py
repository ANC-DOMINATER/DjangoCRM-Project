import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE DOMINATOR")
print("Database created succussfully")



