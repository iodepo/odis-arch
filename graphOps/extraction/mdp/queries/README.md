# README

## About

Directory for SPARQL queries associated with the OIH Solr UI

## Align with UI views

Look at the views in /home/fils/src/Projects/OIH/oih-ui/frontend/src/components/results/types
and make sure the queries address this elements.

## Notes

* need a SHACL test for URL that looks for the http pattern
* a sameAs points to URL, which might be text or IRI or blank.
* citation is TXT or CreativeWork

```regexp
^(https?|http):\/\/[^\s/$.?#].[^\s]*$
```

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


