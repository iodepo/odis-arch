import sys
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
from urllib.parse import urlparse
import pyoxigraph
from pyld import jsonld
import io
import pandas as pd


# test with https://edmo.seadatanet.org/sitemap.xml
# python3 cat2config.py https://edmo.seadatanet.org/sitemap.xml
def extract_value(cell):
    if isinstance(cell, (pyoxigraph.Literal, pyoxigraph.NamedNode, pyoxigraph.BlankNode)):
        return cell.value
    return cell

def parse_sitemap(sitemap_url):
    try:
        # Fetch the sitemap
        response = requests.get(sitemap_url)
        response.raise_for_status()

        # Parse the XML
        root = ET.fromstring(response.content)

        # Handle potential XML namespaces
        namespace = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else ''

        # Extract URLs based on whether there's a namespace or not
        if namespace:
            urls = [url.find('ns:loc', namespace).text for url in root.findall('.//ns:url', namespace)]
        else:
            urls = [url.find('loc').text for url in root.findall('.//url')]

        return urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

def extract_jsonld(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all script tags with type application/ld+json
        jsonld_scripts = soup.find_all('script', type='application/ld+json')

        if jsonld_scripts:
            # Return the content of the first JSON-LD script found
            try:
                # Attempt to parse and pretty-print the JSON
                jsonld_data = json.loads(jsonld_scripts[0].string)
                return json.dumps(jsonld_data, indent=2)
            except json.JSONDecodeError:
                # Return raw content if JSON parsing fails
                return jsonld_scripts[0].string

        return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def main():

    # set up oxygraph
    store = pyoxigraph.Store()  # store = pyoxigraph.Store(path="./store")
    mime_type = "application/n-triples"

    if len(sys.argv) != 2:
        print("Usage: python script.py <sitemap_url>")
        sys.exit(1)

    sitemap_url = sys.argv[1]

    # Validate URL format
    try:
        result = urlparse(sitemap_url)
        if not all([result.scheme, result.netloc]):
            raise ValueError("Invalid URL format")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Parse sitemap
    print(f"Parsing sitemap: {sitemap_url}")
    urls = parse_sitemap(sitemap_url)

    if not urls:
        print("No URLs found in sitemap")
        sys.exit(1)

    print(f"Found {len(urls)} URLs in sitemap")

    # Process each URL
    for url in urls[1:10]:
        print(f"\nChecking {url} for JSON-LD data...")
        jsonld_content = extract_jsonld(url)

        if jsonld_content:
            print("Found JSON-LD content:")
            print(jsonld_content)
            normalized = jsonld.normalize(json.loads(jsonld_content), {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
            x = store.load(io.StringIO(normalized), mime_type, base_iri=None, to_graph=None)
            print(x)
        else:
            print("No JSON-LD content found")

    sparql = """
    PREFIX shacl: <http://www.w3.org/ns/shacl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>

SELECT ?url ?name
WHERE {
?s schema:name ?name .
?s schema:url ?url .
}

"""
    r = store.query(sparql)
    q1 = list(r)
    print(q1)

    vars = r.variables
    value_list = [variable.value for variable in vars]

    df = pd.DataFrame(q1, columns=value_list)
    df = df.applymap(extract_value)

    print(df.head())

if __name__ == "__main__":
    main()


