#1/bin/bash

# jsonld format -q sos.jsonld | rapper -i nquads -o dot -I https://science-on-schema.org/ - | dot -Grankdir=TP  -Tsvg -o sos.svg
# find ./docs/dev/ -name "*.json"

mc_cmd() {
        find $1 -name "*.json"
}

# If you use this for ntriples, be sure to add in a graph in the URL target
for i in $(mc_cmd $1); do
    filename=${i##*/}     # file.zip
    directory=${i%/*}     # /stuff/backup
    basefilename=${filename%%.*}

    echo "converting $i to $directory/$basefilename.svg"

    jsonld format -q $i | \
        rapper -q -i nquads -o dot -I https://iode.org/ - | \
        sed - -e 's/https:\/\/schema.org\//schema\:/g' |   \
        sed - -e 's/http:\/\/www.w3.org\/1999\/02\/22\-rdf\-syntax\-ns\#type/rdfs\:type/g' | \
        sed - -e 's/http:\/\/www.w3.org\/2001\/XMLSchema\#/XMLSchema\#/g' | \
        # dot  -Estyle=dotted -Gsplines=true -Grankdir=TP  -Tsvg -o $2
        neato -Goverlap=false -Estyle=dotted -Gsplines=true    -Grankdir=TP -Tsvg -o $directory/$basefilename.svg

done


