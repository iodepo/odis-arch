"""
Purpose: Standalone script to parse public S3 bucket items, which are
         in NetCDF format, and then generate JSON-LD for each item, 
         based on the ODIS pattern template: 
         https://github.com/iodepo/odis-arch/blob/master/book/thematics/dataset/graphs/wodCastDataset.json        

Background: - World Oceans Database (WOD) S3 home: https://noaa-wod-pds.s3.amazonaws.com/index.html        
            - WOD S3 connection info: https://registry.opendata.aws/noaa-wod/
                   - see right-panel on page
                   
Usage:   python -m pip install -r requirements.txt
         python wod-s3-ncparser.py

Output:  Generates JSON-LD files into an existing output folder locally.
         See the file 'sample-output.json' for an example.

Notes:   Avoids Python MemoryError by checking filesize and downloading
         the file locally (if larger than 400MB), else reads the remote 
         NetCDF file from the S3 resource into memory. Set the
         FILESIZE_THRESHOLD variable on line#41.
         
Requires: Python 3.x
"""

import netCDF4 as nc
import pandas as pd
from datetime import datetime
import boto3
from botocore.handlers import disable_signing
import logging
import gc
import os
import json
from pyld import jsonld

# define common variables
S3_BUCKET_NAME = "noaa-wod-pds"
OUTPUT_FOLDER = "./output/" #must exist
LOGFILE = OUTPUT_FOLDER + "wod-parsed.log" #will get created
URL_BASEPATH_WHERE_JSONLD_FILES_WILL_LIVE_LATER = "https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-wod/"
FILESIZE_THRESHOLD = 400000 #(in KB) if greater, then download file instead of processing in memory.  Default is 400 MB

#log to a file
logging.basicConfig(filename=LOGFILE, encoding="utf-8", level=logging.DEBUG,  
                    format="%(asctime)s;%(levelname)s;%(message)s",  
                    datefmt="%Y-%m-%d %H:%M", filemode = "w")

def cdf2df(data, largeFileFlag):
        
    if largeFileFlag == 0:
        # regular-sized file, so use Python's memory buffer
        nc_file = nc.Dataset("wodfile.nc", memory=data)
    else:
        # large file, over 500 MB, that often causes Python MemoryError
        # so load file locally instead
        nc_file = nc.Dataset(data)

    # Get the metadata
    metadata = nc_file.ncattrs()
    # print(metadata)

    # Print the metadata
    metadata_dict = {}
    for key in metadata:
        # print("{}  :\t {}".format(key, nc_file.getncattr(key)))
        metadata_dict[key] = str("{}".format(nc_file.getncattr(key)))

    # print(metadata_dict)

    df = pd.DataFrame(metadata_dict, index=[0])
    
    nc_file.close()
    del nc_file
    
    return df   

if __name__ == '__main__':
        
    #setup connection to public S3 bucket through boto3 client 
    resource = boto3.resource('s3')
    resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)            
    bucket = resource.Bucket(S3_BUCKET_NAME)
    
    itemCount = 0
    largeFileFlag = 0

    for item in bucket.objects.all():
        if item.key.endswith(".nc"):
        #if item.key == "2010/wod_gld_2010.nc": #big file, ~1GB size
            itemCount+=1
            #print(item.key)
            
            print("Parsing item: " + item.key)
            logging.info("Parsing item: %s", item.key)
            
            file_size = round(item.size*1.0/1024, 2)
            print("    size: " + str(file_size) + " MB")
            
            if file_size > FILESIZE_THRESHOLD:  #avoid memory error, download locally
               print("    large file, downloading locally instead...")
               #download file locally
               bucket.download_file(item.key, OUTPUT_FOLDER + "wodfile.nc")
               resourceBody = OUTPUT_FOLDER + "wodfile.nc";
               largeFileFlag = 1
               
            else:
               #read resource body (data) through the boto3.resource
               resourceBody = item.get()['Body'].read()
               largeFileFlag = 0
                           
            #get the NetCDF file's metadata into a dataframe
            df = cdf2df(resourceBody, largeFileFlag)
            
            #also save the metadata into the output folder as CSV, 
            #  useful for debugging
            keyParsed = os.path.basename(item.key);
            keyParsed = keyParsed.replace(".nc", "");
            df.to_csv(OUTPUT_FOLDER + keyParsed + ".csv",index=True, header=True)            
            
            #generate JSON-LD file
            data = {}
            
            context = {"@vocab": "https://schema.org/", "geosparql": "http://www.opengis.net/ont/geosparql#"}
            data["@type"] = "https://schema.org/Dataset"            

            #name
            name = df["title"].values[0] + ": " + item.key
            print("    name: " + name)
            data["https://schema.org/name"] = name
            
            #decription
            description = df["summary"].values[0]
            print("    description: " + description)
            data["https://schema.org/description"] = description
            
            #url should point to the readable catalogue page for that record
            url = "https://noaa-wod-pds.s3.amazonaws.com/"
            print("    url: " + url)
            data["https://schema.org/url"] = url
            
            #id should point to url of the generated JSON-LD filename
            idUrl = URL_BASEPATH_WHERE_JSONLD_FILES_WILL_LIVE_LATER + keyParsed + ".json"        
            print("    id: " + idUrl)       
            data["@id"] = idUrl
            
            #identifier
            identifier = {}
            identifier["@type"] = "https://schema.org/PropertyValue"
            identifier["https://schema.org/description"] = "These identifiers for individual casts are assigned by the World Ocean Database"
            idPath = df["id"].values[0]
            identifier["https://schema.org/propertyID"] = idPath
            print("    identifier: " + idPath)   
            data["https://schema.org/identifier"] = identifier
            
            #publisher
            publisher = {}
            publisher["@type"] = "https://schema.org/Organization" 
            publisher["https://schema.org/name"] = df["publisher_name"].values[0]
            print("    publisher: " + df["publisher_name"].values[0])
            publisher["https://schema.org/url"] = df["publisher_url"].values[0]
            data["https://schema.org/publisher"] = publisher            

            #distribution
            distribution = {}
            distribution["@type"] = "https://schema.org/DataDownload" 
            distribution["https://schema.org/contentUrl"] = "https://noaa-wod-pds.s3.amazonaws.com/" + item.key
            data["https://schema.org/distribution"] = distribution 

            #spatial data
            minx = df["geospatial_lon_min"].values[0]
            miny = df["geospatial_lat_min"].values[0]
            maxx = df["geospatial_lon_max"].values[0]
            maxy = df["geospatial_lat_max"].values[0]
           
            #schema.org expects lat long (Y X) coordinate order
            boxCoords = str("""{} {} {} {}""".format(miny, minx, maxy, maxx))
            print("    GeoShape:Box: " + boxCoords)
            spatialCov = {}
            spatialCov["@type"] = "https://schema.org/Place"
            geo = {}
            geo["@type"] = "https://schema.org/GeoShape"
            geo["https://schema.org/box"] = boxCoords 
            spatialCov["https://schema.org/geo"] = geo

            geospatialVerticalMin = df["geospatial_vertical_min"].values[0]
            geospatialVerticalMax = df["geospatial_vertical_max"].values[0]
            geospatialVerticalUnits = df["geospatial_vertical_units"].values[0]
            geospatialVerticalPositive = df["geospatial_vertical_positive"].values[0]
            print("    geospatialVerticalMax: " + geospatialVerticalMax)
            print("    geospatialVerticalUnits: " + geospatialVerticalUnits)            
            additionalProperty = []
            additionalProperty1 = {}
            additionalProperty1["https://schema.org/name"] = "Geospatial vertical min"           
            additionalProperty1["https://schema.org/value"] = geospatialVerticalMin            
            additionalProperty.append(additionalProperty1)             
            additionalProperty2 = {}
            additionalProperty2["https://schema.org/name"] = "Geospatial vertical max"           
            additionalProperty2["https://schema.org/value"] = geospatialVerticalMax            
            additionalProperty.append(additionalProperty2)            
            additionalProperty3 = {}
            additionalProperty3["https://schema.org/name"] = "Geospatial vertical units"           
            additionalProperty3["https://schema.org/value"] = geospatialVerticalUnits
            additionalProperty.append(additionalProperty3)
            additionalProperty4 = {}
            additionalProperty4["https://schema.org/name"] = "Geospatial vertical positive"           
            additionalProperty4["https://schema.org/value"] = geospatialVerticalPositive
            additionalProperty.append(additionalProperty4)             
            spatialCov["https://schema.org/additionalProperty"] = additionalProperty              
            data["https://schema.org/spatialCoverage"] = spatialCov            

            #keywords
            keywords = df["keywords"].values[0]
                            
            if not keywords:
                print("    keywords: empty")
            else:
                print("    keywords: " + keywords)
                keywords_list = keywords.split(",")
                data["https://schema.org/keywords"] = keywords_list 
 
            #dateCreated
            dateCreated = df["date_created"].values[0]
            print("    dateCreated: " + dateCreated)
            data["https://schema.org/dateCreated"] = dateCreated

            #dateModified
            dateModified = df["date_modified"].values[0]
            print("    dateModified: " + dateModified)
            data["https://schema.org/dateModified"] = dateModified

            #creditText
            creditText = df["references"].values[0]
            print("    creditText: " + creditText)
            data["https://schema.org/creditText"] = creditText

            #author
            author = {}
            author["@type"] = "https://schema.org/Organization" 
            author["https://schema.org/name"] = df["creator_name"].values[0]
            print("    author: " + df["creator_name"].values[0])
            author["https://schema.org/url"] = df["creator_url"].values[0]
            data["https://schema.org/author"] = author

            #license
            license = df["license"].values[0]
            
            if not license:
                print("    license: empty")
            else:
                print("    license: " + license)
                data["https://schema.org/license"] = license

            #startTime / endTime
            startTime = df["time_coverage_start"].values[0]
            endTime = df["time_coverage_end"].values[0]
            print("    startTime: " + startTime)
            print("    endTime: " + endTime)

            subjectOf = {}
            subjectOf["@type"] = "https://schema.org/Event"
            subjectOf["https://schema.org/name"] = item.key
            subjectOf["https://schema.org/description"] = "About the multi-cast event " + item.key + " (such as time of the cast)"            
            potentialAction = {}
            potentialAction["@type"] = "https://schema.org/Action"
            potentialAction["https://schema.org/name"] = "Time of the event for: " + item.key            
            potentialAction["https://schema.org/startTime"] = startTime
            potentialAction["https://schema.org/endTime"] = endTime
            subjectOf["https://schema.org/potentialAction"] = potentialAction
            data["https://schema.org/subjectOf"] = subjectOf
            
            #export to JSON-LD file
            compacted = jsonld.compact(data, context)
            
            jsonFilePath = OUTPUT_FOLDER + keyParsed + ".json"
    
            with open(jsonFilePath, "w", encoding="utf-8") as f:
                json.dump(compacted, f, ensure_ascii=False, indent=4)

            print("\n")

            #delete df due to memory consumption
            del df
            gc.collect()
                    
    print(str(itemCount) + " items processed in bucket")
    logging.info("%s items processed in bucket", str(itemCount))            
