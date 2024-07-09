# makes a geopackage and h3 output files
# bring in https://colab.research.google.com/drive/1cIGmvpyEG2giLeeUCdzHXgb9w4Mp8h2_

from minio import Minio
from minio.error import S3Error

from minio.commonconfig import CopySource
import os
import tempfile
import fileinput
import sys
import argparse

from defs import alignment
from defs import do_ops


# read  oih/gleaner.oih/graphs/latest
# copy into/over  public/graphs if not 0

def main():
    # read the items in a prefix
    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    parser = argparse.ArgumentParser(description="Process some arguments.")
    # parser.add_argument("--align", action="align_true", help="flag to indicate schema alignment")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--zeros", action="store_true", help="Activate the Zeros flag")
    parser.add_argument("--sourcematch", type=str, default="", help="Match pattern in source resources")
    parser.add_argument("--output", type=str, help="Output file")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if not args.zeros:   # if not looking for zeros in sources, then processing to output
        if args.output is None:
            print("Error: the --output argument is required")
            sys.exit(1)

    # URL for the release graph to process
    s_url, s_bucket, s_obj = do_ops.parse_s3_url(args.source)

    if not args.zeros:
        o_url, o_bucket, o_obj = do_ops.parse_s3_url(args.output)

    # Create client with access and secret key.
    client = Minio(s_url, ak, sk, secure=False)

    print("------------------------")

    temp_directory = setup_temp_directory()

    if True:
        print("schema alignment")
        ll = do_ops.olist(client, s_bucket, s_obj, False)
        pl = do_ops.olist(client, o_bucket, o_obj, False)
        dl = do_ops.diff_lists(do_ops.remove_prefix(ll, s_obj), do_ops.remove_prefix(pl, o_obj))

        for o in dl:
            # print(o)
            fp = temp_directory.name + o

            #  download o to a local var or file (in a temp scratch)
            r = download_object(s_bucket, s_obj, o, fp, client)
            # print(r)

            # process the schema change
            replace_http_with_https(r)

            # upload the file to the new location
            upload_object(o_bucket, o_obj, fp, client)

            # print("need to copy over {}".format(o))
            # do_ops.ocopy(s_bucket, s_obj, o_bucket, o_obj, o, client)

    # temp_directory.cleanup()


# Please note that this operation creates a backup of the original
# file (with a .bak extension). If you don('t want to keep the '
# 'backup, you can remove it afterward using os.remove(filename + ').bak').
def replace_http_with_https(filename):
    with fileinput.input(files=(filename), inplace=True, backup='.bak') as file:
        for line in file:
            sys.stdout.write(line.replace('http://schema.org', 'https://schema.org'))

def download_object(bucket_name, object_prefix, object_name, local_file, client):
    try:
        data = client.get_object(bucket_name, object_prefix + object_name)
        with open(local_file, 'wb') as file_data:
            for d in data.stream(32 * 1024):
                file_data.write(d)
        print(f'Successfully downloaded {object_name} to {local_file}')
        return local_file
    except S3Error as err:
        print(f'An error occurred: {err}')
        return None

def upload_object(bucket_name, object_name, local_file, client):
    filename = os.path.basename(local_file)
    of_path = str("{}/{}").format(object_name, filename)  # object_name is the prefix without the file name
    # print(f'bucket: {bucket_name} object_name {object_name}  of_path {of_path}  local_file {local_file}')
    try:
        client.fput_object(bucket_name, of_path, local_file)
        print(f'Successfully uploaded {local_file} to {bucket_name}/{of_path}')
    except S3Error as err:
        print(f'An error occurred: {err}')

def setup_temp_directory():
    temp_dir = tempfile.TemporaryDirectory()
    # temp_dir = tempfile.mkdtemp()
    print(f'Temporary directory "{temp_dir.name}" has been created.')
    return temp_dir

if __name__ == '__main__':
    main()
