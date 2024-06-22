import requests
import json

def ppjson(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))

with open('/home/fils/.zenodo_sandbox', 'r') as file:
    ACCESS_TOKEN =   file.read().strip()
    
with open('upload.json', 'r') as file:
    jsondata =   file.read()
    
print(ACCESS_TOKEN)
    
params = {'access_token': ACCESS_TOKEN}
headers = {"Content-Type": "application/json"}
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                  params=params,
                  json={},
                  headers=headers)

sc = r.status_code
print(sc)

j = r.json()
ppjson(j)

bucket_url = r.json()["links"]["bucket"]
deposition_url = r.json()["links"]["self"]

''' New API '''
filename = "loremipsum.txt"
path = "./%s" % filename

''' 
The target URL is a combination of the bucket link with the desired filename
seperated by a slash.
'''
with open(path, "rb") as fp:
    r = requests.put(
        "%s/%s" % (bucket_url, filename),
        data=fp,
        params=params,
    )

ppjson(r.json())
    
data = {
    'metadata': {
        'title': 'My first upload',
        'upload_type': 'poster',
        'description': 'This is my first upload',
        'creators': [{'name': 'Doe, John',
                      'affiliation': 'Zenodo'}]
    }
}
r = requests.put(deposition_url,
                 params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
                 headers=headers)

print(r.status_code)
