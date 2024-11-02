from elasticsearch import Elasticsearch

config = {
    "ES_USER": "admin",
    "ES_PASS": "admin"
}

es = Elasticsearch(
    cloud_id = "id",
    basic_auth =(config["ES_USER"],config["ES_PASS"]),
    request_timeout=60
)

if es.ping():
    print("Connected to Elasticsearch.")
else:
    print("Failed to connect to Elasticsearch.")