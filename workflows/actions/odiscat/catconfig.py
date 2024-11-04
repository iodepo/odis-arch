import sys
import httpx  # Replacing requests with httpx
import xml.etree.ElementTree as ET
import json
from urllib.parse import urlparse
import pyoxigraph
from pyld import jsonld
import io
import re
import pandas as pd
import extruct
from w3lib.html import get_base_url
import string
from tqdm import tqdm  # Importing tqdm for progress indication
from datetime import date
from typing import Optional, List
from pydantic import BaseModel, HttpUrl, Field
import yaml
from pathlib import Path


class Source(BaseModel):
    name: str = Field(description="Short identifier for the source")
    propername: str = Field(description="Full proper name of the catalogue")
    catalogue: Optional[str] = Field(description="URL of the catalogue")
    domain: Optional[str] = Field(description="Base domain URL")
    logo: Optional[str] = Field(description="URL of the source logo")
    pid: Optional[str] = Field(description="Persistent identifier URL")
    sourcetype: Optional[str] = Field(description="Type of the source (e.g., sitemap)")
    url: Optional[str] = Field(description="URL to the source data")
    changefreq: Optional[str] = Field(None, description="Change frequency")
    backend: Optional[str] = Field(None, description="Backend system type")
    headless: Optional[str] = Field(description="Whether the source is headless")
    dateadded: Optional[str] = Field(description="Date when the source was added")
    cron: Optional[str] = Field(description="Cron schedule expression")
    active: Optional[str] = Field(description="Whether the source is active")

class SourceConfig(BaseModel):
    sources: List[Source] = Field(description="List of source configurations")

prefix = """---
minio:
  address:
  port:
  accessKey:
  secretKey:
  ssl:
  bucket: oih
gleaner:
  runid: oih # this will be the bucket the output is placed in...
  summon: true # do we want to visit the web sites and pull down the files
  mill: false
context:
  cache: true
contextmaps:
- prefix: "https://schema.org/"
  file: "./assets/jsonldcontext.json"  # wget http://schema.org/docs/jsonldcontext.jsonld
- prefix: "http://schema.org/"
  file: "./assets/jsonldcontext.json"  # wget http://schema.org/docs/jsonldcontext.jsonld
summoner:
  after: ""      # "21 May 20 10:00 UTC"
  mode: full  # full || diff:  If diff compare what we have currently in gleaner to sitemap, get only new, delete missing
  threads: 5
  delay:  # milliseconds (1000 = 1 second) to delay between calls (will FORCE threads to 1)
  headless: http://0.0.0.0:9222  # URL for headless see docs/headless
millers:
  graph: false
"""

def remove_none_values(d):
    """Recursively remove keys with None values from dictionaries"""
    if not isinstance(d, dict):
        return d
    return {
        k: remove_none_values(v)
        for k, v in d.items()
        if v is not None and v != 'None'
    }

def extract_value(cell):
    if isinstance(cell, (pyoxigraph.Literal, pyoxigraph.NamedNode, pyoxigraph.BlankNode)):
        return cell.value
    return cell

def parse_sitemap(sitemap_url):
    try:
        # Fetch the sitemap
        response = httpx.get(sitemap_url)
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

    except httpx.RequestError as e:
        print(f"Error fetching sitemap: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

def trimit(input_str):
    # Define the control characters
    control_chars = ''.join(map(chr, range(0, 32))) + chr(127)

    # Create a translation table
    translation_table = str.maketrans('', '', control_chars + string.whitespace)

    # Translate the input string using the translation table
    result_str = input_str.translate(translation_table)

    return result_str

def extract_jsonld(url):
    try:
        # Fetch the webpage
        response = httpx.get(trimit(url))
        response.raise_for_status()

        # Get base URL for handling relative URLs in the HTML
        base_url = get_base_url(response.text, str(response.url))

        # Extract all metadata formats using extruct
        data = extruct.extract(
            response.text,
            base_url=base_url,
            syntaxes=['json-ld']  # Only extract JSON-LD
        )

        # Get JSON-LD data
        jsonld_data = data.get('json-ld', [])

        if jsonld_data:
            # If we found JSON-LD data, return the first item pretty-printed
            # print(json.dumps(jsonld_data[0], indent=2))
            # print("============================")
            return json.dumps(jsonld_data[0], indent=2)

        return None

    except httpx.RequestError as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def process_string(input_string: str) -> str:
    # Step 1: Lowercase the string
    lowercased_string = input_string.lower()
    # Step 2: Remove all spaces and non-alphabetic characters
    cleaned_string = re.sub(r'[^a-z]', '', lowercased_string)
    # Step 3: Return the first 8 characters
    return cleaned_string[:12]

def get_last_path_element(url: str) -> str:
    parsed_url = urlparse(url)

    # Split the path and get the last element
    path_elements = parsed_url.path.strip('/').split('/')
    if path_elements:
        return path_elements[-1]
    else:
        return ''

def generate_yaml_config(config: SourceConfig, output_path: Optional[Path] = None) -> str:
    """
    Generate YAML from a SourceConfig object.

    Args:
        config (SourceConfig): The configuration object to serialize
        output_path (Optional[Path]): If provided, writes the YAML to this file

    Returns:
        str: The generated YAML content
    """
    # Convert Pydantic model to dict and remove None values
    config_dict = config.model_dump()
    config_dict = remove_none_values(config_dict)

    # Custom representer for HttpUrl to convert to string
    def represent_http_url(dumper, data):
        return dumper.represent_str(str(data))

    # Custom representer for date to convert to ISO format string
    def represent_date(dumper, data):
        return dumper.represent_str(data.isoformat())

    # Add custom representers
    yaml.add_representer(HttpUrl, represent_http_url)
    yaml.add_representer(date, represent_date)

    # Generate YAML with proper formatting
    yaml_content = yaml.dump(config_dict, sort_keys=False, allow_unicode=True, default_flow_style=False)

    # Write to file if output path is provided
    if output_path:
        output_path.write_text(yaml_content)

    return yaml_content

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

    for url in tqdm(urls, desc="Processing URLs", ncols=100):
        try:
           # print(f"\nChecking {trimit(url)} for JSON-LD data...")
           jsonld_content = extract_jsonld(url)
           if jsonld_content:
               normalized = jsonld.normalize(json.loads(jsonld_content), {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
               store.load(io.StringIO(normalized), mime_type, base_iri=None, to_graph=None)
           else:
               pass

           # print("No JSON-LD content found")
        except Exception as e:
           print(f"An error occurred while processing URL {url}: {e}")


    sparql = """
    PREFIX shacl: <http://www.w3.org/ns/shacl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX schema: <https://schema.org/>

    SELECT ?pid ?propername ?url ?value
    WHERE {
        ?pid a schema:Organization .
        ?pid schema:name ?propername .
        ?pid schema:makesOffer ?offer .
        ?offer schema:itemOffered ?s .
        ?s a schema:CreativeWork .
        ?s schema:additionalType "sitemap" .
        ?s schema:additionalProperty ?p .
            ?p schema:propertyID "iode-approved" .
            ?p schema:value ?value .
        ?s schema:url ?url .
    }
    """

    r = store.query(sparql)
    q1 = list(r)
    v = r.variables

    value_list = [variable.value for variable in v]

    df = pd.DataFrame(q1, columns=value_list)
    df = df.applymap(extract_value)

    df['name'] = df.apply(lambda row: get_last_path_element(row['pid']) + process_string(row['propername']), axis=1)

    default_fields = {field: None for field in Source.model_fields.keys()}

    # Create a list of Source instances
    sources: List[Source] = []

    for _, row in df.iterrows():
        # Create a dictionary of data for the Source pydantic model
        row_data = {**default_fields, **row.to_dict()}
        # Create an instance of Source
        source_instance = Source(**row_data)
        sources.append(source_instance)


    sample_config = SourceConfig(
        sources=sources
    )

    yaml_output = generate_yaml_config(sample_config)
    full = prefix + yaml_output
    print("Generated YAML:")
    # print(remove_none_values(full))

    cleaned_dict = remove_none_values(full)

    # Save cleaned dictionary to a YAML file
    with open('gleanerconfig.yaml', 'w') as file:
        yaml.dump(cleaned_dict, file, sort_keys=False, default_flow_style=False)


if __name__ == "__main__":
    main()
