#!/usr/bin/env python

"""
Purpose: Standalone script to generate simple graph file from
         harvested JSON-LD records

Usage:   python maspawio-simple-graph.py

Output:  generates a simple graph file.
         
Requires: Python 3.x

Notes:

         After running, you might also want to run the generated file
         through the 'jsonld-cli' node.js module
         ( https://github.com/digitalbazaar/jsonld-cli ) , 
         to check format, with the command:
         
             jsonld format ina-nodc-simple-graph.json > ttt.json
    
"""

# define common variables
PATH_TO_DATA_FOLDER = "./data-maspawio/" #directory must exist
TEMPLATE_GRAPH_FILENAME = "maspawio-simple-graph-template.json"
NEW_GRAPH_FILENAME = "maspawio-simple-graph.json"
LOGFILE = "maspawio-simple-graph.log"
SHORTNAME = "maspawio" #must be hyphen

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import json
import os, glob
import shutil
import logging

#log to a file
logging.basicConfig(filename=LOGFILE, encoding="utf-8", level=logging.DEBUG,  
                    format="%(asctime)s;%(levelname)s;%(message)s",  
                    datefmt="%Y-%m-%d %H:%M", filemode = "w")


recordNum = 0

print("************************")
print("Parsing records...")
print("************************")
#print("\n")

#create graph file from template
#shutil.copy2(PATH_TO_DATA_FOLDER + TEMPLATE_GRAPH_FILENAME, PATH_TO_DATA_FOLDER + NEW_GRAPH_FILENAME)

itemStartJSONString = '''
    {
      "@type": "ListItem",
      "item": '''
      
itemEndJSONString = '''
    }'''

itemFullString = ''

# read in the template file
with open(PATH_TO_DATA_FOLDER + TEMPLATE_GRAPH_FILENAME, 'r') as outfile:
    filedata = outfile.read()

# loop through the data folder
for jsonldfile in glob.glob(os.path.join(PATH_TO_DATA_FOLDER, '*.json')):
    if not os.path.basename(jsonldfile).startswith(SHORTNAME + '-simple-graph'):
        with open(jsonldfile, 'r') as f:
            jsonldtext = f.read()
            print (jsonldfile)
                          
            #add to master string
            if recordNum != 0:
                itemFullString+= ",\n" + itemStartJSONString + "\n" + jsonldtext + "\n" + itemEndJSONString + "\n"
            else:
                itemFullString+= itemStartJSONString + "\n" + jsonldtext + "\n" + itemEndJSONString + "\n"
                        
            logging.info("parsed: %s", jsonldfile) 

            recordNum+=1
            
# Replace the target string
filedata = filedata.replace('ttt', itemFullString)
# update numberOfItems
filedata = filedata.replace('"numberOfItems": 2', '"numberOfItems": ' + str(recordNum))

# Write the file out again
with open(PATH_TO_DATA_FOLDER + NEW_GRAPH_FILENAME, 'w') as outfile:
  outfile.write(filedata)         

print("\n")
print("************************")
print("    " + str(recordNum) + " JSON-LD records exported to simple graph file")
print("************************")
print("\n")



