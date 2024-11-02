from elasticsearch import Elasticsearch
import re

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

if es.ping():
    print("Connected to Elasticsearch")

    try:
        all_indices = es.indices.get_alias(name="*")
        
        print("All indices:")
        for index in all_indices.keys():
            print(index)

        # Define the pattern to filter indices
        pattern = 'masterdataonline'
        filter_indices = [index for index in all_indices if re.search(pattern, index)]

        print("\nFiltered indices:")
        with open('all_indices.txt', 'a') as file:  # Open file in append mode
            for index in filter_indices:
                file.write(f"{index}\n")

        # Check and delete empty indices
        for index_name in filter_indices:
            try:
                # Get the document count
                response = es.count(index=index_name)
                doc_count = response['count']  # Extract the count from the response
                print(f"{index_name} contains {doc_count} documents")

                # Delete the index if document count is 0
                if doc_count == 0:
                    es.indices.delete(index=index_name)  # Delete the index
                    print('Deleted Index:', index_name)

                    # Log the deleted index
                    with open('deleted_indices.txt', 'a') as log_file:
                        log_file.write(f"{index_name}\n")

            except Exception as e:
                print(f'Error processing index "{index_name}": {e}')

    except Exception as e:
        print(f"Error fetching indices: {e}")

else:
    print("Failed to connect to Elasticsearch")
