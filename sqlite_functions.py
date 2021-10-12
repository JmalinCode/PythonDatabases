import sqlite3
from sqlite3 import Error


def sqlite_connection(database_name):
	"""
		function connects to sqlite database
	"""
	try:
		sqlite_con = sqlite3.connect(f"db/{database_name}.db")
		return sqlite_con
	except Error:
		print(Error)


def sqlite_table_create(sqlite_con):
	"""
		function creates new table
	"""
	cursor = sqlite_con.cursor()
	query = """ CREATE TABLE IF NOT EXISTS carSale(
		company TEXT,
		brand TEXT, 
		model TEXT, 
		price INTEGER )"""
	cursor.execute(query)
	sqlite_con.commit()


def sqlite_insert(sqlite_con, columns_list):
	"""
		function adds new row in table
		columns_list = [company, brand, model, price]
	"""
	cursor = sqlite_con.cursor()
	cursor.execute("INSERT INTO carSale VALUES(?,?,?,?)", columns_list)
	sqlite_con.commit()


def sqlite_update(sqlite_con, row_id, new_price):
	"""
		function updates row`s price
	"""
	cursor = sqlite_con.cursor()
	query = f"UPDATE carSale SET price = {new_price} WHERE ROWID={row_id}"
	cursor.execute(query)
	sqlite_con.commit()


def sqlite_delete_by_id(sqlite_con, row_id):
	"""
		function deletes row in table by id
	"""
	cursor = sqlite_con.cursor()
	query = f" DELETE FROM carSale WHERE ROWID == {row_id}"
	cursor.execute(query)
	sqlite_con.commit()
	cursor.execute('VACUUM')  # resets ROWID in table after deleting row


def sqlite_select(sqlite_con):
	"""
		function returns rows of table in list
	"""
	cursor = sqlite_con.cursor()
	query = f"SELECT * FROM carSale"
	cursor.execute(query)
	sqlite_con.commit()
	sqlite_row_list = []
	for row in cursor:
		sqlite_row_list.append(row)
	return sqlite_row_list