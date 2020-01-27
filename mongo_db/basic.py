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
# mycollection.insert_many(data)
print(client.list_database_names())

# for finding in collection
res = mycollection.find_one()  # it finds and returns the first occurence/instance.
print(res)
res = mycollection.find()      # it returns the entire record which is feeded into the database
for rec in res:
    print(rec)

# custom query
query = {"name": "John"}           # normal query
query = {"name": {"$regex": "^D"}} # query search using regex - name starting with D

for rec in mycollection.find(query):
    print(rec)


# sorting data
for rec in mycollection.find().sort('name', 1): # sorting in ascending order
    print("ASCENDING: ", rec)

for rec in mycollection.find().sort('name', -1): # sorting in descending order
    print("DESCENDING: ", rec)

# deleting operations
query = {"name": "Mrinal Sinha"}
mycollection.delete_many(query)
for rec in mycollection.find():
    print(rec)

# update operations
query = {"name": {"$regex": "^Dha"}}
new_values = {"$set": {"name": "Dhwani", "email": "dhwani@________.com"}}
mycollection.update_many(query, new_values)
