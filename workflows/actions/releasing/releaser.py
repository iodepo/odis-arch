# makes a geopackage and h3 output files
# bring in https://colab.research.google.com/drive/1cIGmvpyEG2giLeeUCdzHXgb9w4Mp8h2_

from minio import Minio
from minio.commonconfig import CopySource
import os
import sys
import re
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
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--zeros", action="store_true", help="Activate the Zeros flag")
    parser.add_argument("--sourcematch", type=str, default="", help="Match pattern in source resources")
    parser.add_argument("--output", type=str, help="Output file")
    # parser.add_argument("--schemaalign", action="schema_align", help="flag to indicate schema alignment")

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

    if args.zeros:
        zl = do_ops.olist(client, s_bucket, s_obj, True)
        print("The following files are zero length and need to be reviewed")
        for z in zl:
            print(z)
    else:
        ll = do_ops.olist(client, s_bucket, s_obj, False)
        pl = do_ops.olist(client, o_bucket, o_obj, False)
        dl = do_ops.diff_lists(do_ops.remove_prefix(ll, s_obj), do_ops.remove_prefix(pl, o_obj))

        if bool(args.sourcematch):
            print("Removing files not matching {}".format(args.sourcematch))
            dl = [s for s in dl if args.sourcematch in s]

        for o in dl:
            print("need to copy over {}".format(o))
            do_ops.ocopy(s_bucket, s_obj, o_bucket, o_obj, o, client)

if __name__ == '__main__':
    main()
