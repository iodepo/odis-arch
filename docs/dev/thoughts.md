# Notes



### ODIS Cat links

Maybe address this through some of the prov nanopub approaches in gleaner.

## References

* [Science on Schema](https://github.com/ESIPFed/science-on-schema.org//)
* [Ocean Best Practices on Schema](https://github.com/adamml/ocean-best-practices-on-schema)
* https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping
* https://resources.data.gov/resources/dcat-us/

## People and Institutions

### Refs

* https://schema.org/Person
* https://schema.org/Organization

For institution see also the projects section below.  Note that in Organization there 
many specific types we can use at the bottom.

```json
{
  "@context": "http://schema.org/",
  "@type": "Person",
  "name": "Jane Doe",
  "jobTitle": "Professor",
  "telephone": "(425) 123-4567",
  "url": "http://www.janedoe.com"
}
```

### Ref
* https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/DataRepository.md
  
## Documents and Best Practices

Thematic section on documents and best practices.  

This would scope:

* services that allow searching on these stores
* The documents themselves
* perhaps just the repository itself
* when we talk DC..  are we talking DC in JSON-LD or mapped to schema.org

Could use Org -> provides service

### Refs

* For dataset we can use [SOS Dataset](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md)
* OBPS group is using JericoS3 API (ref:  https://www.jerico-ri.eu/)
  * Traditional knowledge points here
  * sounds like they use dspace  
* For other document these are likely going to be some [schema:CretiveWork](https://schema.org/CreativeWork) with there being many subtypes we can explore.   See also here Adam Leadbetter's work at [Ocean best practices](https://github.com/adamml/ocean-best-practices-on-schema)
  * This is a great start and perhaps helps to highlight why SHACL shapes are useful
  * https://irishmarineinstitute.github.io/erddap-lint/ 
  * https://github.com/earthcubearchitecture-project418/p419dcatservices/blob/master/CHORDS/DataFeed.jsonld
*[EMODnet](https://emodnet.eu/en)  (Coner Delaney)
  * ERDAP also
  * Are we talking links from schema.org that link to OGC and ERDAP services 
  * Are these methods?  
  * Sounds like may link to external metadata for interop they have developed in the community
* NOAA connected as well
  * Interested in OGC assets  
  * ERDAP data platform

## Training

Start with https://schema.org/Course

```json
{
  "@context": "https://schema.org/",
  "@type": "Course",
  "description": "In this course you will get an introduction to the main tools and ideas in the data scientist's toolbox...",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": ["MOOC","online"],
    "endDate": "2019-03-21",
    "startDate": "2019-02-15"
  }
}
```

```json
{
  "@context": "https://schema.org/",
  "@type": "Course",
  "courseCode": "F300",
  "name": "Physics",
  "provider": {
    "@type": "CollegeOrUniversity",
    "name": "University of Bristol",
    "url": {"@id": "/provider/324/university-of-bristol"}
  }
}
```

## Spatial

See https://github.com/ESIPFed/science-on-schema.org/issues/105

```json
{
    "@context": {
        "@version": 1.1,
        "geoblob": {
            "@id": "http://example.com/vocab/json",
            "@type": "@json"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "description": "http://igsn.org/core/v1/description",
        "geosparql": "http://www.opengis.net/ont/geosparql#",
        "schema": "https://schema.org/"
    },
    "@id": "https://samples.earth/id/do/bqs2dn2u6s73o70jdup0",
    "@type": "http://igsn.org/core/v1/Sample",
    "description": "A fake ID for testing",
    "schema:subjectOf": [
        {
            "schema:url": "https://samples.earth/id/do/bqs2dn2u6s73o70jdup0.geojson",
            "@type": "schema:DigitalDocument",
            "schema:format": [
                "application/vnd.geo+json"
            ],
            "schema:conformsTo": "https://igsn.org/schema/spatial.schema.json"
        }
    ],
    "geosparql:hasGeometry": {
        "@id": "_:N98e75cacc29f40deb555eb583cb162dc",
        "@type": "http://www.opengis.net/ont/sf#Point",
        "geosparql:asWKT": {
            "@type": "http://www.opengis.net/ont/geosparql#wktLiteral",
            "@value": "POINT(-76 -18)"
        },
        "geosparql:crs": {
            "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
    },
    "geoblob": {
        "type": "GeometryCollection",
        "geometries": [{
            "type": "Point",
            "coordinates": [-76, -18]
        }]
    },
    "schema:spatialCoverage": {
        "@type": "schema:Place",
        "schema:geo": {
          "@type": "schema:GeoCoordinates",
          "schema:latitude": -18,
          "schema:longitude": -76
        }
      }
}
```


## Vessels

Sadly vessel is taken at schema.org for an entirely different "thing".  

## Projects

What defines a project?  From Schema.org:

> An enterprise (potentially individual but typically
> collaborative), planned to achieve a particular aim. Use properties from
> Organization, subOrganization/parentOrganization to indicate project sub-structures.

### Functional interest

* find collaborators
* find project gaps
* who funds what (semantic grouping)
* find duplications of funding (who is doing things already done)
* ID regional trends (what is important where) and then compare and contrast

### Notes

* [EurOcean](http://www.kg.eurocean.org/)
  * National projects in native languages
  * Use: [SeaDataNet](https://www.seadatanet.org/Metadata)
    * https://imdis.seadatanet.org/content/download/122068/file/2_1_IMDIS_2018_submission_61.pdf
    * https://www.rd-alliance.org/group/research-metadata-schemas-wg/wiki/enabling-global-data-discovery-through-structured-data
  * They have to deal with no common structure among the databases for descriptions
  * Set of fields have been aligned on with IDs
  * keywords to identify marine projects
  * Relationship with CORDIS
  * Understand the unit of knowledge being developed that can be transferred
    * How to describe unit of knowledge (ref: http://www.kg.eurocean.org/KOs)
* [ODIDO](http://www.ioc-africa.org/projects)
  * Set of parameters defined
    * Project Name
    * Country
    * Funds Source
    * Executing Agency
    * Focal Area
    * Start Date
    * End Date
    * Contact
    * Total Grant
    * Thematic Areas
    * Website
    * LME Region
    * Lead Implementing Agency
  * Current UI is a list.  Needs a way to ensure this can be crawed as a collection
    * Leverage https://schema.org/ItemList on a master index list page
* How many resources have spatial coverage
* What went in (people, funds, etc) and output (kg docs, etc)

### Ref

* https://schema.org/Project
  
### Questions

* Are these reseach projects?
  * https://schema.org/FundingAgency
  * https://schema.org/ResearchProject
* As distinct from institution above, correct?

I've used research project:  https://opencoredata.org/id/csdco/res/YUFL

## SDG Linking

### Refs

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

## Services

* https://schema.org/docs/actions.html
* https://schema.org/Action
* https://www.w3.org/TR/web-share/
* https://www.hydra-cg.com/spec/latest/core/

The graph describes a service than can be invoked with

```bash
curl --data-binary "@yourfile.jpg" -X POST https://us-central1-top-operand-112611.cloudfunctions.net/function-1
```

This with POST a jpeg to the service and get back a simple text response with some information 
about the image.

```json
{
  "@context": "http://schema.org/",
  "@type": "Action",
  "@id": "https://us-central1-top-operand-112611.cloudfunctions.net/function-1",
  "result": {
    "@type": "DataDownload",
    "encodingFormat": "text/plain",
    "description": "a simple text result for the RGB counts"
  },
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://us-central1-top-operand-112611.cloudfunctions.net/function-1",
    "httpMethod": "POST",
    "contentType": ["image/jpeg", "image/png"]
  },
  "object": {
    "@type": "ImageObject",
    "description": "A JPEG or PNG to analyze the RGB counts"
  }
}
```
