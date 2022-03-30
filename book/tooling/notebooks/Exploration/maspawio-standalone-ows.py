#!/usr/bin/env python

"""
Purpose: Standalone script to generate RDF from CSW endpoint

Usage:   python maspawio-standalone-ows.py

Output:  saves a new RDF file, for all catalogue records

Notes:

    HTTPS issue:
       Partners do need to start to move to HTTPS from HTTP, as Chrome and many
       browsers throw errors or warnings for HTTP.  Recommended method for 
       installing the certificate on Ubuntu: Let's Encrypt ( https://letsencrypt.org/ ).

"""

# define variables
CSW_ENDPOINT = "http://maspawio.net/catalogue/csw"
PATH_TO_DATA_FOLDER = "./data-ows/"
NEW_RDF_FILENAME = "maspawio.rdf"
HOSTNAME = "http://maspawio.net"

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import json
from pyld import jsonld
import os, sys, io
from owslib.csw import CatalogueServiceWeb
import ssl
import pandas as pd
import kglab

# generate a Context for each connection
# disable SSL for now

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

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

# loop through all visible records in the endpoint, and save as 
# local JSON file

index = 0

print("************************")
print("Parsing records...")
print("************************")
#print("\n")

csw = CatalogueServiceWeb(CSW_ENDPOINT)
# print(csw.identification.type)
#[op.name for op in csw.operations]
#['GetCapabilities', 'GetRecords', 'GetRecordById', 'DescribeRecord', 'GetDomain']
#csw.getdomain('GetRecords.resultType')
#print(csw.results)
#csw.getrecords2(esn="full", resulttype="hits", typenames='gmd:MD_Metadata')
csw.getrecords2(esn="full", resulttype="results", typenames='csw:Record')
nrecords = len(csw.records)
print(str(nrecords) + " records found...")
index = 0

for rec in csw.records:

    index = index +1
    
    #name
    name = csw.records[rec].title
    print("    " + name)
            
    #id
    id = csw.records[rec].identifier

    #description
    description = csw.records[rec].abstract

    #keywords
    subjects = csw.records[rec].subjects
    
    #regions
    regions = csw.records[rec].spatial

    #spatial data
    minx = csw.records[rec].bbox.minx
    miny = csw.records[rec].bbox.miny
    maxx = csw.records[rec].bbox.maxx
    maxy = csw.records[rec].bbox.maxy

    poly = str("""POLYGON({}  {}  {}  {} {}  {}  {}  {} {} {})""".format(minx, miny, minx, maxy, maxx, maxy, maxx, miny, minx, miny))

    data = {}

    data['@id'] = str(HOSTNAME + "/id/{}".format(index))      #id.text

    data['@type'] = 'https://schema.org/Dataset'

    data['https://schema.org/name'] = name
    data['https://schema.org/description'] = description

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
        k.append(s)
    data['https://schema.org/keywords'] = k 
    
    context = {"@vocab": "https://schema.org/", "geosparql": "http://www.opengis.net/ont/geosparql#"}
    compacted = jsonld.compact(data, context)

    # need sha hash for the "compacted" var and then also generate the prov for this record.
    
    filename = str(PATH_TO_DATA_FOLDER + "maspawio{}.json".format(index))
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(compacted, f, ensure_ascii=False, indent=4)
        
    kgset.load_jsonld(filename)

print("\n")
print("************************")
print("Parsed " + str(index) + " records")
print("************************")
print("\n")

# save RDF file locally

try:
    kgset.save_rdf(PATH_TO_DATA_FOLDER + NEW_RDF_FILENAME, format="ttl", base=None, encoding="utf-8")
except:
    print("\n")
    print("************************")
    print("Problem generating: " + PATH_TO_DATA_FOLDER + NEW_RDF_FILENAME)
    print("************************")
    print("\n")  
else:    
    print("\n")
    print("************************")
    print("Successfully generated: " + PATH_TO_DATA_FOLDER + NEW_RDF_FILENAME)
    print("************************")
    print("\n")



