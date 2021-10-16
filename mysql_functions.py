from mysql.connector import connect, Error


def mysql_connection_to_server():
	connection = None
	try:
		connection = connect(host="localhost", user="newuser2", password="Password32123")
	except Error as e:
		print(e)
	return connection


def mysql_create_database(database_name, mysql_con):
	query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
	cursor = mysql_con.cursor()
	cursor.execute(query)
	print("Create DB OK")


def mysql_connection_to_database(database_name):
	try:
		connection = connect(host="localhost", user="newuser2", password="Password32123", database=database_name)
		print("Connection DB OK")
		return connection
	except Error as e:
		print(e)


def mysql_create_table(mysql_con):
	query = """
		CREATE TABLE IF NOT EXISTS carsale(
				rowid INTEGER,
				company TEXT,
				brand TEXT, 
				model TEXT, 
				price INTEGER )"""
	cursor = mysql_con.cursor()
	cursor.execute(query)
	mysql_con.commit()


def mysql_insert(mysql_con, records):
	query = "INSERT INTO carsale (rowid, company, brand, model, price) VALUES (%s, %s, %s, %s, %s)"
	cursor = mysql_con.cursor()
	cursor.executemany(query, records)
	mysql_con.commit()


def mysql_select(mysql_con):
	query = "SELECT company, brand, model, price FROM carsale"
	cursor = mysql_con.cursor()
	cursor.execute(query)
	mysql_row_list = []
	for row in cursor:
		mysql_row_list.append(row)
	print(mysql_row_list)
	return mysql_row_list

