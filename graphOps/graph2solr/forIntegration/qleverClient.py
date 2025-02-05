from SPARQLWrapper import SPARQLWrapper, JSON, CSV

# curl -s https://qlever.cs.uni-freiburg.de/api/wikidata -H "Accept: application/qlever-results+json" -H "Content-type: application/sparql-query" --data "SELECT * WHERE { ?s ?p ?o } LIMIT 1" | jq


# curl -s "http://workstation.lan:7001?timeout=600s&access-token=data_7643543846_Zs6nw7yi3Z9m" -H "Accept: text/tab-separated-values" -H "Content-type: application/sparql-query" --data "SELECT * WHERE { ?s ?p ?o }" >  results.tsv


# work with the SPARQL in odis-in for the various types.   So there will be pipeline for each type
# Read the results into polar and do any modifications needed on the results in polars.
# polars to JSONL and also into Parquet(?)

query = "SELECT * WHERE {?subject ?predicate ?object} LIMIT 100 "

URL4SPARQLENDPIOINT = "http://workstation.lan:7019/api/sparql"
sparql = SPARQLWrapper(URL4SPARQLENDPIOINT)
sparql.setQuery(query)
sparql.setReturnFormat(CSV)
results = sparql.query().convert()

# for result in results["results"]["bindings"]:
    # print(result)

print(results)
