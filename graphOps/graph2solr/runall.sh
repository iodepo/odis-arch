#!/bin/bash
## Do I need to remove the lancedb each time too?

curl -X POST 'http://localhost:8983/solr/gettingstarted/update?commit=true' -H 'Content-Type: application/json' -d '{"delete": {"query": "*:*"}}'
python graph2solr.py query --source  "http://0.0.0.0:7019" --sink "./stores/files/results_sparql.csv" --query "./SPARQL/SPARQL_q1.rq"  --table "sparql_results"
python graph2solr.py group --source "sparql_results" --sink './stores/files/results_long_grouped.csv'
python graph2solr.py augment --source "sparql_results_grouped"
python graph2solr.py jsonl --source "sparql_results_grouped_augmented"
python graph2solr.py batch --source "./stores/solrInputFiles/sparql_results_grouped_augmented.jsonl" --sink "http://localhost:8983/solr/gettingstarted"
