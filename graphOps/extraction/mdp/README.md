# Master Data Product 

## TODO

* [ ] Add the columns "completeness" and "accreditation" to the products  

### Temporal

The temporal coverage all comes from the "temporalCoverage".   We get the 
start, end dates and start end years from processing the temporalCoverage.    Need
to put this into the python time package and pull these and augment the temporal parquet

###  Geometry

Need to do apply the spatial functions to the filteredgeom

Need to apply Jeff's transforms


## About

This is a quick start for code to generate a "Master Data Product" from a 
provided OIH Release graph.  The graph needs to be in NQuads format and follow
the guidance from the OIH Book to express resources that align with the 
queries used.



## Code

* mdp_v2.py
  * Updated mdp using PyOxigraph and better processing
* oih_engine.py
  * Leverages the above and loops through the queries and sources to make products
* oih_processSpatial.py
  * flesh out the spatial elements
* oih_processTemporal.py
  * flesh out the temporal elements



* mdp.py
  * Original MDP, still more comprehensive in terms of pre-processing the data
* Morgue/objectProcessor.sh
  * BASH shell script to loop on items to make products from mdp, like oih_producer.py for mdp_v2.py




## Commands (new)

Indexing via the scheduling system for ODIS places the resulting summoned documents into 
the buckets _gleaner.oih/summoned/PARTNER_ with the generated graphs being placed in 
_gleaner.oih/graphs/latest/PARTNER_release.nq_ and _gleaner.oih/graphs/latest/PARTNER_prov.nq_ 

At established times these graphs are placed into prefix _commons/ODIS-KG-MAIN/18042024/_ where
the last item is the time stamp of the time the snapshot was made.  

From these graphs in the latest prefix, we can generate the resulting products via

```bash
 python mdp_v2.py  --source "s3://ossapi.oceaninfohub.org/commons/ODIS-KG-MAIN/18042024/cioos_release.nq"  --query "./queries/baseQuery.rq"  --output  "s3://ossapi.oceaninfohub.org/commons/OIH-PROD/18042024/cioos.parquet"
```

This both pulls from the ODIS object store and pushed the results back to the object store.  

The code _oih_producer.py_ is used to apply all queries to all objects in a given prefix.  



## DuckDB

DuckDB is used to query the products and generate pandas dataframes that are converted to JSON.

These are located in the ODIS-IN repository SQL directory. 


## Quickstart

> NOTE:  This program can take several minutes to run.  While it does attempt to provide
> feedback on progress, this can be slow also as it can only increment on query completion.
> Also, some of the dataframe transforms can be lengthy too.  

An example command will be like:

> NOTE:  A run for a graph the size of CIOOS takes around 4 to 5 minutes

```Bash
 python mdp.py  --source "s3://nas.local:49153/public/graphs/test1/africaioc_release.nq"  --output  "s3://nas.local:49153/public/assets/test1/testjan30.parquet"
```

```Bash
python mdp.py  --source "http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.nq"  --output "./output/cioos.parquet"
```

for s3 something like the following can be used assuming you have set the environment variables
 MINIO_ACCESS_KEY and  MINIO_SECRET_KEY.

```Bash
 python mdp.py  --source "s3://nas.local:49153/public/graphs/test1/africaioc_release.nq"  --output "./output/test.parquet"
```

Can now save to s3 as well:

```Bash
 python mdp.py  --source "s3://nas.local:49153/public/graphs/test1/africaioc_release.nq"  --output "s3://nas.local:54321/public/graphs/products/africaioc.parquet"
```

At present, I only support Parquet and CSV output based on the file extension.  

## mdp2solr.py

```Bash
python mdp2Solr.py --source ./output/cioos.parquet --outputdir ./output/solr
```

## MDP2Solr

```Bash
 python mdp2solr.py  --source "s3://nas.local:49153/public/assets/africaioc.parquet"  --output "./output/solr/
```

## Testing with Oxigraph

To test of the queries directly we want to be able to load up the RDF into Oxigraph (or your favorite triplestore) 
and test our queries there directly.


to load the graphs
```Bash
 curl -i -X PUT    -H 'Content-Type:text/x-nquads'    --data-binary @file.nq  http://localhost:7878/store
```

if you are using minio, you can cat the object directly into the triplestore

```Bash
mc cat nas/public/graphs/test1/africaioc_release.nq | curl -i -X PUT    -H 'Content-Type:text/x-nquads'    --data-binary @-  http://localhost:7878/store
```


to clear the graphs
```Bash
 curl -i -X POST -H "Content-Type:application/sparql-update" -d "CLEAR ALL"   http://localhost:7878/update
```


# Notes Related to Solr Dataset

## Thoughts

* One option is to do this as SPARQL into Pandas and then do changes there
* However, when cutting across all the different types and providers we might not
  have a common structure
  * Each type is likely a separate concern
  * Do a frame for each type

Then we know we have a common structure for each thematic type (Person, Course, Dataset, etc)
and we can likely map directly down in the dataframe from there without a query need.
This involves processing the JSON-LD documents, not the KG though.  The question is could this 
be done off the release graph rather than the JSON-LD objects.  It might be nicer.   

We could use the release graph, pull each named graph, convert to JSON-LD and frame.  

How is that process different than leveraging SHACL and in addition to validation, forming
a new set of triples that also could map directly into the data frame.

Indeed, both these approach seem to work when just thinking them through.  A few observations though:

* Framing is likely faster, though we can spread both across cores with Dask and other approaches
* SHACL might let us handle errors better and gives us shapes to test provider resources with.

First oder thought is:  try SHACL first.  

## About

Need to pull from the release graphs a parquet file with the elements from 
the graph to populate the items in the notes sections below.  


```python

###
#  Text address / name / CountryOfLastProcessing to Regions
#
# This is a super simple geocoder -- if there's text (in "address", 
# "name", or "CountryOfLastProcessing" properties) that contains
# a country that's spelled like the "geoAreaName" value from 
# the UNSD "GeoArea" API endpoint, we take the
# region from there. 

# For more on the UNSD API, see https://unstats.un.org/SDGAPI/swagger/
# and see the JSON results tree for the GeoArea endpoint at 
# https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/Tree
# We now connect through the live API, and get the list of all countries 
# and regions in JSON, which we then parse.  Formerly, we had to 
# manually download a CSV from 
# https://unstats.un.org/unsd/methodology/m49/overview

# Algorithim:
# * lower everything.
# * removing anything in parens e.g., we want Iran to match, not require
#   Iran(Islamic Republic of),
# * Remove stop words.
# * Split on whitespace
# * remove ending period e.g. we want "Ghana" from "Accra, Ghana."

# Then, for properties mentioned above, we check to see if any of the 
# countries are in the address, and map away from there.  Note, 
# Cote d'Ivoire and Timor Leste are going to potentially have accent issues.
#
# Note -- this is a linear search, but there are only 200 countries so it's not that bad.

```


