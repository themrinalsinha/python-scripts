# pip install pymongo

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())
