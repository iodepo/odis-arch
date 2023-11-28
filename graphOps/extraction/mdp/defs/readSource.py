from urllib.request import urlopen


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
