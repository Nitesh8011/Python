from elasticsearch import Elasticsearch

config = {
    "ES_USER" : "admin",
    "ES_PASS": "admin"
}

es = Elasticsearch(
    cloud_id="id",
    basic_auth=(config["ES_USER"], config["ES_PASS"]),
    request_timeout=60
)

example_doc = {
    "title": 'Example Document',
    "content": "Content of an example document."
}

es.indices.create(index='test-index2')

if es.indices.exists(index='test-index2'):
    print("Index Exits")
    es.index(index='test-index2', id=1, document=example_doc)
else:
    print("index doesn't exits")