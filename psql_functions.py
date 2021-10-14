import psycopg2
from psycopg2 import Error



def psql_connection(database_name):
	"""
		function connects to database
	"""
	try:
		psql_con = psycopg2.connect(f"db/{database_name}.db")
		return psql_con
	except Error:
		print(Error)


def psql_table_create(psql_con):
	"""
		function creates new table
	"""
	cursor = psql_con.cursor()
	query = """ CREATE TABLE IF NOT EXISTS carSale(
		company VARCHAR(255) NOT NULL,
		brand VARCHAR(255) NOT NULL, 
		model VARCHAR(255) NOT NULL, 
		price INT )"""
	cursor.execute(query)
	psql_con.commit()


def psql_insert(psql_con, columns_list):
	"""
		function adds new row in table
		columns_list = [company, brand, model, price]
	"""
	cursor = psql_con.cursor()
	cursor.execute("INSERT INTO carSale VALUES (%s,%s,%s,%s)", columns_list)
	psql_con.commit()


def psql_update(psql_con, row_id, new_price):
	"""
		function updates row`s price
	"""
	cursor = psql_con.cursor()
	query = f"UPDATE carSale SET price = {new_price} WHERE ROWID={row_id}"
	cursor.execute(query)
	psql_con.commit()


def psql_delete_by_id(psql_con, row_id):
	"""
		function deletes row in table by id
	"""
	cursor = psql_con.cursor()
	query = f" DELETE FROM carSale WHERE ROWID == {row_id}"
	cursor.execute(query)
	psql_con.commit()
	cursor.execute('REINDEX TABLE carSale;')  # resets ROWID in table after deleting row


def psql_select(psql_con):
	"""
		function returns rows of table in list
	"""
	cursor = psql_con.cursor()
	query = f"SELECT * FROM carSale"
	cursor.execute(query)
	psql_con.commit()
	psql_row_list = []
	for row in cursor:
		psql_row_list.append(row)
	return psql_row_list
