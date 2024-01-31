# makes a geopackage and h3 output files
# bring in https://colab.research.google.com/drive/1cIGmvpyEG2giLeeUCdzHXgb9w4Mp8h2_

from minio import Minio
from minio.commonconfig import CopySource
import os, sys
import argparse

# read  oih/gleaner.oih/graphs/latest
# copy into/over  public/graphs if not 0

def main():
    # read the items in a prefix
    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--output", type=str, help="Output file")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.output is None:
        print("Error: the --output argument is required")
        sys.exit(1)

    # URL for the release graph to process
    s_url, s_bucket, s_obj = parse_s3_url(args.source)
    o_url, o_bucket, o_obj = parse_s3_url(args.output)

    # Create client with access and secret key.
    client = Minio(s_url, ak, sk, secure=False)

    # sbucket = "gleaner.oih"
    # sprefix = "graphs/latest/"
    ll = olist(client, s_bucket, s_obj)
    # for o in ll:
    #     print(o)

    # dbucket = "public"
    # dprefix = "graphs/test1/"
    pl = olist(client, o_bucket, o_obj)
    # for o in pl:
    #     print(o)

    print("------------------------")

    # dl = diff_lists(ll, pl)
    dl = diff_lists(remove_prefix(ll, s_obj), remove_prefix(pl, o_obj))

    for o in dl:
        print("need to copy over {}".format(o))
        ocopy(s_bucket, s_obj, o_bucket, o_obj, o, client)


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


def olist(client, bucket, prefix):
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
                print("found 0 len object {}".format(o))
        except Exception as e:
            print(e)

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

if __name__ == '__main__':
    main()
