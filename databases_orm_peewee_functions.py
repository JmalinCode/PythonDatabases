from models import *


def db_table_create(db_con):
	"""
		function creates new table
	"""
	print("db_con", db_con)
	db_con.create_tables([CarSale])


def sqlite_insert(columns_list):
	"""
		function adds new row in table
		columns_list = [company, brand, model, price]
	"""
	CarSale(
		company=columns_list[0],
		brand=columns_list[1],
		model=columns_list[2],
		price=int(columns_list[3])
	).save()


def sqlite_update(row_id, new_price):
	"""
		function updates row`s price
	"""
	CarSale(
		rowid=row_id,
		price=int(new_price)
	).save()


def sqlite_delete_by_id(row_id):
	"""
		function deletes row in table by id
	"""
	try:
		CarSale.get(CarSale.rowid == row_id).delete_instance()
	except DoesNotExist:
		print(f'cant delete row with id = {row_id}')


def db_select():
	"""
		function returns rows of table in list
	"""
	query = CarSale.select()
	return [[i.rowid, i.company, i.brand, i.model, i.price] for i in query]


def psql_export_select():
	"""
		function returns rows of table in list with extra condition
	"""
	query = CarSale.select().where(CarSale.price <= 1500)
	return [[i.rowid, i.company, i.brand, i.model, i.price] for i in query]


def db_export_insert(columns_list):
	"""
		function adds new row in table
		columns_list = [rowid, company, brand, model, price]
	"""
	CarSale.create(
		rowid=int(columns_list[0]),
		company=columns_list[1],
		brand=columns_list[2],
		model=columns_list[3],
		price=int(columns_list[4])
	)
