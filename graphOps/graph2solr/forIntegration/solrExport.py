import requests
import json
import argparse
from urllib.parse import urljoin

# http://localhost:8983/solr/your_core/select?q=*:*&wt=json&rows=1000000

def export_solr_to_json(solr_url, rows, output_file):
    # Construct the full URL for the Solr request
    params = {
        'q': '*:*',
        'wt': 'json',
        'rows': rows
    }
    url = urljoin(solr_url, 'select')

    try:
        # Send GET request to Solr
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the JSON response
        data = response.json()

        # Write the response to a file
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Successfully exported {len(data['response']['docs'])} documents to {output_file}")

    except requests.RequestException as e:
        print(f"Error occurred while making the request: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response from Solr")
    except IOError:
        print(f"Error writing to file: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Solr data to JSON file.")
    parser.add_argument("solr_url", help="Base URL of the Solr server (e.g., http://localhost:8983/solr/your_core/)")
    parser.add_argument("rows", type=int, help="Number of rows to export")
    parser.add_argument("output_file", help="Name of the output JSON file")

    args = parser.parse_args()

    export_solr_to_json(args.solr_url, args.rows, args.output_file)


