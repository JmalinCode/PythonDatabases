import sqlite3
from sqlite3 import Error


def sqlite_connection(database_name):
	"""
		function connects to sqlite database
	"""
	try:
		sqlite_db = sqlite3.connect(f"db/{database_name}.db")
		return sqlite_db
	except Error:
		print(Error)


def sqlite_table_create(sqlite_db):
	"""
		function creates new table
	"""
	cursor = sqlite_db.cursor()
	query = """ CREATE TABLE IF NOT EXISTS carSale(
		company TEXT,
		brand TEXT, 
		model TEXT, 
		price REAL )"""
	cursor.execute(query)
	sqlite_db.commit()


def sqlite_insert(sqlite_db, company, brand, model, price):
	"""
		function adds new row in table
	"""
	cursor = sqlite_db.cursor()
	cursor.execute("INSERT INTO carSale VALUES(?,?,?,?)", [company, brand, model, price])
	sqlite_db.commit()


def sqlite_update(sqlite_db, row_id, new_price):
	"""
		function updates car price
	"""
	cursor = sqlite_db.cursor()
	query = f"UPDATE carSale SET price = {new_price} WHERE ROWID={row_id}"
	cursor.execute(query)
	sqlite_db.commit()


def sqlite_delete_by_id(sqlite_db, row_id):
	"""
		function deletes row in table by id
	"""
	cursor = sqlite_db.cursor()
	query = f" DELETE FROM carSale WHERE ROWID == {row_id}"
	cursor.execute(query)
	sqlite_db.commit()


def sqlite_select(sqlite_db):
	"""
		function returns rows of table in list
	"""
	cursor = sqlite_db.cursor()
	query = f"SELECT ROWID, * FROM carSale"
	cursor.execute(query)
	sqlite_db.commit()
	return cursor
