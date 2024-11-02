from elasticsearch import Elasticsearch
import re
import reindex_body as rb

source_es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
destination_es = Elasticsearch([{'host': 'localhost', 'port': 9201, 'scheme': 'http'}])


try:
    if source_es.ping():
        print("Connected with elastic cluster")

    try:
        all_indices = source_es.index.get_alias(name='*')

        print("All indices:")
        for index in all_indices:
            print(f"{index}\n")

        pattern = 'masterdataonline'
        filter_indices = [
            index for index in all_indices
            if re.search(pattern, index)
        ]

        print("\nFiltered indices:")
        with open('all_index.txt','a') as file:
            file.write(f"{index}\n")

        for index_name in filter_indices:
            try:
                rb.reindex_data(index_name)
                
            except Exception as e:
                print(f"Failed to reindex: ",{e})

    except Exception as e:
        print("error w",{e})

except Exception as e:
    print("Failed to connect with cluster", {e})