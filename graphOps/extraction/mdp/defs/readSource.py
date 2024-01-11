from urllib.request import urlopen
from . import readobject


def read_data(source):
    if source.startswith('http://') or source.startswith('https://'):
        # It's a URL
        df = urlopen(source)
        dg = df.read()
    elif source.startswith('s3://'):
        # it's an S3 based object
        dg = readobject.reads3url(source)
    else:
        # It's a file
        with open(source, 'r') as file:
            dg = file.read()
    return dg
