#!/usr/bin/env python

"""
Purpose: Standalone script to generate a sitemap.xml from a GitHub
         repository containing JSON-LD files, such as
         https://github.com/iodepo/odis-arch/tree/master/collection/tempHosting/data-maspawio

Usage:   python maspawio-sitemap.py

Output:  sitemap.xml
         
Requires: Python 3.x

Note:    This assumes that you have checked out the repo files to your
         local machine.
         Make sure that you set the variable "GITHUB_REPO_LOCAL_PATH" 

"""

# define common variables
GITHUB_REPO_LOCAL_PATH = "E:/iodepo/odis-arch-git/collection/tempHosting/data-maspawio"
GITHUB_REPO_RAW_BASE_URL = "https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-maspawio/"
NEW_SITEMAP_FILENAME = "sitemap.xml"

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import os, sys
import datetime

# Get Today's Date to add as Lastmod
lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')

# function to print a line of html for the indented hyperlink
def printlink(url):
    print ("  <url>")
    print ("    <loc>" + url + "</loc>")
    print ("    <lastmod>" + lastmod_date + "</lastmod>")
    print ("  </url>")
    return
    
original_stdout = sys.stdout # Save a reference to the original standard output    

#create sitemap.xml    
with open(NEW_SITEMAP_FILENAME, 'w', newline='\n') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print ('<?xml version="1.0" encoding="UTF-8"?>')
    print ('<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">')
    
    #use a Python set, to force unique values
    urls = set()
        
    #loop through directories
    for subdir, dirs, files in os.walk(GITHUB_REPO_LOCAL_PATH):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                path = os.path.dirname(filepath)
                urls.add(GITHUB_REPO_RAW_BASE_URL + file)
                             
    #iterate through unique record urls
    for val in urls:
        printlink(val)
        
    print ('</urlset>', end='')
    sys.stdout = original_stdout # Reset the standard output to its original value

print("\n")
print("************************")
print("    " + str(len(urls)) + " records exported to sitemap.xml")
print("************************")
print("\n")