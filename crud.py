from pymongo import MongoClient


# CRUD
def create(lst_car_set):
    return mytb.insert_many(lst_car_set)


def update(before, after):
    return mytb.update_one(before, after)


def read(record):
    return mytb.find(record)


def delete(record):
    return mytb.delete_one(record)


def print_result():
    return print(list(mydb.mytb.find({})))


# DB records
tavria = {"rowid": 1, "manufacter": "ZAZ", 
          "power": "73", "max_speed": "140"}
lacetti = {"rowid": 2, "manufacter": "Chevrolet", 
           "power": "122", "max_speed": "180"}
logan = {"rowid": 3, "manufacter": "Renault", 
         "power": "90", "max_speed": "160"}

#Create client and insert records in db
client = MongoClient()


mydb = client.car_database
mytb = mydb.cars
create([tavria, lacetti, logan])
