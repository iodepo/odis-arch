#1/bin/bash

# jsonld format -q sos.jsonld | rapper -i nquads -o dot -I https://science-on-schema.org/ - | dot -Grankdir=TP  -Tsvg -o sos.svg

jsonld format -q $1 | \
    rapper -q -i nquads -o dot -I https://science-on-schema.org/ - | \
    sed - -e 's/https:\/\/schema.org\//schema\:/g' |   \
    sed - -e 's/http:\/\/www.w3.org\/1999\/02\/22\-rdf\-syntax\-ns\#type/rdfs\:type/g' | \
    sed - -e 's/http:\/\/www.w3.org\/2001\/XMLSchema\#/XMLSchema\#/g' | \
    dot  -Estyle=dotted -Gsplines=true -Grankdir=TP  -Tsvg -o $2
    #neato -Goverlap=false -Estyle=dotted -Gsplines=true    -Grankdir=TP -Tsvg -o $2


