"""
Purpose: Download all ODIS parquet files locally       
                   
Usage:   python get-odis-parquet-files-local.py

Output:  Creates an "assets" folder in the path you specified through
         the outputFolderPath variable

Notes:   
         
Requires: Python 3.x
"""

import os
from minio import Minio

outputFolderPath = "C:/ms4w/apps/iodepo/odis-arch-git/dashboard/data/"

address = "ossapi.oceaninfohub.org:80"
bucket = "public"
prefix = "assets"

client = Minio(address, secure=False) # Create client with anonymous access.
for item in client.list_objects(bucket, prefix=prefix, recursive=True):
    if "test" not in item.object_name.lower() and "old" not in item.object_name.lower() and ".parquet" in item.object_name.lower():
        print("    downloading " + item.object_name)
        client.fget_object(bucket,item.object_name,outputFolderPath + item.object_name)
