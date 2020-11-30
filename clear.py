import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
def executeScriptsFromFile(filename):
	fd = open(filename, 'r')
	sqlFile = fd.read()
	fd.close()
	sqlCommands = sqlFile.split(';')

	for command in sqlCommands:
		try:
			if command.strip() != '':
				db.cursor().execute(command)
		except:
			print("Command skipped")

db.cursor().execute("DROP DATABASE IF EXISTS tp_db")
db.cursor().execute("CREATE DATABASE tp_db")

db.close()

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tp_db"
)

executeScriptsFromFile("naim.sql")
db.close()