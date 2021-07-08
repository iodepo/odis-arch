# Documents

For OIH documents will scope more than datasets.   Documents will include maps, reports,
guidance and other creative works.  Due to this OIH will focus on a generic example
of [schema.org/CreativeWork](https://schema.org/CreativeWork) and then provide examples
for more focused creative work examples.

These will include initially;

* [https://schema.org/Map](https://schema.org/Map)
* [https://schema.org/Dataset](https://schema.org/Dataset) with guidance here likely to
  recommend following the [Science on Schema](https://science-on-schema.org) guidance under
  development at ESIP.
* [https://schema.org/Course](https://schema.org/Course)
  
Items not scoped above can be represented as a generic CreativeWork at this time. 
An example of a minimal description of such a resource would look like the following

[Load in JSON-LD Playground](https://json-ld.org/playground/#startTab=tab-expanded&json-ld=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/creativework.json)

[Load in Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool#url=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/creativework.json)


```{literalinclude} ./graphs/creativework.json
:linenos:
```

![Doc Guidance image](./graphs/creativework.svg)


## Maps

A map in this context would be a static file or document of some sort.  Map services like 
those described by an OGC Catalogue Service or other GIS service would be described as a 
service.  

Note, that in the current context, schema.org Map typically references maps a document.
Here we are likely to reference a KML, Shapefile or GeoPackage.  We may wish to then 
indicate the type of document it is through a mimetype via encoding.  

If this is related to a WFS, WMS or related service, it is likely we would then use the 
service description approach.  

A link to a minimal map creative work follows.


[Load in JSON-LD Playground](https://json-ld.org/playground/#startTab=tab-expanded&json-ld=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/map.json)

[Load in Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool#url=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/map.json)

<!-- embedme ./graphs/map.json -->
```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Map",
    "@id": "https://example.org/id/XYZ",
    "name": "Name or title of the document",
    "description": "Description of the map to aid in searching",
    "url":  "https://www.sample-data-repository.org/creativework/map.pdf"
}

```

![Doc Guidance image](./graphs/map.svg)

Note that at present the schema.org type Map only offers one special property beyond
the parent CreativeWork.  That is a [mapType](https://schema.org/Map) which is an
enumeration of types that do not apply to OIH use cases.  However, the use of the
Map typing itself may aid in narrowing search requests later to a specific creative work.


## Notes


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




### SDG Linking

#### Refs

* [SDGs](http://www.ontobee.org/ontology/SDGIO?iri=http://purl.unep.org/sdg/SDGIO_00000000_)
* [SDG targets](http://www.ontobee.org/ontology/SDGIO?iri=http://purl.unep.org/sdg/SDGIO_00000001)
* [SDG indicators](http://www.ontobee.org/ontology/SDGIO?iri=http%3A%2F%2Fpurl.unep.org%2Fsdg%2FSDGIO_00000003)



Note, how would we do a link to a SDG (sustainable development goal)?
We could use [subjectOf](https://schema.org/subjectOf) like SOS did
for metadata below.  

<!-- embedme ./graphs/doc.json -->

```json
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "@id": "https://example.org/id/XYZ",
  "name": "Name or title of the document",
  "description": "Description of the dataset to aid in searching",
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.sample-data-repository.org/dataset/472032.tsv",
    "encodingFormat": "text/tab-separated-values"
  },
  "subjectOf": {
    "@type": "DataDownload",
    "name": "eml-metadata.xml",
    "description": "EML metadata describing the dataset",
    "encodingFormat": [
      "application/xml",
      "https://eml.ecoinformatics.org/eml-2.2.0"
    ],
    "dateModified": "2019-06-12T14:44:15Z"
  },
  "maintainer" : {
     "@type" : "Organization",
     "@id": "https://link.to/PID_like_re3_or_others",
     "description": "Organization or Person who maintains the creative work"
  }
}
```

![Doc Guidance image](./graphs/doc.svg)
