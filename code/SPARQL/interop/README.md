# Interoperable

## About

queries to support graph interoperability
* unique predicates and counts
* unique types and counts
* spatial elements
* temporal elements
* variableMeasured
* PIDs (doi and orcid)  limited by identifier
  * We limit by use in schema:identifier  (with limit: 913  without: ?? )

## Query References

The following are SPARQL queries that can be found at [odis-arch/code/SPARQL/interop](https://github.com/iodepo/odis-arch/tree/schema-dev-df/code/SPARQL/interop)

### Count By License

Number of resources with a license declared 

### DOIs

Number of resources with a DOI declared 


### ORCIDSs

Number of resources with an ORCID declared 


### Count by Spatial

Number of resources with geoSPARQL or schema.org properties
associated with spatial information


### Count by Temporal

Number of resources with temporal information.  At presnt this 
is just schema:endDate and schema:startDate but this will be 
expanded.

### Types and Type by defined set

Counts of the types used in the OIH patterns. 

### Count by Predicates

Count and name of all predicates used

### Count by Variable Measured

Count and name of all schema:variableMeasured used


## CLI Snippets

```bash
curl -s -XPOST  --header "Content-Type:application/sparql-query" --data-binary  @countByLicense.rq  "http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql?format=json"  | jq .results.bindings  | jq -r -L. 'include "json2csv"; json2csv' -
```

```bash
 curl -s -XPOST  --header "Content-Type:application/sparql-query" --data-binary   @countByTypeSet.rq  "http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql?format=json"  | jq .results.bindings  | jq -r -L. 'include "json2csv"; json2csv' -
```

Note with the Python package csv2md you can make this markdown too.

```bash
curl -s -XPOST  --header "Content-Type:application/sparql-query" --data-binary   @countByTypeSet.rq  "http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql?format=json"  | jq .results.bindings  | jq -r -L. 'include "json2csv"; json2csv' - | csv2md
```

## Snippets


```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?o
WHERE {
  ?s ?p ?o .
  FILTER (datatype(?o) = xsd:dateTime)
}

```

The following won't work, but perhaps a Blazegraph issue?
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?o
WHERE {

  ?s rdf:type ?type
   FILTER ( ?type IN (schema:ResearchProject, schema:Project, schema:Organization, schema:Dataset, schema:CreativeWork, schema:Person, schema:Map, schema:Course, schema:CourseInstance, schema:Event, schema:Vehicle) )
  ?s ?p*  ?o .
  FILTER (datatype(?o) = xsd:dateTime)
}
```



### Property Paths

Ref:  https://www.w3.org/TR/sparql11-property-paths/ 

```SPARQL
SELECT DISTINCT ?o
WHERE {
  ?s ?p* ?o .
}

```

This query will find all distinct objects ?o connected to a given 
subject ?s through any number of predicates ?p. Keep in mind that 
depending on the size and complexity of your dataset, such a query 
could be computationally expensive and may take a considerable amount 
of time to execute.

If you want to limit the path length, you can use the Kleene 
plus (+) or specify a range by using curly braces {}:


```SPARQL
# Using Kleene plus (+) to find paths with at least one predicate
SELECT DISTINCT ?o
WHERE {
  ?s ?p+ ?o .
}

# Limiting the path length to a specific range (e.g., 1 to 3 predicates)
SELECT DISTINCT ?o
WHERE {
  ?s ?p{1,3} ?o .
}

```

The Kleene plus (+) ensures that there is at least one predicate in the 
path, while the curly braces {} allow you