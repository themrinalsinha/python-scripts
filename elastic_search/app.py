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
es.indices.delete('cities')


# ============ different search query for matching document ============
# sample document
doc_1 = {"sentence": "Today is a sunny day"}
doc_2 = {"sentence": "Today is a bright-sunny day"}
doc_3 = {"sentence": "Tomorrow is day after today"}
doc_4 = {"sentence": "Bored AF"}

# inserting records
es.index(index="english", id=1, body=doc_1)
es.index(index="english", id=2, body=doc_2)
es.index(index="english", id=3, body=doc_3)
es.index(index="english", id=4, body=doc_4)

# search query
result = es.search(index="english", body={"from": 0, "size": 0, "query": {"match": {"sentence": "SUNNY"}}})
print(f"\nRESULT (1): {result}")

result = es.search(index="english", body={"from": 0, "size": 2, "query": {"match": {"sentence": "SUNNY"}}})
print(f"\nRESULT (2): {result}")

# match query
result = es.search(index="english", body={"from": 0, "size": 0, "query": {"match_phrase": {"sentence": "bright sunny"}}})
print(f"\nSearch using match_phrase: {result}")

result = es.search(index="english", body={"from": 0, "size": 1, "query": {"match_phrase": {"sentence": "bright sunny"}}})
print(f"\nSearch using match_phrase: {result}")

# using term query when you want to match the exact value
result = es.search(index="english", body={"from": 0, "size": 0, "query": {"term": {"sentence": "Bored AF"}}})
print(f"\nResult (term search): {result}")

result = es.search(index="english", body={"from": 0, "size": 1, "query": {"term": {"sentence": "Bored AF"}}})
print(f"\nResult (term search): {result}")
es.indices.delete("english")


# =========== (combining queries) - must / must_not / should ===========
print()
doc_1 = {"sentence": "Today is a sunny day"}
doc_2 = {"sentence": "Today is a bright-sunny day"}
doc_3 = {"sentence": "Tomorrow is day after today"}
doc_4 = {"sentence": "Bored AF"}

es.index(index="newindex", id=1, body=doc_1)
es.index(index="newindex", id=2, body=doc_2)
es.index(index="newindex", id=3, body=doc_3)
es.index(index="newindex", id=4, body=doc_4)

result = es.search(
    index = "newindex",
    body = {
        "from": 0,
        "size": 1,
        "query": {
            "bool": {
                "must_not": {
                    "match": {"sentence": "bright"}
                },
                "should": {
                    "match": {"sentence": "sunny"}
                }
            }
        }
    }
)

print(f"\nCombined query: {result}")

# =========== using regular expression on search ============
# regular expression to match everything
result = es.search(index="newindex", body={"query": {"regexp": {"sentence": ".*"}}})
print(f"\nREGULAR EXPRESSION (Search): {result}")

# match those with "sun" as subset
result = es.search(index="newindex", body={"query": {"regexp": {"sentence": "sun.*"}}})
print(f"\nRE (sun as subset): {result}")
es.indices.delete("newindex")

# ====================================================================================
es.indices.delete("travel")
es.indices
"""
MAPPING
----------------------------------------------------------------------------------
As per Elasticsearch Reference, "Mapping is the process of defining how a document,
and the fields it contains, are stored and indexed.

It enables in faster search retrieval and aggregations. Hence, your mapping defines
how effectively you can handle you data. A bad mapping can have severe consequences
on the performance of your system.
"""

data = [
    {"city": "Banglore", "country": "India", "datetime": "2018,01,01,10,20,00"}, # YYYY,MM,dd,hh,mm,ss
    {"city": "London", "country": "England", "datetime": "2020,01,02,10,20,10"},
    {"city": "Washington", "country": "USA", "datetime": "2019,01,01,10,20,00"},
    {"city": "Canberra", "country": "Australia", "datetime": "2018,02,01,11,20,00"},
]

for index, record in enumerate(data, start=1):
    es.index(index="travel", id=index, body=record)

# to get the existing mapping that the es built for us
_mapping = es.indices.get_mapping(index="travel")
print(f"\nMAPPING (in-built)\n{_mapping}")
"""
Example:
{'travel': {'mappings': {'properties':
    {'city': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
     'country': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}},
     'datetime': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'ignore_above': 256}}}}}}}

NOTE: here you can see that the datetime field is not considered as mapping,
      rather it is taken as a string (in default mapping), so in order to handle
      such scenarios, we need to create our own custom mapping.
"""
# to create your own custom mapping
es.indices.put_mapping(
    index = "travel",
    body = {
        "properties": {
            "city": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "country": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "datetime": {
                "type": "date",
                "format": "yyyy,MM,dd,hh,mm,ss"
            }
        }
    }
)
# es.indices.delete(index="travel")
# es.indices.create(index="travel")

# inserting data again
# for index, record in enumerate(data, start=1):
#     es.index(index="travel", id=index, body=record)
