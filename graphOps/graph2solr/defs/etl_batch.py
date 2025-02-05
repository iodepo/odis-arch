import json
from pysolr import Solr
import json

from pysolr import Solr


def batch_mode(source, sink, batch_size=1000, commit_within=1000):
    """
    Loads a JSONL file into Solr using the batch API.

    Args:
    solr_url: The URL of your Solr server (e.g., 'http://localhost:8983/solr/my_core').
    jsonl_file: The path to the JSONL file.
    batch_size: The number of documents to send in each batch.
    commit_within: The maximum time in milliseconds before a commit is performed.

    Returns:
    None
    """
    print(f"Batch mode: Processing data from {source} to {sink}")


    solr = Solr(sink)
    docs = []

    with open(source, 'r') as f:
        for line in f:
            doc = json.loads(line)
            docs.append(doc)

            if len(docs) >= batch_size:
                try:
                    solr.add(docs, commitWithin=commit_within)
                    docs = []
                except Exception as e:
                  print(f"Error during bulk insert: {e}")
                  raise

    if docs:  # Add any remaining documents
        try:
            solr.add(docs, commitWithin=commit_within)
        except Exception as e:
            print(f"Error during bulk insert: {e}")
            raise
