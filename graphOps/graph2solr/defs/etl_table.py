import json
import sys
from pathlib import Path

import requests


def table_mode(source, sink):
    """Handle table mode operations"""
    print(f"Table mode: Processing data from {source} to {sink}")
    # Add table-specific logic here


    if not Path(source).is_file():
        sys.exit(f"Error: File {source} does not exist.")

    counter = 0
    with open(source, 'r') as f:
        for line in f:
            counter += 1
            try:
                # Create Solr update document
                doc = json.loads(line)
                solr_doc = {"add": {"doc": doc}}

                # Send to Solr
                print(f"Processing line {counter}...")
                response = requests.post(
                    sink,
                    json=solr_doc,
                    headers={"Content-Type": "application/json"}
                )
                response.raise_for_status()
                print(f"Line {counter} uploaded successfully.")

            except Exception as e:
                print(f"Error uploading line {counter}: {str(e)}")

    print(f"Finished processing {counter} lines from {source}")
