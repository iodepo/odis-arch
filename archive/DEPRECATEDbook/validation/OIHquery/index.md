# OIH Query

## About

This section describes both current OIH query in SPARQL and also the related SHACL shape 
that can be used to validate a resources alignment to the query.



```SPARQL
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX con: <http://www.ontotext.com/connectors/lucene#>
PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
PREFIX schemaold: <http://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#
SELECT DISTINCT ?s  ?wat ?orgname ?domain ?type ?score ?name ?url ?lit ?description ?headline
WHERE
{
   ?lit bds:search "coral reef management" .
   ?lit bds:matchAllTerms "false" .
   ?lit bds:relevance ?score .
   ?lit bds:minRelevance "0.30" .
   graph ?g {
    ?s ?p ?lit .
    FILTER isIRI(?s)
    ?s rdf:type ?type . 
    OPTIONAL { ?s schema:name ?name .   }
    OPTIONAL { ?s schema:headline ?headline .   }
    OPTIONAL { ?s schema:url ?url .   }
    OPTIONAL { ?s schema:description ?description .    }
  }
   ?sp prov:generated ?g  .
   ?sp prov:used ?used .
   ?used prov:hadMember ?hm .
   ?hm prov:wasAttributedTo ?wat .
   ?wat rdf:name ?orgname .
   ?wat rdfs:seeAlso ?domain
}
ORDER BY DESC(?score)  ?name
LIMIT 30
OFFSET 0
```

