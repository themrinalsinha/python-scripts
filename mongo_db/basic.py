from pymongo import MongoClient

client = MongoClient()
mydb = client['mydemodb']
mycollection = mydb['mydemotable']

# sample dataset
data = [
    {"id": 1, "name": "Mrinal Sinha", "email": "mrinal@advarisk.com"},
    {"id": 2, "name": "Dhawal Bhai", "email": "dhawal@advarisk.com"},
    {"id": 3, "name": "Manish Chandak", "email": "manish@advarisk.com"},
    {"id": 4, "name": "Santhosh Soloman", "email": "santhosh@advarisk.com"},
]

# inserting multiple records at once.
mycollection.insert_many(data)
print(client.list_database_names())

# for finding in collection
res = mycollection.find_one()  # it finds and returns the first occurence/instance.
print(res)
res = mycollection.find()      # it returns the entire record which is feeded into the database
for rec in res:
    print(rec)
