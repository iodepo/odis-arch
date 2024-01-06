# makes a geopackage and h3 output files
# bring in https://colab.research.google.com/drive/1cIGmvpyEG2giLeeUCdzHXgb9w4Mp8h2_

from minio import Minio
from minio.commonconfig import CopySource
import os


# read  oih/gleaner.oih/graphs/latest
# copy into/over  public/graphs if not 0

def main():
    # read the items in a prefix

    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    # Create client with access and secret key.
    client = Minio("nas.lan:49153", ak, sk, secure=False)

    sbucket = "gleaner.oih"
    sprefix = "graphs/latest/"
    ll = olist(client, sbucket, sprefix)
    # for o in ll:
    #     print(o)

    dbucket = "public"
    dprefix = "graphs/test1/"
    pl = olist(client, dbucket, dprefix)
    # for o in pl:
    #     print(o)

    print("------------------------")

    # dl = diff_lists(ll, pl)
    dl = diff_lists(remove_prefix(ll, sprefix), remove_prefix(pl, dprefix))

    for o in dl:
        print("need to copy over {}".format(o))
        ocopy(sbucket, sprefix, dbucket, dprefix, o, client)


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


if __name__ == '__main__':
    main()
