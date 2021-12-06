

def insert(session, table_class, columns_set):
	new_row = table_class(**columns_set)
	session.add(new_row)
	session.commit()


def update(session, table_class, rowid, new_price):
	update_row = session.query(table_class).filter(table_class.row_id == rowid)
	update_row[0].price = new_price
	session.add(update_row[0])
	session.commit()


def delete_by_id(session, table_class, rowid):
	session.query(table_class).filter(table_class.row_id == rowid).delete()


def table_select(session, table_cl):
	res = []
	for row_id, c, b, m, p in session.query(table_cl.row_id,
	                                        table_cl.company,
	                                        table_cl.brand,
	                                        table_cl.model,
	                                        table_cl.price, ):
		res.append([row_id, c, b, m, p])
	return res


def dict_select(session, table_cl):
	res = []
	for row_id, c, b, m, p in session.query(table_cl.row_id,
	                                        table_cl.company,
	                                        table_cl.brand,
	                                        table_cl.model,
	                                        table_cl.price, ):
		res.append({'row_id': row_id, 'company': c, 'brand': b, 'model': m, 'price': p})
	return res


def print_json(select_list):
	print('{')
	for row in select_list:
		print('   {', end=' ')
		for item in row:
			print(item, end=', ')
		print('},')
	print('}\n')

