import os
from minio import Minio
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from io import BytesIO

# def write_bytes(source):
#     url, bucket, obj = parse_s3_url(source)
#
#     sk = os.getenv("MINIO_SECRET_KEY")
#     ak = os.getenv("MINIO_ACCESS_KEY")
#
#     # Create client with access and secret key.
#     mc = Minio(url, ak, sk, secure=False)
#     data = mc.get_object(bucket, obj)
#     d = data.read()
#
#     return d


def get_bytes(source):
    url, bucket, obj = parse_s3_url(source)

    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    # Create client with access and secret key.
    mc = Minio(url, ak, sk, secure=False)
    data = mc.get_object(bucket, obj)
    d = data.read()

    return d


def reads3url(source):
    url, bucket, obj = parse_s3_url(source)

    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    # Create client with access and secret key.
    mc = Minio(url, ak, sk, secure=False)
    d = read_object_to_string(mc, bucket, obj)

    return d


def read_object_to_string(mc, bucket_name, object_name):
    try:
        data = mc.get_object(bucket_name, object_name)
        data_str = data.read().decode('utf-8')
        return data_str
    except Exception as e:
        print(e)


def parse_s3_url(s3_url):
    protocol, url = s3_url.split("://")
    if protocol != 's3':
        raise ValueError('URL is not a valid S3 URL')

    split_url = url.split("/")
    server_url = split_url[0]
    bucket_name = split_url[1]
    object_path = "/".join(split_url[2:])

    return server_url, bucket_name, object_path


def get_object(target):
    # it's an S3 based object
    print("Reading object from minio")

    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")
    srv, bkt, obj = parse_s3_url(target)

    # Create client with access and secret key.
    mc = Minio(srv, ak, sk, secure=False)

    try:
        data = mc.get_object(bkt, obj)
        buffer = BytesIO(data.read())

        # Use PyArrow to read the Parquet file into a Table
        table = pq.read_table(buffer)

        # Convert the PyArrow Table into a pandas DataFrame
        df = table.to_pandas()
        return df
    except Exception as e:
        print(f"Error getting object: {e}")

