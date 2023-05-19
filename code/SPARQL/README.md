# SPARQL


## Index

### africa.rq

Searches all the countries in Africa for instances of the name in 
a object literial, this tends to be Keywords.  

It also searches via regex description.

### baseQuery.rq

Example full text index search against the Blazegraph Lucene index.

### countByKeyword.rq

Provide an ordered count of items associated with keywords.

### countByLicense.rq

Provide an ordered count of items associated with license information.

### countByOrg.rq

Provide an ordered count of items associated with organizational information.

### countByPred.rq

Provide an ordered count of items associated with vocabulary predicates.

### countBySpatial.rq

Provide an ordered count of items associated with spatial predicates.

### countByType.rq

Provide an ordered count of items associated with vocabulary types.


### countByTypeSet.rq

Provide an ordered count of items associated with vocabulary types associated with IOH thematic types.


### duplicationTest.rq

A first testing query to locate duplicates based on exact name matching.  This 
is more a placeholder for a more complex query but this does pull some actionable information. 

### ex1.rq

A testing query, no description yet. 


### freeTextExample.rq

A testing query, for searching the graph index. 


### lens3.rq

A testing query, no description yet. 


## Notes


[SPARQL Reference](https://www.w3.org/TR/sparql11-query/)

```bash
curl  -XPOST  --header "Content-Type:application/sparql-query"  --data-binary @hasLicense.rq  http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql 
```

You can also do ?format=json  or csv with these.   When you do that you can 
also then leverage the powerful jq tool with commands like

```bash
curl  -XPOST  --header "Content-Type:application/sparql-query"  --data-binary @countByLicense.rq  http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql\?format\=json | jq '.results.bindings[]'
```


Or, if you have the results already.

```text
cat results.json | jq '.results.bindings[] .s.value' 
```

which would look at all the elements _s_ in the bindings array and pull their value.
