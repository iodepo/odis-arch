# README

## References

* [Science on Schema](https://github.com/ESIPFed/science-on-schema.org//)
* [Ocean Best Practices on Schema](https://github.com/adamml/ocean-best-practices-on-schema)
* https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping
* https://resources.data.gov/resources/dcat-us/


## Notes

* ODISCat links are something we might be able to link via nanopubs


### SDG Linking

#### Refs

* [SDGs](http://www.ontobee.org/ontology/SDGIO?iri=http://purl.unep.org/sdg/SDGIO_00000000_)
* [SDG targets](http://www.ontobee.org/ontology/SDGIO?iri=http://purl.unep.org/sdg/SDGIO_00000001)
* [SDG indicators](http://www.ontobee.org/ontology/SDGIO?iri=http%3A%2F%2Fpurl.unep.org%2Fsdg%2FSDGIO_00000003)



Note, how would we do a link to a SDG (sustainable development goal)?
We could use [subjectOf](https://schema.org/subjectOf) like SOS did
for metadata below.  

```json
{
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
    "distribution": {
      "@type": "DataDownload",
      ...
    },
    "subjectOf": {
      "@type": "DataDownload",
      "name": "eml-metadata.xml",
      "description": "EML metadata describing the dataset",
      "encodingFormat": ["application/xml", "https://eml.ecoinformatics.org/eml-2.2.0"],
      "dateModified":"2019-06-12T14:44:15Z"
    }
  }
  ```