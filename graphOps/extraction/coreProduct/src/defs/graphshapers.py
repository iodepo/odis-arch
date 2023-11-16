import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning


# pop out last element in a quad to make a triple
def popper(input):
    # lines = input.decode().split('\n')  # Split input into separate lines  HTTP source
    # lines = input.split('\n')  # Split input into separate lines
    if isinstance(input, bytes):
        lines = input.decode().split('\n')
    else:
        lines = input.split('\n')


    modified_lines = []
    for line in lines:
        newline = line.replace("http://schema.org", "https://schema.org")
        segments = newline.split(' ')
        if len(segments) > 3:
            segments.pop()  # Remove the last two segment
            segments.pop()
            new_line = ' '.join(segments) + ' .'
            modified_lines.append(new_line)

    result_string = '\n'.join(modified_lines)

    return (result_string)


def contextAlignment(input):
    # lines = input.decode().split('\n')  # Split input into separate lines  HTTP source
    # lines = input.split('\n')  # Split input into separate lines
    if isinstance(input, bytes):
        lines = input.decode().split('\n')
    else:
        lines = input.split('\n')

    modified_lines = []
    for line in lines:
        newline = line.replace("http://schema.org", "https://schema.org")
        modified_lines.append(newline)

    result_string = '\n'.join(modified_lines)

    return (result_string)


def publicurls(client, bucket, prefix):
    urls = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        result = client.stat_object(bucket, obj.object_name)

        if result.size > 0:  # how to tell if an objet   obj.is_public  ?????
            url = client.presigned_get_object(bucket, obj.object_name)
            # print(f"Public URL for object: {url}")
            urls.append(url)

    return urls


# def to_wkt(polygon_string):
#     # split the input string into pairs
#     pairs = polygon_string.split(',')
#
#     # transform each pair into 'y x' format
#     # transformed_pairs = [' '.join(reversed(pair.split())) for pair in pairs]
#     transformed_pairs = [' '.join(pair.split()) for pair in pairs]
#
#     # join the transformed pairs with a comma and a space
#     transformed_string = ', '.join(transformed_pairs)
#
#     # return the final WKT string
#     return f"POLYGON (({transformed_string}))"


def contains_alpha(s):
    if isinstance(s, (int, float)):
        return False
    return any(c.isalpha() for c in s)
