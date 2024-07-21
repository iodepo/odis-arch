#!/bin/bash
# A wrapper script for loading RDF into Jena
# usage:  load2Blaze.sh directory endpoint
# example:  load2Blaze.sh mydata.nq https://example.org/blazegraph/namespace/kb/sparql
# example:  load2Blaze.sh mydata.nq http://localhost:7878/store
pushd $1

files=$( ls -1  *.nq )
counter=0
for i in $files ; do
    echo "-------------start-------------"
    echo Next: $i
    # rapper -e -c -i nquads $i
    curl -X POST -H 'Content-Type:text/x-nquads' --data-binary @$i $2
    echo "-------------done--------------"
done

popd

