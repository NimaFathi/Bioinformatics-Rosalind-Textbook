from pymongo import MongoClient
from bson.son import SON
import pprint
import rocksdb
import os
client = MongoClient("mongodb://nima.fathi:aRZM1qeDrZB46ZV7Q77tTDcbUaRJlIUgz8JesFPicF@217.182.141.19:27017/analytics-db")
db = client["analytics-db"]
col1 = db.events
'''
query = col1.find({"domain": "sheypoor.com"}).limit(100)
for q in query:
    print(q)'''
col2 = db.products
query = col2.find({"advertiser_id":})