#!/bin/bash

for file in "$@"; do
    if [ -f "$file" ]; then
        echo "## ${file}"
        curl  -s -XPOST  --header "Content-Type:application/sparql-query" --data-binary @${file}  "http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql?format=json"  | jq .results.bindings  | jq -r -L. 'include "json2csv"; json2csv' - | csv2md
        echo "   "
        echo "   "
    else
        echo "$file is not a valid file"
    fi
done
