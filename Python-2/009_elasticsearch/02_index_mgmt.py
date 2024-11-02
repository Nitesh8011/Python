from elasticsearch import Elasticsearch

config = {
    "ES_USER": "admin",
    "ES_PASS": "admin"
}

es = Elasticsearch(
    cloud_id='id',
    basic_auth=(config["ES_USER"],config["ES_PASS"]),
    request_timeout=60
)

# Create Index
es.indices.create(index='test-index')

if es.indices.exits(index='test-index'):
    print("Index Exits")
else:
    print("Index doesn't exits")


# Delete Index
es.indices.delete(index='test-index')

if es.indices.exists(index='test-index'):
    print("Index Deleted")
else:
    print("Index doesn't exits")