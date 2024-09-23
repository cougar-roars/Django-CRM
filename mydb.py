
# import mysqlclient
# import pymysql
import mysql.connector


dateBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	password = 'password123',
	# dataBase = 'mysql',
	# sock = '3306'

	)

# prepare a cusor object
cursorObject=dateBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL Done!")