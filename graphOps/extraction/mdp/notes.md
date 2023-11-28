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

## Notes

Here are the keys extracted from the provided JSON:

- id
- type
- txt_creator
- txt_dateModified
- txt_datePublished
- description
- txt_distribution
- id_includedInDataCatalog
- txt_includedInDataCatalog
- txt_keywords
- txt_license
- name
- id_provider
- txt_provider
- id_publisher
- txt_publisher
- geom_type
- has_geom
- geojson_point
- geojson_simple
- geojson_geom
- geom_area
- geom_length
- the_geom
- dt_startDate
- n_startYear
- dt_endDate
- n_endYear
- txt_temporalCoverage
- txt_url
- txt_variableMeasured
- txt_version
- index_id
- _version_
- indexed_ts
- json_source

These are all the keys present in the JSON object you provided.


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