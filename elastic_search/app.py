from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://localhost", port="9200")
# es = Elasticsearch() # localhost:9200 by default
# es = Elasticsearch("http://localhost:9200")


# ============ Creating / Deleting / Checking Indexes ============
# creating an index
first_index = es.indices.create(index="first_index", ignore=400)
print(f"\nFirst Index (acknowledgment): {first_index}")

# to check if index exists
first_index_status = es.indices.exists(index="first_index")
print(f"\nCheck if 'first_index' exists: {first_index_status}")

# to delete an index
delete_ack = es.indices.delete(index="first_index")
print(f"\nDelete index (acknowledgment): {delete_ack}")

# ============ Insert / Get Query ============
# sample document
es.indices.delete('cities')

doc_1 = {"city": "New Delhi", "country": "India"}
doc_2 = {"city": "London", "country": "England"}
doc_3 = {"city": "Los Angeles", "country": "USA"}
doc_4 = {"city": "Maxico City", "country": "Maxico"}

# Now we'll create index and add the document to it.
_inserted = es.index(index="cities", id=1, body=doc_1)
print(f"\nInserted doc - 1: {_inserted}")

_inserted = es.index(index="cities", id=2, body=doc_2)
print(f"\nInserted doc - 2: {_inserted}")

_inserted = es.index(index="cities", id=3, body=doc_3)
print(f"\nInserted doc - 3: {_inserted}")

_inserted = es.index(index="cities", id=4, body=doc_4)
print(f"\nInserted doc - 4: {_inserted}")

# Now let's say we want to get and check the data present for id=2
result = es.get(index="cities", id=2)
print(f"\nResult for ID-2 is: {result}")
print(f"DATA for ID-2: {result['_source']}")
