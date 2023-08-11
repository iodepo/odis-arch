# Framing JSON-LD README

Standalone script to "frame" the JSON-LD, with the goal of 
removing the `schema:` namespace from the properties, and remove 
any use of `@id` to reference other subjects inside the same
JSON-LD graph.  

For more background on framing, see: https://www.w3.org/TR/json-ld-framing/#introduction         

# Sample JSON-LD

Example source JSON-LD might look like the following (notice the 
`includedInDataCatalog` property below :
   
````
    "@graph": [
      {
          "@id": "https://pacificdata.org/data/dataset/oai-www-spc-int-83181781-a4ca-4c1f-88c6-9bef3bc657e0",
          "@type": "schema:Dataset",
          "schema:identifier": "['oai:www.spc.int:83181781-a4ca-4c1f-88c6-9bef3bc657e0', 'https://purl.org/spc/digilib/doc/cpr9d']",
          "schema:inLanguage": "en",
          "schema:includedInDataCatalog": {
              "@id": "_:N78677995425d4dd194ae2ba0ce59a407"
          }
      },
      {
          "@id": "_:N78677995425d4dd194ae2ba0ce59a407",
          "@type": "schema:DataCatalog",
          "schema:description": "",
          "schema:name": "Pacific Data Hub",
          "schema:url": "https://pacificdata.org"
      }
    ]
````
       
Output JSON-LD should look like:

````
    "@graph": [
      {
          "@id": "https://pacificdata.org/data/dataset/oai-www-spc-int-83181781-a4ca-4c1f-88c6-9bef3bc657e0",
          "@type": "schema:Dataset",
          "identifier": "['oai:www.spc.int:83181781-a4ca-4c1f-88c6-9bef3bc657e0', 'https://purl.org/spc/digilib/doc/cpr9d']",
          "inLanguage": "en",
          "includedInDataCatalog": {
            "@type": "DataCatalog",
            "description": "",
            "name": "Pacific Data Hub",
            "url": "https://pacificdata.org"
          }
      }            
    ]   
 ````
   
## Requires

Python 3.x

## Pre-Install

- install necessary Python packages: `python -m pip install -r requirements.txt`
- edit the 2 paths to the source & output folders, around line 60

## Execute

- `python framing-json-ld.py`

## Output

- output folder containing framed JSON-LD files
- logfile stored in same folder as the script



