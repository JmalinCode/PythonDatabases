from peewee import *

sqlite_db = SqliteDatabase(f'db/test.db')


class CarSale(Model):
	rowid = PrimaryKeyField(unique=True)
	company = CharField()
	brand = CharField()
	model = CharField()
	price = IntegerField()

	class Meta:
		order_by = id
		database = sqlite_db
