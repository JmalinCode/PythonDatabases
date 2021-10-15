from mysql.connector import connect, Error


def mysql_connection_to_server():
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i")
		print(connection)
		print("Connection OK")
	except Error as e:
		print(e)


def mysql_create_database(database_name):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i")
		create_db_query = f"CREATE DATABASE {database_name}"
		cursor = connection.cursor()
		cursor.execute(create_db_query)
		print("Create DB OK")
	except Error as e:
		print(e)


def mysql_connection_to_database(database_name):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		print(connection)
		print("Connection DB OK")
	except Error as e:
		print(e)


def mysql_create_table(database_name):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		create_table_query = """
			CREATE TABLE IF NOT EXISTS carSale(
					RAWID INTEGER,
					company TEXT,
					brand TEXT, 
					model TEXT, 
					price INTEGER )"""
		cursor = connection.cursor()
		cursor.execute(create_table_query)
		connection.commit()
		print("Create Table OK")
	except Error as e:
		print(e)


def mysql_insert(database_name, table_name):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		records = [
		(0, "VAG", "Volkswagen", "Golf IV", "8000"),
		(1, "VAG", "Volkswagen", "CC", "15000"),
		(2, "VAG", "Volkswagen", "Q5", "35000"),
		]
		insert_table_query = f"INSERT INTO {table_name} (rawid, company, brand, model, price) VALUES (%s, %s, %s, %s, %s)"
		cursor = connection.cursor()
		cursor.executemany(insert_table_query, records)
		connection.commit()
		print("Insert OK")
	except Error as e:
		print(e)


def mysql_update(database_name, table_name, raw_id, new_price):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		update_query = f"UPDATE {table_name} SET price = {new_price} WHERE rawid={raw_id}"
		cursor = connection.cursor()
		cursor.execute(update_query)
		connection.commit()
		print("Update OK")
	except Error as e:
		print(e)


def mysql_delete_by_id(database_name, table_name, raw_id):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		delete_query = f"DELETE FROM {table_name} WHERE rawid = {raw_id}"
		cursor = connection.cursor()
		cursor.execute(delete_query)
		connection.commit()
		cursor.execute(f'OPTIMIZE TABLE {table_name};')
		print("Delete OK")
	except Error as e:
		print(e)


def mysql_select(database_name, table_name):
	try:
		connection = connect(host = "localhost", user = "anton", password = "3ntTP4+3_i", database = database_name)
		select_query = f"SELECT * FROM {table_name}"
		cursor = connection.cursor()
		cursor.execute(select_query)
		mysql_row_list = []
		for row in cursor:
			mysql_row_list.append(row)
		print("Select OK")
		print(mysql_row_list)
		return mysql_row_list
	except Error as e:
		print(e)
