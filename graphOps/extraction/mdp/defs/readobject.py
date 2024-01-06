

def read_object_to_string(mc, bucket_name, object_name):
    try:
        data = mc.get_object(bucket_name, object_name)
        data_str = data.read().decode('utf-8')
        return data_str
    except Exception as e:
        print(e)
