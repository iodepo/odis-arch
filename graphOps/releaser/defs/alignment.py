import re


# popper will convert nq to nt (via a simple hack), it will also convert http to https for schema.org prefixes
def popper(input):
    lines = input.splitlines()
    modified_lines = []

    for line in lines:
        newline = line.replace("http://schema.org", "https://schema.org")
        segments = newline.split(' ')

        if len(segments) > 3:
            segments.pop()   # Remove the last two segment
            segments.pop()
            new_line = ' '.join(segments) + ' .'
            modified_lines.append(new_line)


    # print(len(modified_lines))
    result_string = '\n'.join(modified_lines)
    # print(len(result_string))

    return(result_string)

# prefalign will convert http to https for schema.org prefixes
def prefalign(input):
    lines = input.splitlines()
    modified_lines = []

    regex = re.compile(r'[\r\n\t]+')

    for line in lines:
        new_line = line.replace("http://schema.org", "https://schema.org")
        new_string = re.sub(regex, ' ', new_line)
        modified_lines.append(new_string)


    # print(len(modified_lines))
    result_string = '\n'.join(modified_lines)
    # print(len(result_string))

    return(result_string)

def publicurls(client, bucket, prefix):
    urls = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        result = client.stat_object(bucket, obj.object_name)

        if result.size > 0:  #  how to tell if an objet   obj.is_public  ?????
            url = client.presigned_get_object(bucket, obj.object_name)
            # print(f"Public URL for object: {url}")
            urls.append(url)

    return urls

