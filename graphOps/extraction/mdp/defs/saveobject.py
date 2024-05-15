from urllib.request import urlopen
import sys
import os
import io
import pyarrow as pa
import pyarrow.parquet as pq

from minio import Minio

from . import readobject

def write_data(target, mf):
    if target.startswith('s3://'):
        # it's an S3 based object
        print("Saving results to minio")

        sk = os.getenv("MINIO_SECRET_KEY")
        ak = os.getenv("MINIO_ACCESS_KEY")
        srv, bkt, obj = readobject.parse_s3_url(target)

        # Create client with access and secret key.
        mc = Minio(srv, ak, sk, secure=False)

        # Convert the DataFrame to a parquet file
        table = pa.Table.from_pandas(mf)
        buf = io.BytesIO()
        pq.write_table(table, buf)
        buf.seek(0)

        try:
            mc.put_object(bkt, obj, buf, len(buf.getvalue()))
        except Exception as e:
            print(f"Error saving object: {e}")
    else:
        # It's a file
        print("Saving results to file")
        _, file_extension = os.path.splitext(target)

        if file_extension == '.parquet':
            # mf = mf.astype(str) # WARNING do I want this?   if empty colum, perhaps just remove and use schema name mapping? (used exact schema)
            mf.to_parquet(target, engine='fastparquet')  # engine must be one of 'pyarrow', 'fastparquet'
            # mf.write_parquet(target)  # engine must be one of 'pyarrow', 'fastparquet'
        elif file_extension == '.csv':
            mf.to_csv(target)
        else:
            print(f'Error: unsupported file extension {file_extension}. Support .parquet or .csv only')
