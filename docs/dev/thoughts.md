# Notes


## References


* [Science on Schema](https://github.com/ESIPFed/science-on-schema.org//)
* [Ocean Best Practices on Schema](https://github.com/adamml/ocean-best-practices-on-schema)
* https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping
* https://resources.data.gov/resources/dcat-us/



## People and Institutions

### Ref
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
  

## Documents

### Ref
* For dataset we can use [SOS Dataset](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md)
  
For other document these are likely going to be some https://schema.org/CreativeWork with there being many subtypes we can explore.   See also here Adam Leadbetter's work at https://github.com/adamml/ocean-best-practices-on-schema

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



### Ref

* https://schema.org/Project
  

### Questions
* are these reseach projects?
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
