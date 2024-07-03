from minio import Minio
from minio.commonconfig import CopySource
import os
import sys
import re
import argparse


def ocopy(src_bucket, src_prefix, dst_bucket, dst_prefix, object_name, client):
    src = CopySource(src_bucket, src_prefix + object_name)

    try:
        # copy object with new key in same bucket.
        client.copy_object(dst_bucket, dst_prefix + object_name, src)
        print(f"Object '{object_name}' has been copied to '{dst_prefix + object_name}'")
    except Exception as err:
        print(f"An error occurred: {err}")


def diff_lists(source, destination):
    return [item for item in source if item not in destination]


def remove_prefix(lst, prefix):
    return [item.replace(prefix, '', 1) for item in lst]


def olist(client, bucket, prefix, zeros):
    objects = client.list_objects(
        bucket, prefix=prefix, recursive=True,
    )

    onl = [obj.object_name for obj in objects]

    znl = []
    for o in onl:
        try:
            obj_info = client.stat_object(bucket, o)
            # print("{} is {} ".format(o, obj_info.size))
            if obj_info.size <= 0:
                znl.append(o)
                # print("Skipping 0 len object {}".format(o))
        except Exception as e:
            print(e)

    if zeros:
        return znl
    else:
        onl = [item for item in onl if item not in znl]

    return onl


def parse_s3_url(s3_url):
    protocol, url = s3_url.split("://")
    if protocol != 's3':
        raise ValueError('URL is not a valid S3 URL')

    split_url = url.split("/")
    server_url = split_url[0]
    bucket_name = split_url[1]
    object_path = "/".join(split_url[2:])

    return server_url, bucket_name, object_path