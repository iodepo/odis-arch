#!/bin/bash
#

mc_cmd() {
        mc anonymous --recursive links bucket/prefix
}

# If you use this for ntriples, be sure to add in a graph in the URL target
for i in $(mc_cmd); do
    echo "--------------------------"
    echo "Loading $i"
    curl $i | curl -X POST -H 'Content-Type:text/x-nquads' --data-binary @- https://example.org/namespace/sparql
done

