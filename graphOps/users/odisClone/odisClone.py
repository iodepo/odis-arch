import warnings
import argparse
import sys
import os
import requests
from minio import Minio
from concurrent.futures import ThreadPoolExecutor

warnings.simplefilter(action='ignore', category=FutureWarning)  # remove pandas future warning


def main():
    parser = argparse.ArgumentParser(description="Script with two modes: download and load")
    subparsers = parser.add_subparsers()

    download_parser = subparsers.add_parser('download')
    download_parser.add_argument("--source", type=str, help="Source file/URL")
    download_parser.add_argument("--outputdir", type=str, help="Output directory")
    download_parser.set_defaults(func=modeDownload)


    load_parser = subparsers.add_parser('load')
    load_parser.add_argument("--sourcedir", type=str, help="Source file/URL")
    load_parser.set_defaults(func=modeLoad)

    args = parser.parse_args()
    args.func(args)

def modeLoad(args):
    # Load to Minio
    # curl -v -X POST -H 'Content-Type:text/x-nquads' --data-binary @./data/cioos_release.nt http://localhost:7878/store

    directory_path = "data"

    for f in os.listdir(directory_path):
        fp = os.path.join(directory_path, f)
        print(f"Loading: {fp}")
        d = f2bs(fp)
        mimetype = "text/x-nquads"
        headers = {'Content-Type': mimetype}
        url="http://localhost:7878/store"
        r = response = requests.post(url, data=d, headers=headers)
        # r = post_data(url="http://localhost:7878/store",
        #               mimetype="Content-Type:text/x-nquads",
        #               data=ff)
        print(r)


def modeDownload(args):

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.outputdir is None:
        print("Error: the --outputdir argument is required")
        sys.exit(1)

    source = args.source  ## TODO  implement this
    client = Minio("ossapi.oceaninfohub.org:80", secure=False)  # Create client with anonymous access.
    urls = publicurls(client, "commons", "OIH-KG/21022024/nt")

    directory_path = args.outputdir

    # Check if the directory exists
    if not os.path.exists(directory_path):
        # Create the directory
        os.makedirs(directory_path)

    with ThreadPoolExecutor() as executor:
        for url in urls:
            if "_prov" not in url:
                executor.submit(download_file, url)


def f2bs(filename):
    with open(filename, 'r') as file:
        return file.read()

def post_data(url, mimetype, data):
    headers = {'Content-Type': mimetype}
    response = requests.post(url, files=data, headers=headers)
    return response

def publicurls(client, bucket, prefix):
    urls = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        result = client.stat_object(bucket, obj.object_name)

        if result.size > 0:  # how to tell if an objet   obj.is_public  ?????
            url = client.presigned_get_object(bucket, obj.object_name)
            # print(f"Public URL for object: {url}")
            urls.append(url)

    return urls

def download_file(url):
    """Downloads a remote file and handles potential errors."""
    try:
        response = requests.get(url, stream=True)  # Stream for efficient memory usage
        response.raise_for_status()  # Raise exception for error codes

        filename = url.split("/")[-1]
        local_filename = f"./data/{filename.replace('.nq', '.nt')}"  # Convert extension

        with open(local_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):  # Download in chunks
                f.write(chunk)

        print(f"Downloaded: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Download failed for {url}: {e}")




if __name__ == '__main__':
    main()