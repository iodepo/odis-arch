# Shapes

## About

Need to sync / coordinate with the 
[Geoshapes](https://github.com/geoschemas-org/geoshapes) repository.


## Example use

The following command will pull a release graph from the OIH system and process it via a SHACL shape 
stored in GitHub.  This could also be used with various packages to generate reports like seen 
at [odis validation](https://github.com/iodepo/odis-arch/tree/schema-dev-df/workflows/output/validation) and
PDFs such as this [example report](https://github.com/iodepo/odis-arch/blob/schema-dev-df/workflows/output/validation/report_02-23-2023-06-46-07.pdf).
The details are then found in an [associated CSV document](https://github.com/iodepo/odis-arch/blob/schema-dev-df/workflows/output/validation/validationReport_02-23-2023-06-46-07.csv)


```bash

curl http://ossapi.oceaninfohub.org/public/graphs/summonedafricaioc_v1_release.rdf |   pyshacl -s https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/SHACL/oih_search.ttl -sf turtle -df n3 -f table -

```

## Resources

* [pySHACL](https://github.com/RDFLib/pySHACL)

## Examples

```bash

curl http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.rdf |   pyshacl -s https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/code/SHACL/typesAreURI.ttl -sf turtle -df n3 -f table -

```