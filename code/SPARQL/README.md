# SPARQL

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