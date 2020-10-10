# install python mongo client pymongo using pip
# $ pip install pymongo

def get_data():
    from os       import getcwd, path
    from json     import load, dump
    from requests import get
    _file = path.join(getcwd(), 'data.json')
    if path.exists(_file):
        with open(_file, 'r') as f:
            json_object = load(f)
            return json_object
    else:
        response = get('https://jsonplaceholder.typicode.com/posts')
        with open(_file, 'w') as f:
            dump(response.json(), f)
        return response.json()

from pymongo import MongoClient
"""
Making a connection with MongoClient

# DEFAULT connection
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('localhost', 27017)
"""
# client = MongoClient() # OR
# client = MongoClient('mongodb://localhost:27017/') # OR
client = MongoClient('localhost', 27017)

# listing all the available databases
# print(client.list_database_names())

"""
In mongodb, you can't create database until and unless, you have content.
Collections in mongodb are like tables in the SQL
"""
# creating the database and collection
my_database   = client['my_database']
my_collection = my_database['posts']

# inserting data in our collection
my_collection.insert_many(get_data())
my_record = my_collection.insert_one({
    "id": 101,
    "title": "the importance of hello",
    "body": "the world beyond hello",
})
print(f"Inserted document id: {my_record.inserted_id}")

"""
finding in collection/table
"""
record = my_collection.find_one()
# print(f"Single occurrence: {record}") # it will just return the 1st object

records = my_collection.find()
print(f"All occurrences: {records}") # return all the records

myquery = {"title": "qui est esse"}
records = my_collection.find(myquery)
for _record in records:
    print(_record)

print()
myquery = {"title": {"$regex": "^ea"}}
records = my_collection.find(myquery)
for _record in records:
    print(_record)

"""
arranging database
"""
# sorting in ascending order
records = my_collection.find().sort('title', 1)
for _record in records[:10]:
    print(_record.get('title'))
print()

# sorting in descending order
records = my_collection.find().sort('title', -1).limit(10)
for _record in records[:10]:
    print(_record.get('title'))
print()


"""
delete operations
"""
myquery = {'title': 'sed ab est est'}
# delete one record
r = my_collection.delete_one(myquery)
print(f"RAW result: {r.raw_result}")
print(f"DELETE count: {r.deleted_count}")

# delete many records
myquery = {'title': {'$regex': "^qui"}}
r = my_collection.delete_many(myquery)
print(f"RAW result: {r.raw_result}")
print(f"DELETE count: {r.deleted_count}")


"""
updating records
"""
# updating single record
myquery = {'title': 'the importance of hello'}
newvalue = {'$set': {'title': 'hello there bro...'}}
r = my_collection.update_one(myquery, newvalue)
print(f"UPDATE (one): {r.raw_result} | {r.upserted_id}")

# updating multiple record
myquery = {'title': {'$regex': '^o'}}
newvalue = {'$set': {'title': 'Ooooooaoaaaaa....'}}
r = my_collection.update_many(myquery, newvalue)
print(f"UPDATE (many): {r.raw_result} | {r.upserted_id}")


"""
droppig database and collection
"""
my_collection.drop()
client.drop_database('posts')
print(f'Available db: {client.list_database_names()}')
