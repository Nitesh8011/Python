from elasticsearch import Elasticsearch
import random

# Connect to Elasticsearch
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}]
)

num_indices = 10
num_doc_count = 3
base_index_name = 'dummy_masterdataonline_'
base_alias_name = 'alias_'

for i in range(num_indices):
    index_name = f"{base_index_name}{i + 1}"
    alias_name = f"{base_alias_name}{i + 1}"  # Create a different alias name
    try:
        # Create the index
        es.indices.create(index=index_name, ignore=400)
        print(f'Index {index_name} created successfully.')

        # Create the alias
        es.indices.put_alias(index=index_name, name=alias_name)
        print(f'Alias {alias_name} created for index {index_name}.')

        # Add documents to the index
        for j in range(num_doc_count):
            doc = {
                'title': f'Document {j + 1} for {index_name}',
                'content': f'This is some content for document {j + 1}.',
                'number': random.randint(1, 100)  # Random number for variation
            }
            es.index(index=index_name, body=doc)  # Add the document to the index

        print(f'Added {num_doc_count} documents to {index_name}.')

    except Exception as e:
        print(f'Failed to create index "{index_name}": {e}')
