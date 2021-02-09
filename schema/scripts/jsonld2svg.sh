#!/bin/bash
#
# Note this script requires json-dl, rapper, sed and graphviz
#  jsonld.js https://github.com/digitalbazaar/jsonld.js
#  rapper http://librdf.org/raptor/rapper.html
#  sed https://www.gnu.org/software/sed/manual/sed.html  (sed is rather standard in UNIX systems)
#  graphviz https://graphviz.org/
#
# useage
# ./jsonld2scg ./dir/to/search/from
#
# notes
# there are two graph options, dot and neat.  dot gives a more
# top down directed graph like result and neato more a "true" graph like layout.
# I'm not sure which I like more, they each have virtues and vices. 
#
# refs
# https://www.w3.org/2018/09/rdf-data-viz/ is old but has some nice information
#

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
        dot  -Estyle=dotted -Gsplines=true -Grankdir=LR  -Tsvg -o $directory/$basefilename.svg
        # neato -Goverlap=false -Estyle=dotted -Gsplines=true    -Grankdir=TP -Tsvg -o $directory/$basefilename.svg

done


