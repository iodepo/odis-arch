# Notes

## About

Some notes related to elements to integrate.

## Search criteria  

At present there are discussions about search criteria.

* search by type:  basic type search implemented in the SPARQL
* region:  search by location baed on spatial or address elements.  We might be able to do this
by leveraging the "org" graph being generated and ensuring that spatial elements are associated 
with that organization (geolocation, lat long, various region names.)
    * This also relates to IHO sea region assignment via point in poly example 
* date range search (requires xsd:dateTime)


## Authoritative Source approach

Resources need to be able to declare the authoritative source for a reference.  This is not
directly provenance and likely address by the schema.org/author property.  This property
works at present on CreativeWork or Rating and should connect a Person or Organization.

## DCAT aware

Need to address approaches for how to make the OIH search DCAT aware as we will be getting a lot 
of material from CKAN and DKAN leveraging DCAT.  This could be done with apply the rules to the 
triplestore based on the published crosswalks.  

### Refs

* https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping

## Licensing

### Ref

* https://schema.org/license 

## Language examples

>> Need to note an issue on this in the repo as a multilingual gap in the current approach. 

JSON-LD supports a (language indexing)[https://json-ld.org/spec/latest/json-ld/#language-indexing].  This can be used as follows.

* @none is used for data with no language
* @set is used when compacting the document and ensure the elements are in array form

```json

{
  "@context": {
    "vocab": "http://example.com/vocab/",
    "label": {
      "@id": "vocab:label",
      "@container": ["@language", "@set"]
    }
  },
  "@id": "http://example.com/queen",
  "label": {
    "en": "The Queen",
    "de": [ "Die Königin", "Ihre Majestät" ],
    "@none": "The Queen"
  }
}
```

## Controlled vocabulary list

This could be done by a schema.org/ListItem with links to the controlled vocabulary.  There is also
https://schema.org/courseMode and https://schema.org/code (only on medical entry for now)

## Date

Schema.org expects the date to be in ISO 8601 format, which allows both variants (with and without time zone). 
As they don’t give any further restrictions, specifying the time zone (of your choice) is optional.

### Ref

* https://www.w3.org/TR/2014/REC-html5-20141028/text-level-semantics.html#attr-time-datetime
* https://schema.org/startDate 
* https://schema.org/temporalCoverage 

We cab push the xsd:dateTime through context via

```json
{
  "@context": {
    "ical": "http://www.w3.org/2002/12/cal/ical#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ical:dtstart": {
      "@type": "xsd:dateTime"
    }
  },
  "ical:summary": "Lady Gaga Concert",
  "ical:location": "New Orleans Arena, New Orleans, Louisiana, USA",
  "ical:dtstart": "2011-04-09T20:00:00Z"
}
```

This is needed in order to support proper SPARQL date range queries. 


