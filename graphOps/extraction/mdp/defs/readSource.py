from urllib.request import urlopen
# from minio import Minio


def read_data(source):
    if source.startswith('http://') or source.startswith('https://'):
        # It's a URL
        df = urlopen(source)
        dg = df.read()
    else:
        # It's a file
        with open(source, 'r') as file:
            dg = file.read()
    return dg


# add in s3:// support
# # Initialize minioClient with an endpoint and access/secret keys.
# minioClient = Minio('play.minio.io:9000',
#                     access_key='YOURACCESSKEY',
#                     secret_key='YOURSECRETKEY',
#                     secure=True)
#
# # Use function to read object into a string
# object_string = read_object_to_string(minioClient, 'mybucket', 'myobject')
# print(object_string)
