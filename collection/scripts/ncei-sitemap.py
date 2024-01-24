#!/usr/bin/env python

"""
Purpose: Standalone script to generate a sitemap.xml from a CSV,
         where the CSV was generated from a data export
         from the Marine Microplastics viewer
         https://www.ncei.noaa.gov/products/microplastics

Usage:   python ncei-sitemap.py

Output:  sitemap.xml
         
Requires: Python 3.x

Note:    the url <loc> value must be unique, for the sitemap to be valid
         (meaning: you cannot have duplicate urls listed inside
         the sitemap.xml)

"""

# define common variables
CSV_FILENAME = "MarineMicroplastics-2024-01-10.csv"
NEW_SITEMAP_FILENAME = "sitemap.xml"

"""
#########################
# you shouldn't have to modify anything below
#########################
"""

import csv
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
    
    #open existing CSV for reading
    with open(CSV_FILENAME, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter =',',quotechar ='"',quoting=csv.QUOTE_MINIMAL)
       
        #loop through all records
        for row in reader:
            urls.add(row['Accession Link'])
                             
    #iterate through unique record urls
    for val in urls:
        printlink(val)
        
    print ('</urlset>')
    sys.stdout = original_stdout # Reset the standard output to its original value

print("\n")
print("************************")
print("    " + str(len(urls)) + " records exported to sitemap.xml")
print("************************")
print("\n")
