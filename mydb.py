import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Guildwars123###'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dailyplanner")

print("file executed!")