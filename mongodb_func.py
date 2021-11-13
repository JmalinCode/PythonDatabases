from pymongo import MongoClient


def rowid_find_func(collection):
    select = mongodb_table_select(collection)
    row_id = 1
    for row in select:
        if row[0] >= row_id:
            row_id = row[0] + 1
        print(row_id)
    return row_id


def mongodb_insert(collection, columns_set):
    rowid = rowid_find_func(collection)
    collection.insert_one({'_id': rowid, **columns_set})


def mongodb_update(collection, rowid, new_price):
    collection.update_one({'_id': rowid}, {'$set': {'price': new_price}})


def mongodb_table_select(collection):
    rows = collection.find()
    return [list(row.values()) for row in list(rows)]


def mongodb_delete_by_id(collection, rowid):
    collection.delete_one({'_id': rowid})


def print_json(collection):
    rows = collection.find()
    print('{')
    for row in rows:
        print(row)
    print('}\n')


if __name__ == '__main__':
    # How to use
    cluster = MongoClient(
        "mongodb+srv://newuser:Password32123@cluster1.rtnha.mongodb.net/testdb?retryWrites=true&w=majority")
    mongodb_con = cluster.testdb
    collection = mongodb_con.test

    new_obj = {'company': 'KievCars1', 'brand': 'new', 'model': 'old', 'price': 69}
    # insert
    mongodb_insert(collection, new_obj)
    # update
    mongodb_update(collection, 1, 96)
    # delete
    mongodb_delete_by_id(collection, 2)
    # select
    mongodb_table_select(collection)


