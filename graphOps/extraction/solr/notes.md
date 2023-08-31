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