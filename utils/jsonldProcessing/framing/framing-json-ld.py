#!/usr/bin/env python

"""
Purpose: Standalone script to "frame" the JSON-LD, with the goal of 
         removing the "schema:" namespace from the properties, and remove 
         any use of "@id" to reference other subjects inside the same
         JSON-LD graph.  

         Background on framing: https://www.w3.org/TR/json-ld-framing/#introduction         

Usage:   python framing-json-ld.py

Output:  Generates a new output folder containing framed JSON-LD files.
         
Requires: Python 3.x

Notes:

  Example source JSON-LD might look like the following (notice the 
  "includedInDataCatalog" property below :
  
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
         
  Output JSON-LD should look like:
  
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
"""

# define common variables
PATH_TO_SOURCE_DATA_FOLDER = "/home/apps/minio-buckets-cioos/summoned/cioos/"
PATH_TO_OUTPUT_DATA_FOLDER = "/home/apps/minio-buckets-cioos/framed/"
LOGFILE = "./framing-json-ld.log"

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

from pyld import jsonld
import json
import os, glob
import logging

#log to a file
logging.basicConfig(filename=LOGFILE, encoding="utf-8", level=logging.DEBUG,  
                    format="%(asctime)s;%(levelname)s;%(message)s",  
                    datefmt="%Y-%m-%d %H:%M", filemode = "w")


frametext =   {
    "@context": {"@vocab": "https://schema.org/"},
    "@type": "Dataset"
}

typesList = ["Dataset", "DigitalDocument", "CreativeWork", "Movie"]

fileNum = 0

print("\n")
print("************************")
print("Parsing folder: " + PATH_TO_SOURCE_DATA_FOLDER)
print("************************")
print("\n")
logging.info("Parsing FOLDER: %s", PATH_TO_SOURCE_DATA_FOLDER)

# loop through the source data folder
for jsonldfile in glob.glob(os.path.join(PATH_TO_SOURCE_DATA_FOLDER, '*.jsonld')):
        filename = os.path.basename(jsonldfile)
        print ("parsing file: " + filename)
        
        #load the JSON-LD
        jsonloaded = json.load(open(jsonldfile, 'r'))
        
        #check if exception (possibly caused by an empty "url" parameter)
        if "code" in jsonloaded and jsonloaded["code"] == "runtime_exception":
            print("skipping file due to runtime exception in JSON-LD")
            continue        
                  
        #get the schema url
        if "@vocab" in jsonloaded["@context"]:
            context = jsonloaded["@context"]["@vocab"]
            
        elif "schema" in jsonloaded["@context"]:
            context = jsonloaded["@context"]["schema"]
            
        #get the data type
        for item in jsonloaded["@graph"]:
            if "@type" in item:
                for x in typesList:
                    typeNamespace = "schema:" + x
                    if item["@type"] == x or item["@type"] == typeNamespace:
                        print("    " + item["@type"])
                        type = x

        #modify frametext
        if "http://" in context:     
            frametext["@context"] = {"@vocab": "http://schema.org/"}
        frametext["@type"] = type
                
        #frame the JSON-LD
        framed = jsonld.frame(jsonloaded, frametext)
               
        #write the new JSON-LD file to output folder
        with open(PATH_TO_OUTPUT_DATA_FOLDER + filename, 'w') as outfile:
            outfile.write(json.dumps(framed, indent=2))
            fileNum+=1            
                    
        logging.info("    parsed: %s", filename)
                     
print("\n")
print("************************")
print("    " + str(fileNum) + " JSON-LD files have been framed")
print("************************")
print("\n")



