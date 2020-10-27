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


