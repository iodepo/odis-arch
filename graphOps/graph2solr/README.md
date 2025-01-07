# SOLR Ops

* Need to work on the spatial conversion to support both Solr and WIS2
  * look at the DuckOps_wis2.py
* Ref: /home/fils/scratch/qleverflow/configs/TESTnq
* Ref: /home/fils/scratch/solr/solr-8.11.2


addup.py  should be able to do add[bulk] and update
ref: https://claude.ai/chat/9fe1c04f-7d90-465a-98a2-34b237ed7e42


```
OIH Knowledge Graph -----  via SPARQL ----------> csv
csv ---------------------- via DuckBD ----------> results_grouped.csv
results_grouped.csv------- via csv2jsonl.py ----> solrinput.jsonl
solrinput.jsonl ---------- via processor.sh ----> solr
```


The steps addup.py needs to do.

1) the SPARQL query (should it go to lance at this point?)
2) duck query to group by out of the lance arror (into a new table in the database?) (duckquery.py and aggtest3.py are likely the latest to look at for source)
3) at this point convert it to JSON-L  (also save into lance, or to files?   both, likely) (csv2jsonl.py is the code to look at for this)
4) load into Solr (bulk and single record)


## Notes & References

> for duckdb step see
> https://lancedb.github.io/lancedb/python/duckdb/
> and
> https://duckdb.org/2021/12/03/duck-arrow.html

## Starting Solr

```
./bin/solr start -e schemaless
```

Then visit: http://localhost:8983/solr

Delete all records:
```
curl -X POST 'http://localhost:8983/solr/gettingstarted/update?commit=true' -H 'Content-Type: application/json' -d '{"delete": {"query": "*:*"}}'
```

## Sheets

Term list

https://docs.google.com/spreadsheets/d/1pVYNt4IATmpG73MMk30GlvW70K0zl7IvAgnZn-oj58U/edit?gid=0#gid=0

## time run

~ 6.5 hours to load in single file mode
~ 32 seconds in 1K batch mode

Line 592331 uploaded successfully.
Finished processing 592331 lines from ./stores/solrInputFiles/sparql_results.jsonl
python graph2solr.py table --source dfdfd --sink sdsdsdsd   1080.28s  user 152.43s system 5% cpu 6:35:44.85 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                193 MB
page faults from disk:     0
other page faults:         27471

Num Docs:274923
Max Doc:274924


## A run examples

> Note, qlever needs to be running as well as a Solr instance

```
python graph2solr.py query --source  "http://0.0.0.0:7019" --sink "./stores/files/results_sparql.csv" --query "./SPARQL/baseQuery.rq"  --table "sparql_results"

python graph2solr.py group --source "sparql_results" --sink './stores/files/results_long_grouped.csv'

python graph2solr.py jsonl --source "sparql_results_grouped"

python graph2solr.py table --source "./stores/solrInputFiles/sparql_results_grouped.jsonl" --sink "http://localhost:8983/solr/gettingstarted/update?commit=true"
python graph2solr.py batch --source "./stores/solrInputFiles/sparql_results_grouped.jsonl" --sink "http://localhost:8983/solr/gettingstarted"
```

# Notes

* Date to ISO date, so 2023 become 2023-01-01
* I can either select first in SQL or limit 1 in SPARQL for things like datePublished and dateModified (since they
  don't seem to be things that can be lists)
* Note, imposing the dtype in the graph is better than alignment after the fact from an AI readiness point of view