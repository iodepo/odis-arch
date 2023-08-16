#!/usr/bin/env python

import requests
import json
import os
import sys

example_input_json = \
'''
{
    "author" : "Lee, Jin",
    "affiliation" : "Stanford University",
    "data" : [
        {
            "title" : "Dataset CTCF (1/2) for ENCODE-DREAM TF Binding Challenge",
            "description" : "Dataset CTCF (1/2) for ENCODE-DREAM in vivo Transcription Factor Binding Site Prediction Challenge",
            "files" : [
                "/users/leepc12/code/atac-seq-pipeline/cromwell-executions/atac/223a2529-028e-43aa-98f9-6079fa9c5d30/call-bowtie2/shard-1/execution/ENCFF641SFZ.subsampled.400.trim.merged.bam",
                "/users/leepc12/code/atac-seq-pipeline/cromwell-executions/atac/223a2529-028e-43aa-98f9-6079fa9c5d30/call-bowtie2/shard-0/execution/ENCFF341MYG.subsampled.400.trim.merged.bam"               
            ]
        },
        {
            "title" : "Dataset CTCF (2/2) for ENCODE-DREAM TF Binding Challenge",
            "description" : "Dataset CTCF (2/2) for ENCODE-DREAM in vivo Transcription Factor Binding Site Prediction Challenge",
            "files" : [
                "/users/leepc12/code/atac-seq-pipeline/cromwell-executions/atac/223a2529-028e-43aa-98f9-6079fa9c5d30/call-filter/shard-0/execution/ENCFF341MYG.subsampled.400.trim.merged.nodup.bam",
                "/users/leepc12/code/atac-seq-pipeline/cromwell-executions/atac/223a2529-028e-43aa-98f9-6079fa9c5d30/call-filter/shard-1/execution/ENCFF641SFZ.subsampled.400.trim.merged.nodup.bam"
            ]
        }
    ]
}
'''

def upload_to_zenodo(access_token, author, affiliation, title, desc, files):    
    print('='*40)
    print(author, affiliation, title, desc)
    r1 = requests.get('https://zenodo.org/api/deposit/depositions',
                        params={'access_token': access_token})
    print(r1.status_code)

    headers = {"Content-Type": "application/json"}
    r2 = requests.post('https://zenodo.org/api/deposit/depositions',
                        params={'access_token': access_token}, json={},
                        headers=headers)
    print(r2.status_code)

    deposition_id = r2.json()['id']
    print('deposition_id = {}'.format(deposition_id))

    for f in files:
        print('uploading {}...'.format(f))
        data = {'filename': os.path.basename(f)}
        files_ = {'file': open(f, 'rb')}
        r3 = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                          params={'access_token': access_token}, data=data,
                          files=files_)
        print('uploading done. status: {}'.format(r3.status_code))
        # print(json.dumps(r3.json(),indent=4))

    data = {
        'metadata': {
            'title': title,
            'upload_type': 'dataset',
            'description': desc,
            'creators': [{'name': author, 'affiliation': affiliation}]
        }
    }

    r4 = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                     params={'access_token': access_token}, data=json.dumps(data),
                     headers=headers)
    print(r4.status_code)
    # print(json.dumps(r4.json(),indent=4))

def main():
    if len(sys.argv)!=3:        
        print("Usage: python {} [INPUT_JSON] [ZENODO_ACCESS_TOKEN]\n\nExample [INPUT_JSON]\n{}".format(
            sys.argv[0],example_input_json))
        sys.exit(1)
    access_token = sys.argv[2]
    with open(sys.argv[1]) as f:
        json_obj = json.load(f)

    for elem in json_obj['data']:
        upload_to_zenodo(access_token, json_obj['author'], json_obj['affiliation'],
            elem['title'], elem['description'], elem['files'])

if __name__=='__main__':
    main()

