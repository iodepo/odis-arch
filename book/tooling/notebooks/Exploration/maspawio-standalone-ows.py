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

# define common variables
CSW_ENDPOINT = "http://maspawio.net/catalogue/csw"
CSW_ENDPOINT_TIMEOUT = 60 #seconds
PATH_TO_DATA_FOLDER = "./data-ows/"
NEW_RDF_FILENAME = "maspawio.rdf"
HOSTNAME = "http://maspawio.net"

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

# +
import json
from pyld import jsonld
import os, sys, io, uuid
from owslib.csw import CatalogueServiceWeb
from owslib.fes import SortBy, SortProperty
import ssl
import pandas as pd
import kglab
import logging

#log to a file
logging.basicConfig(filename='owslib.log', encoding='utf-8', level=logging.DEBUG)

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

# loop through all visible records in the endpoint, and save each layer as 
# a local JSON-LD file.  Note that CSW results are 'paged' with 10 
# records for each page.

stop = 0
flag = 0
index = 0
pagesize = 10
totalrecs = 0
sort_property = 'dc:title'  # a supported queryable of the CSW
sort_order = 'ASC'  # should be 'ASC' or 'DESC'

print("************************")
print("Parsing records...")
print("************************")
#print("\n")

while stop == 0:
    if flag == 0:  # first run, start from 0
        startpos = 0
    else:  # subsequent run, startposition is now paged
        startpos = csw.results['nextrecord']    

    csw = CatalogueServiceWeb(CSW_ENDPOINT, timeout=CSW_ENDPOINT_TIMEOUT)
    sortby = SortBy([SortProperty(sort_property, sort_order)])
    csw_dublincore_outputschema = 'http://www.opengis.net/cat/csw/2.0.2'
    csw_iso_outputschema = 'http://www.isotc211.org/2005/gmd'
    # print(csw.identification.type)
    #[op.name for op in csw.operations]
    #['GetCapabilities', 'GetRecords', 'GetRecordById', 'DescribeRecord', 'GetDomain']
    #csw.getdomain('GetRecords.resultType')
    #csw.getrecords2(esn="full", resulttype="hits", typenames='gmd:MD_Metadata')
    #WARNING: esn="full" FAILS <----- causes index/range error with Dublin Core schema profile
    #                        likely because some record titles contain special characters
    #csw.getrecords2(esn="brief", startposition=startpos, resulttype="results", typenames='csw:Record', sortby=sortby, maxrecords=pagesize)
    logging.info('getting records %d to %d', startpos, startpos+pagesize)
    #DublinCore schema request...
    #csw.getrecords2(esn="full", startposition=startpos, resulttype="results", typenames='csw:Record', sortby=sortby, maxrecords=pagesize, outputschema=csw_dublincore_outputschema)
    #ISO 19115:2003 schema request...
    #csw.getrecords2(esn="full", startposition=startpos, resulttype="results", typenames='gmd:MD_Metadata', sortby=sortby, maxrecords=pagesize, outputschema=csw_iso_outputschema)
    csw.getrecords2(esn="full", startposition=startpos, resulttype="results", typenames='gmd:MD_Metadata', maxrecords=pagesize, outputschema=csw_iso_outputschema)
    logging.debug(csw.request)
    logging.debug(csw.response)
    #print(csw.results)
      #{'matches': 149, 'returned': 10, 'nextrecord': 11}
    
    if csw.results['returned'] == 0: #no results
        break

    print(str(len(csw.records)) + " records found...")
    totalrecs += len(csw.records)  

    #harvest each record layer
    for rec in csw.records:
    
        #handle empty first record for global extents (with DublinCore schema)
        #if csw.records[rec].title != "":
        #handle empty record (with ISO schema)
        if hasattr(csw.records[rec].identification, 'title'): 

            index+=1
    
            #name
            name = csw.records[rec].identification.title
            #name = csw.records[rec].title #DublinCore
            print("    " + name)
        
            #id
            id = csw.records[rec].identifier

            #description
            description = csw.records[rec].identification.abstract
            #description = csw.records[rec].abstract #DublinCore

            #keywords
            subjects = csw.records[rec].identification.keywords
            #subjects = csw.records[rec].subjects #DublinCore
    
            #regions
            #regions = csw.records[rec].spatial #DublinCore

            #spatial data
            minx = csw.records[rec].identification.bbox.minx
            miny = csw.records[rec].identification.bbox.miny
            maxx = csw.records[rec].identification.bbox.maxx
            maxy = csw.records[rec].identification.bbox.maxy

            poly = str("""POLYGON(({} {}, {} {}, {} {}, {} {}, {} {}))""".format(minx, miny, minx, maxy, maxx, maxy, maxx, miny, minx, miny))

            data = {}

            data['@id'] = str(HOSTNAME + "/id/{}".format(id))      #id.text

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
            #print(*subjects)
            #print(subjects[0]['keywords'])
            k = subjects[0]['keywords']                 
            #for s in subjects: #DublinCore
            #    k.append(s)
            data['https://schema.org/keywords'] = k 
    
            context = {"@vocab": "https://schema.org/", "geosparql": "http://www.opengis.net/ont/geosparql#"}
            compacted = jsonld.compact(data, context)

            # need sha hash for the "compacted" var and then also generate the prov for this record.
    
            filename = str(PATH_TO_DATA_FOLDER + "maspawio{}.json".format(index))
    
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(compacted, f, ensure_ascii=False, indent=4)
        
            kgset.load_jsonld(filename)
    
    #check if next record exists 
    if csw.results['nextrecord'] == 0 \
        or csw.results['nextrecord'] > csw.results['matches']:  # end the loop, exhausted all records
        stop = 1
        break        
    
    #not first run, so trigger next page    
    flag = 1

print("\n")
print("************************")
print("Parsed " + str(totalrecs) + " records")
print("    " + str(index) + " exported to JSON-LD")
print("    " + str(totalrecs - index) + " were invalid records")
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



