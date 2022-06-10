#!/usr/bin/env python

"""
Purpose: Standalone script to generate individual JSON-LD files
         and a master RDF document, live, from CKAN endpoint

Usage:   python pacificdatahub-harvest.py

Output:  saves a new JSON-LD file, for each catalogue record 
         exposed through the CKAN API, and also a
         .RDF resource file.
         
Requires: Python 3.x

Notes:

    HTTPS issue:
       Partners do need to start to move to HTTPS from HTTP, as Chrome and many
       browsers throw errors or warnings for HTTP.  Recommended method for 
       installing the certificate on Ubuntu: Let's Encrypt ( https://letsencrypt.org/ ).

"""

# define common variables
CKAN_ENDPOINT = "https://pacificdata.org/data"
CKAN_ENDPOINT_TIMEOUT = 60 #seconds
PATH_TO_DATA_FOLDER = "./data-pacificdatahub/" #directory must exist
NEW_RDF_FILENAME = "pacificdatahub-catalogue.rdf"
HOSTNAME = "https://pacificdata.org/"
LOGFILE = "pacificdatahub-harvest.log"
SHORTNAME = "pacificdatahub" #must be hyphen

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import json
from pyld import jsonld
import os, sys, io, uuid
import ssl
import pandas as pd
import kglab
import logging
import requests
import pprint
import numpy as np
import geojson
#from ckanapi import RemoteCKAN

#log to a file
logging.basicConfig(filename=LOGFILE, encoding="utf-8", level=logging.DEBUG,  
                    format="%(asctime)s;%(levelname)s;%(message)s",  
                    datefmt="%Y-%m-%d %H:%M", filemode = "w")

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
    
# define function for getting bounding box from GeoJSON coordinates    
def get_bounding_box(geometry):
    coords = np.array(list(geojson.utils.coords(geometry)))
    return coords[:,0].min(), coords[:,1].min(), coords[:,0].max(), coords[:,1].max()
    
index = 0

packages = CKAN_ENDPOINT + "/api/action/package_list"
response = requests.get(packages)
response_dict = json.loads(response.content)
# Check the contents of the response
assert response_dict['success'] is True  # make sure if response is OK
datasets = response_dict['result']         # extract all the packages from the response
numrecs = len(datasets)
print("Total number of packages: " + str(numrecs)) # print the total number of datasets
  # 10,965
  
#loop through all datasets
for rec in datasets:

    base_url = CKAN_ENDPOINT + "/api/action/package_show?id="

    # Construct the url for the package of interest
    package_information_url = base_url + rec

    # Make the HTTP request
    package_information = requests.get(package_information_url)

    # Use the json module to load CKAN's response into a dictionary
    package_dict = json.loads(package_information.content)

    # Check the contents of the response.
    assert package_dict['success'] is True  # again make sure if response is OK
    package_dict = package_dict['result']   # we only need the 'result' part from the dictionary
    
    # pretty print the package information to screen
    #pprint.pprint(package_dict) 
    
    # only harvest PDH records
    if package_dict['isPartOf'] == "pdh.pacificdatahub":
    
        data = {}
    
        #name (human readable)
        name = package_dict['title']
        print("    " + name)
        ckan_name = package_dict['name']
    
        #schema.org id should point to url of dataset record
        url = CKAN_ENDPOINT + "/dataset/" + ckan_name
        data["@id"] = url    
    
        #id
        id = package_dict['id']
        logging.info("record id: %s", id)

        #description
        if "notes" in package_dict:
            description = package_dict["notes"]
        else:
            description = "none"
            
        data["@type"] = "https://schema.org/Dataset"

        data["https://schema.org/name"] = name
        data["https://schema.org/description"] = description
        data["https://schema.org/url"] = url    
    
        #tags / keywords
        if "tags" in package_dict:
            tags = package_dict['tags']
            for i in range(len(tags)):
                #print(tags[i])
                if i == 0:
                    k = tags[i]["display_name"]
                else:
                    k += ", " + tags[i]["display_name"]          
        else:
            k = "none"
            
        data["https://schema.org/keywords"] = k
    
        #spatial / coverage
        if "spatial" in package_dict and package_dict['spatial'] != '':
                
            georesponse_dict = json.loads(package_dict['spatial'])
            coords = georesponse_dict['coordinates']
            bounds = get_bounding_box(coords)
            
            minx, miny, maxx, maxy = bounds
            poly = str("""POLYGON(({} {}, {} {}, {} {}, {} {}, {} {}))""".format(minx, miny, minx, maxy, maxx, maxy, maxx, miny, minx, miny))
            
            #print(bounds)
            #pprint.pprint(package_dict['spatial'])

            aswkt = {}
            aswkt["@type"] = "http://www.opengis.net/ont/geosparql#wktLiteral"
            aswkt["@value"] = poly

            crs = {}
            crs["@id"] = "http://www.opengis.net/def/crs/OGC/1.3/CRS84"

            hg = {}
            hg["@type"] = "http://www.opengis.net/ont/sf#Polygon" 
            hg["http://www.opengis.net/ont/geosparql#asWKT"] = aswkt
            hg["http://www.opengis.net/ont/geosparql#crs"] = crs

            data["http://www.opengis.net/ont/geosparql#hasGeometry"] = hg

        context = {"@vocab": "https://schema.org/", "geosparql": "http://www.opengis.net/ont/geosparql#"}
        compacted = jsonld.compact(data, context)

        # need sha hash for the "compacted" var and then also generate the prov for this record.
    
        filename = str(PATH_TO_DATA_FOLDER + SHORTNAME + "-{}.json".format(id))
    
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(compacted, f, ensure_ascii=False, indent=4)
    
        kgset.load_jsonld(filename)

        index+=1

print("\n")
print("************************")
print("Parsed " + str(numrecs) + " records")
print("    " + str(index) + " exported to JSON-LD")
print("    " + str(numrecs - index) + " were invalid records")
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