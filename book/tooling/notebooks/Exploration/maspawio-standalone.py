#!/usr/bin/env python

"""
Purpose: Standalone script to generate RDF from provided file "maspawio.csv"

Usage:   python maspawio-standalone.py

Output:  saves a new file: data/maspawio.rdf

Notes:

    HTTPS issue:
       Partners do need to start to move to HTTPS from HTTP, as Chrome and many
       browsers throw errors or warnings for HTTP.  Recommended method for 
       installing the certificate on Ubuntu: Let's Encrypt ( https://letsencrypt.org/ ).

"""

# define variables
PATH_TO_CSV = "./data/maspawio-http.csv"
PATH_TO_GENERATE_NEW_RDF = "./data/maspawio.rdf"
HOSTNAME = "http://maspawio.net"

#########################
# you shouldn't have to modify anything below
#########################

import json
from pyld import jsonld
import os, sys, io
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl
import pandas as pd
import kglab

# generate a Context for each connection
# disable SSL for now

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get all Catalogue record links (actually a GetRecordById request)

links = pd.read_csv(PATH_TO_CSV, skiprows=7)
linkcol = links["dclink"]
urls = linkcol.values

# prepare namespace

namespaces = {
    "schema":  "https://schema.org/",
    "shacl":   "http://www.w3.org/ns/shacl#" ,
    }

kgset = kglab.KnowledgeGraph(
    name = "Schema.org based datagraph",
    base_uri = "https://example.org/id/",
    namespaces = namespaces,
    )

# loop through all urls, parse response, and save as 
# local JSON file

index = 0

print("************************")
print("Parsing records...")
print("************************")
print("\n")

for x in urls:
    index = index +1 
    
    dcxml = x
    with urlopen(dcxml, context=ctx) as f:
        tree = ET.parse(f)
        root = tree.getroot()
        
    r = root.find('{http://www.opengis.net/cat/csw/2.0.2}Record')

    # id
    id = r.find('{http://purl.org/dc/elements/1.1/}identifier')

    # name
    # This can be used to form the URL:  https://maspawio.net/layers/geonode%3Alocally_managed_marine_areas_kenya
    name = r.find('{http://purl.org/dc/elements/1.1/}title')
    print("        " + name.text)

    # description
    description = r.find('{http://purl.org/dc/terms/}abstract')

    # keywords
    subjects = r.findall('{http://purl.org/dc/elements/1.1/}subject')

    # spatial data
    bb = r.find('{http://www.opengis.net/ows}BoundingBox')
    uc = bb.find('{http://www.opengis.net/ows}UpperCorner')
    lc = bb.find('{http://www.opengis.net/ows}LowerCorner')
    ucs = uc.text.split(" ")
    lcs = lc.text.split(" ")
    x1 = float(ucs[0])
    y1 = float(ucs[1])
    x2 = float(lcs[0])
    y2 = float(lcs[1])

    # # 'POLYGON(x1 y1, x1 y2, x2 y2, x2 y1, x1 y1)'
    poly = str("""POLYGON({}  {}  {}  {} {}  {}  {}  {} {} {})""".format(x1, y1, x1, y2, x2, y2, x2, y1, x1, y1))

    data = {}

    data['@id'] = str(HOSTNAME + "/id/{}".format(index))      #id.text

    data['@type'] = 'https://schema.org/Dataset'

    data['https://schema.org/name'] = name.text
    data['https://schema.org/description'] = description.text

    aswkt = {}
    aswkt['@type'] = "http://www.opengis.net/ont/geosparql#wktLiteral"
    aswkt['@value'] = poly

    crs = {}
    crs['@id'] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"

    hg = {}
    hg['@type'] = "http://www.opengis.net/ont/sf#Polygon" 
    hg['http://www.opengis.net/ont/geosparql#asWKT'] = aswkt
    hg['http://www.opengis.net/ont/geosparql#crs'] = crs

    data['http://www.opengis.net/ont/geosparql#hasGeometry'] = hg

    # keyword(s) loop
    k = []
    for s in subjects:
        k.append(s.text)
    data['https://schema.org/keywords'] = k 
    
    context = {"@vocab": "https://schema.org/", "geosparql": "http://www.opengis.net/ont/geosparql#"}
    compacted = jsonld.compact(data, context)

    # need sha hash for the "compacted" var and then also generate the prov for this record.
    
    filename = str("data/maspawio{}.json".format(index))
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(compacted, f, ensure_ascii=False, indent=4)
        
    kgset.load_jsonld(filename)
    
print("\n")
print("************************")
print("Parsed " + str(index) + " records")
print("************************")
print("\n")

# save RDF file locally

kgset.save_rdf(PATH_TO_GENERATE_NEW_RDF, format="ttl", base=None, encoding="utf-8")

print("\n")
print("************************")
print("File generated: " + PATH_TO_GENERATE_NEW_RDF)
print("************************")
print("\n")

