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


### provTest1.rq

A testing query, no description yet. 



## Notes


```bash
curl  -XPOST  --header "Content-Type:application/sparql-query"  http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql -d@hasLicense.rq
```

## Snippets

```sparql
FILTER (
        ?type IN (schema:Person, schema:Organization, schema:CreativeWork, schemax:Person, schemax:Organization)
) .
```