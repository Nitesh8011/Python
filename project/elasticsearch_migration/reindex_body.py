import reindex

def reindex_data(reindex_index):
    try:
        reindex_body = {
            "source": {
                "remote": {
                    "host": reindex.source_es    
                },
                "index": reindex_index,
                "query": { 
                    "match_all": {}
                }
            },
            "dest": {
                "index": reindex_index
            }
        }

        response = reindex.destination_es.reindex(body=reindex_body, wait_for_completion=True)
        print("Reindexing response:", response)

    except Exception as e:
        print(f"Failed to reindex: ", {e})