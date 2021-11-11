from pymongo import MongoClient



tavria = {"power": "73", "max_speed": "140", "weight": "800", "engine_volume": "1.2"}
lacetti = {"power": "122", "max_speed": "180", "weight": "1665", "engine_volume": "1.8"}
logan = {"power": "90", "max_speed": "160", "weight": "1545", "engine_volume": "1.6"}

client = MongoClient()
col = client.mydb.test

def create(lst):
    result = col.insert_many(lst)


def update(before, after):
    result = col.update_one(before, after)


def read(record):
    result = col.find(record)


def delete(record):
    result = col.delete_one(record)
