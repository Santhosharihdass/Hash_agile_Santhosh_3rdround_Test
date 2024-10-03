from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

response = es.search(index='employees', body={
    "query": {
        "match_all": {}
    }
})

for hit in response['hits']['hits']:
    print(hit['_source'])
