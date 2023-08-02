# Validation workflow

# example command

```bash
python validationReport.py -d http://ossapi.oceaninfohub.org/public/graphs/summonedafricaioc_v1_release.nq -s https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/SHACL/oih_search.ttl -n oihsearch
```

```bash
❯ python validationReport.py -a ALL -s https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/SHACL/oih_search_http.ttl -n oihsearch
```



```bash
 pyshacl -s ../../../code/SHACL/oih_search.ttl -sf turtle -df nt -f human ./test.nt | grep -i "description missing" | wc -l

```
