
import pymongo
from conf import *

client = pymongo.MongoClient(host = db_host, port = db_port)
db = client[db_name]
phone_coll = db[phone_coll_name]
estatle_coll = db[estatle_coll_name]
room_coll = db[room_coll_name]
rent_rooms_coll = db[rent_rooms_coll_name]

def insert_phone(phone):
    phone_coll.insert({'phone': phone})
    return True



def search_estatle(eid, etitle, page_num, page_size):
    res = estatle_coll.find({'estatleId': eid, 'estatleTitle': etitle}).skip(page_num * page_size).limit(page_size)
    return list(res)


def search_root(rid):
    return room_coll.find_one({'roomID': rid})


def search_rentRooms(city, cityCircle, page_num, page_size):
    res = rent_rooms_coll.find({'city': city, 'cityCircle': cityCircle}).skip(page_num * page_size).limit(page_size)
    return list(res)
    
