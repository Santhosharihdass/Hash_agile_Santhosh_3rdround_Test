import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

df = pd.read_csv('/home/ubunut/Employee Sample Data 1.csv', encoding='latin1') 

if es.indices.exists(index='employees'):
    es.indices.delete(index='employees')

es.indices.create(index='employees')

for i, row in df.iterrows():
    doc = row.to_dict()
    try:
        es.index(index='employees', body=doc)
    except Exception as e:
        print(f"Error indexing document {i}: {e}")

print("Employee data indexed successfully.")
