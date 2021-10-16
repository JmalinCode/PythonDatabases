import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def psql_connection():
	psql_con = None
	try:
		psql_con = psycopg2.connect(database="postgres", user="postgres", password="Password32123", host="127.0.0.1", port="5432")
		psql_con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	except (Exception, Error) as e:
		print(e)
	return psql_con


def psql_database_create(psql_con):
	psql_con.autocommit = True
	cursor = psql_con.cursor()
	try:
		cursor.execute("CREATE DATABASE psql_db;")
		print("Query executed successfully")
	except (Exception, Error) as e:
		print(e)


def psql_table_create(psql_con):
	psql_con.autocommit = True
	cursor = psql_con.cursor()
	try:
		query = """DROP TABLE IF EXISTS carsale;
		CREATE TABLE if not exists carsale(
		company TEXT,
		brand TEXT, 
		model TEXT, 
		price INTEGER);"""
		cursor.execute(query)
		print("Query executed successfully")
	except (Exception, Error) as e:
		print(e)


def psql_insert(psql_con, columns_list):
	"""
		function adds new row in table
		columns_list = [company, brand, model, price]
	"""
	psql_con.autocommit = True
	cursor = psql_con.cursor()
	cursor.execute("INSERT INTO carsale VALUES (%s,%s,%s,%s);", columns_list)


def psql_select(psql_con):
	"""
		function returns rows of table in list
	"""
	psql_con.autocommit = True
	cursor = psql_con.cursor()
	query = f"SELECT * FROM carsale;"
	cursor.execute(query)
	psql_row_list = []
	for row in cursor:
		psql_row_list.append(row)
		# print("row", row)
	return psql_row_list


def psql_export_select(psql_con):
	psql_con.autocommit = True
	cursor = psql_con.cursor()
	query = f"SELECT * FROM carsale WHERE price < 5000;"
	cursor.execute(query)
	psql_row_list = []
	for row in cursor:
		psql_row_list.append(row)
	# print("row", row)
	print(psql_row_list)
	return psql_row_list
