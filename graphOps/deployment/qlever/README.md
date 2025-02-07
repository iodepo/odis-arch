# Qlever Test Instance

## About

This document describes the use of [qlever-control](https://github.com/ad-freiburg/qlever-control)
to work with the ODIS-OIH graph.

The pre-requisite for using this approach includes python and docker. Once satisfied, you
will need to:

```bash
pip install qlever
```

You will find extensive documentation at the GitHub repo above for the various
qlever commands. What follows is a short example using the ODIS resources and
configuration files.

Make sure the command ```qlever``` is now in your PATH variable. You may need
to modify your path variable to ensure it is.

First, create a working directory for the ODIS graph to live in on your system.
Call this anything you wish, here I will use ```odis-oih-graph```.

Then change directory, cd, into that new directory and run the
following commands from there.

```bash
wget http://ossapi.oceaninfohub.org/public/Qleverfile-odis
qlever -q Qleverfile-odis get-data         # Download the dataset
qlever -q Qleverfile-odis index            # Build index data structures for this dataset
qlever -q Qleverfile-odis start            # Start a QLever server using that index
qlever -q Qleverfile-odis ui               # Launch the QLever UI
```

The raw SPARQL endpoint should be on port 7019 if you wish to use your own
SPARQL client. See [GleanerIO Architype Tooling](https://github.com/gleanerio/archetype/blob/master/docs/tooling.md)
for some references to clients and other related tooling.

If you also ran the UI command, you should get

```
The QLever UI should now be up at http://localhost:8176 ...You can log in as QLever UI admin with username and password "demo"
```

and be able to see the UI on port 8176.

## Update Support

As of Nov 15, 2024, the following work:

```
INSERT DATA { ... }
DELETE DATA { ... }
INSERT { ... } WHERE { ... }
DELETE { ... } WHERE { ... }
```

## SPARQL Extensions

The following two extensions to QLever are of use.

[SPARQL plus Text](https://github.com/ad-freiburg/qlever/blob/master/docs/sparql_plus_text.md)

[Path Search Feature Documentation for SPARQL Engine](https://github.com/ad-freiburg/qlever/blob/master/docs/path_search.md)

## CLI Snippets

```bash
curl -s "http://workstation.lan:7001" -H "Accept: text/tab-separated-values" -H "Content-type: application/sparql-query" --data "SELECT * WHERE { ?s ?p ?o } LIMIT 10" ;

```

```bash
curl -s "http://workstation.lan:7001" -H "Accept: text/tab-separated-values" -H "Content-type: application/sparql-query" --data @./searchODIS/dataset.rq ;

```

```bash
curl -s "http://workstation.lan:7019?timeout=600s&access-token=odis_7643543846_6dMISzlPrD7i" -H "Accept: text/csv" -H "Content-type: application/sparql-query" --data "SELECT * WHERE { ?s ?p ?o  }" >  results.csv
```

## Notes

```
❯ qlever --qleverfile Qleverfile-odis ui --host-name workstation.lan

```

# Notes

```
 chmod o+w . && docker run -it --rm -v $QLEVER_HOME/qlever-indices/olympics:/index --entrypoint bash qlever -c "cd /index && xzcat olympics.nt.xz | IndexBuilderMain -F ttl -f -  -i olympics -s olympics.settings.json | tee olympics.index-log.txt"
```

```
PORT=7001; docker run --rm -v $QLEVER_HOME/qlever-indices/olympics:/index  -p $PORT:7001 -e INDEX_PREFIX=olympics --name qlever.olympics qlever
PORT=7001; docker run --rm -v $QLEVER_HOME/qlever-indices/olympics:/index -p $PORT:7001 --entrypoint bash qlever -i olympics --name qlever.olympics qlever
PORT=7001; docker run --rm -v $QLEVER_HOME/qlever-indices/olympics:/index -p $PORT:7001 -i olympics --name qlever.olympics qlever
```

qlever format: Accept: application/qlever-results+json
