#!/bin/bash
# A wrapper script for loading RDF into Blazegraph from Minio
# usage:  jsonldLoader.sh souceBucket https://ts.collaborium.io/blazegraph/namespace/queue/sparql
# dependancies:
# Minio mc:  https://github.com/minio/mc   https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs-redirect
# jsonld:  https://github.com/digitalbazaar/jsonld.js
# curl : should be standard install on most systems

#mc_cmd() {
#    mc ls $1 | awk '{print $6}'
#}

# If you use this for ntriples, be sure to compute and/or add in a graph in the URL target
#for i in $(mc_cmd $1); do
#    mc cat $1/$i | grep -o "{[^{}]*}" $filename | grep "\"file\":" | jq .
#done


mc cat oih/$1 | grep -o "{[^{}]*}" $filename | grep "\"file\":" | jq .
