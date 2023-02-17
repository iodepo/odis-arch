# SPARQL

## Notes

Count clip for Africa query

```text
regex: 6175
literal: 1679
combined 7854

8014
Run time:  1min, 33sec, 463ms	 

```

```bash
curl -v  -XPOST  --header "Content-Type:application/sparql-query"  http://graph.oceaninfohub.org/blazegraph/namespace/oih/sparql -d@africa.rq
```

## Snippets

```sparql
       FILTER (
        ?type IN (schema:Person, schema:Organization, schema:CreativeWork, schemax:Person, schemax:Organization)
        ) .
```