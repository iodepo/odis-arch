# DCAT Mapping


## ESRI meeting notes:

### Code of note

This is a simple python script that uses the pySHACL and 
the SHACL-AF mode to generate a new graph based on the 
transforms [dcat2schema.py](./dcat2schema.py).  It uses
this very simple testing 
shape: [dcatsdoOLD.ttl](./shapes/dcatsdoOLD.ttl)
to convert dcat:description to schema:description.  This is 
just a pipeline test to demonstrate the approach and 
explore if investing in building out all the required
NodeShapes is useful. 

It might also be useful to explore [SSSOM](https://mapping-commons.github.io/sssom/home/) 
as a tool in this process.  We could define the mapping in that,
and then  generate the SPARQL needed to 
perform the transformations.  

The process could also leverage the JSON-LD Framing approach to allow us
to pull out the elements from the source files that we want.  Based on those then
we can use SHACL AF or other process to generate out the triples we want. 


### Notes 

* DCAT-US: https://resources.data.gov/resources/dcat-us/
* ESRI data hub uses RSS and feeds various formats like DCAT via that.
Check out: https://datahub-dc-dcgis.hub.arcgis.com/search 
([ocean search](https://datahub-dc-dcgis.hub.arcgis.com/search?q=ocean) for example)

### Feed (RSS) References

* https://doc.arcgis.com/en/hub/content/federate-data-with-external-catalogs.htm 
* https://datahub-dc-dcgis.hub.arcgis.com/api/feed/rss/2.0 


Example JSON (DCAT)
https://datahub-dc-dcgis.hub.arcgis.com/data.json


### Command Notes

```bash
 curl https://datahub-dc-dcgis.hub.arcgis.com/data.json | pyshacl -s ../code/SHACL/dcatsdo.ttl -sf turtle -df json-ld -a -i none -f nt - 
 ```

```bash
curl https://datahub-dc-dcgis.hub.arcgis.com/data.json  | jsonld format  -q | rapper -c -i ntriples -I http://example.org/id/ -
```

