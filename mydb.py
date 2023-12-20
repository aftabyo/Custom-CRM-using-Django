import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='@Ftab8198'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("all done")