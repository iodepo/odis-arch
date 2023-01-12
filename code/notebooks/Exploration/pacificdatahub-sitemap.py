#!/usr/bin/env python

"""
Purpose: Standalone script to generate sitemap, from CKAN endpoint

Usage:   python pacificdatahub-sitemap.py

Output:  sitemap.xml
         
Requires: Python 3.x, CKAN+DCAT extension installed

"""

# define common variables
CKAN_ENDPOINT = "https://pacificdata.org/data"
CKAN_ENDPOINT_TIMEOUT = 60 #seconds
NEW_SITEMAP_FILENAME = "sitemap.xml"
HOSTNAME = "https://pacificdata.org/"
LOGFILE = "pacificdatahub-sitemap.log"
SHORTNAME = "pacificdatahub" #no spaces

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import json
import os, sys, io, uuid
import ssl
import pandas as pd
import logging
import requests
import pprint
import datetime

#log to a file
logging.basicConfig(filename=LOGFILE, encoding="utf-8", level=logging.DEBUG,  
                    format="%(asctime)s;%(levelname)s;%(message)s",  
                    datefmt="%Y-%m-%d %H:%M", filemode = "w")

# Get Today's Date to add as Lastmod
lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')

# function to print a line of html for the indented hyperlink
def printlink(url):
    print ("  <url>")
    print ("    <loc>" + url + "</loc>")
    print ("    <lastmod>" + lastmod_date + "</lastmod>")
    print ("  </url>")
    return
  
packages = CKAN_ENDPOINT + "/api/action/package_list"
response = requests.get(packages)
response_dict = json.loads(response.content)
# Check the contents of the response
assert response_dict['success'] is True  # make sure if response is OK
datasets = response_dict['result']         # extract all the packages from the response
numrecs = len(datasets)
print("Total number of packages: " + str(numrecs)) # print the total number of datasets
  # 10,965

original_stdout = sys.stdout # Save a reference to the original standard output

with open('sitemap.xml', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print ('<?xml version="1.0" encoding="UTF-8"?>')
    print ('<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">')
    
    index = 0

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
    
        # only harvest PDH records (currently FAILS!)
        #if package_dict['isPartOf'] == "pdh.pacificdatahub":
        
        #name (human readable)
        name = package_dict['title']
        logging.info("record title: %s", name)
        #print("    " + name)
        ckan_name = package_dict['name']
    
        url = CKAN_ENDPOINT + "/dataset/" + ckan_name + ".jsonld?profiles=schemaorg"
    
        printlink(url)

        index+=1
        logging.info("record number: %s", str(index))        

    print ('</urlset>')
    sys.stdout = original_stdout # Reset the standard output to its original value

print("\n")
print("************************")
print("Parsed " + str(numrecs) + " records")
print("    " + str(index) + " exported to sitemap.xml")
print("    " + str(numrecs - index) + " were invalid records")
print("************************")
print("\n")
