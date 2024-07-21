# Local ODIS/OIH Graph Tooling

## About

A bit of code to pull down ODIS/OIH graph and load into a local triplestore for a more intensive query and use.

> Note: You will need a minimum of 7 to 10 Gb of
> free memory for oxigraph when you install the graph.  

Once you get [oxigraph](https://github.com/oxigraph/oxigraph) running, you can visit the built in UI at
http://localhost:7878/ .

## Commands

Download the graph files

```bash
 python odisClone.py download --source http://notimplemented.org --outputdir ./data
 ```

Load them to oxigraph on http://localhost:7878  (will make a flag)

```bash
python odisClone.py load  --sourcedir ./data
```

## TODO

- [ ] Update the script with help and command line options to remove the hard coded elements in there now (odisClone.py)
- [ ] Add schema alignment to the script (odisClone.py)
- [ ] Integrate AWS SPARQL client into the Docker compose file
- [ ] Option to stream directly into a triplestore
- [ ] Add information about parquet products

## Command line examples for oxigraph

Load an nquads file
```bash
curl -i  -X POST -H 'Content-Type:text/x-nquads' --data-binary @africaioc_release.nq  http://localhost:7878/store
```

Load several from a directory via bash
```bssh
for file in *; do [ -f "$file" ] && curl -i  -X POST -H 'Content-Type:text/x-nquads' --data-binary @$file  http://localhost:7878/store; done
```

Clean all data (DANGEROUS:  empties the triplestore to start fresh)
```bash
curl -i -X POST -H "Content-Type:application/sparql-update" -d "CLEAR ALL"   http://localhost:7878/update
```

## Notes on schema alignment

It is the nature of schema.org that both the _http://schema.org/_
and _https://schema.org/_ namespace are used.   At present
the graphs downloaded do not normalize to a single one.  

Due to this, your SPARQL queries can miss IRIs from the other
prefix.

To address this, I have coded a function to normalize the namespaces.
This is not currently in the code, but I have it elsewhere and I will 
add it.  

## Notes on SPARQL

If you load quads into the triplestore, you need to make sure you surround 
your patterns with

```sparql
graph ?g {
    ...
}
```

as seen below

query all named graphs, including the default graph
```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
prefix prov: <http://www.w3.org/ns/prov#>
PREFIX schema: <https://schema.org/>

SELECT DISTINCT ?s ?type ?name ?address ?description ?courseName ?location
WHERE {
    graph ?g {
        BIND(schema:Organization AS ?type)
        ?s rdf:type ?type .
        OPTIONAL { ?s schema:name ?name . }
        OPTIONAL { ?s schema:address ?address . }
        OPTIONAL { ?s schema:description ?description . }
        OPTIONAL {
            ?s schema:hasCourseInstance ?hasCourseInstance .
            ?hasCourseInstance schema:name ?courseName
        }
        OPTIONAL { ?s schema:location ?location . }
    }
}
```
 
If you are loading just triples with only a default graph, remove 
those elements.  

Query a default graph only
```sparql
PREFIX schema: <https://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?s ?type ?name ?address ?description ?courseName ?location
WHERE {
         BIND(schema:Organization AS ?type)
        ?s rdf:type ?type .
        OPTIONAL { ?s schema:name ?name . }
        OPTIONAL { ?s schema:address ?address . }
        OPTIONAL { ?s schema:description ?description . }
        OPTIONAL {
            ?s schema:hasCourseInstance ?hasCourseInstance .
            ?hasCourseInstance schema:name ?courseName
        }
        OPTIONAL { ?s schema:location ?location . }
 }
 ```


## References

SPARQL examples can be found in [ODIS-IN SPARQL](https://github.com/iodepo/odis-in/tree/master/SPARQL)

See [GleanerIO Archetype Tooling documentation](https://github.com/gleanerio/archetype/blob/master/docs/tooling.md)
