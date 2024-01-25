# Depth

## Introduction

This document introduces approaches for the representation of depth in the
metadata to aid in the discovery and filtering of resources of interest based
on depth values.

## Scope

The scope of this work is related to the metadata and specifically
leverages schema.org and geoSPARQL vocabularies to do this encoding.

We will address two areas in the data model for the representation of depth.
One is that the depth is expressed in a variable measured.  The other than 
it is a spatial property on some geometry associated with the resource.

This can be spatial, like Place, or part of the measured variables both 
depending on whether the author is making a positioning claim or reporting a result. 

A resource might have multiple depth values, say min and max, with multiple
variables measured.  It might also then have some other depth associated with the
geometry or a spatial feature associated with the resource.  

### Depth Measurement


- For any depth measurements that are part of a dataset itself (i.e. not just in the metadata)
    - Use a variableMeasured stanza to describe the depth variables in your dataset, including the right semantic markup (See CODE BLOCK 2) 
      - The “right” semantic Markup means that the vocabulary, thesaurus, ontology or other DefinedTerm you use is defined exactly as you understand it / have used it in your description. If you disagree with the definition or elements of it, DO NOT use the term and search for an alternative in another trusted semantic resource. Using an undefined vocabulary term or a free text string is BETTER than using a defined term with a poor or inappropriate definition.
    - Include values for measurementTechnique and other properties, as we’re now talking about a variable actually in your dataset (rather than in the metadata about your dataset)

CODE BLOCK 2

```json
   "variableMeasured" : [
      {
           "@type": "PropertyValue",
           "name": "depth",
           "description": "Depth (spatial coordinate) relative to water surface in the water body. Definition: The distance of a sensor or sampling point below the sea surface",
           "propertyID": [
               "https://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/"
           ],
           "measurementTechnique": "description of technique used",
           "unitText": "m",
           "unitCode": [
               "https://qudt.org/vocab/unit/M",
               "https://vocab.nerc.ac.uk/collection/P06/current/ULAA/",
               "http://dbpedia.org/resource/Metre"
           ]
       },
]
```

Reference: [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/#example-60-expanded-value-with-type) with respect to the type above in the geosparql:asWKT node.

### Depth via schema.org

- schema.org:
  - In any @Place stanzas used in spatialCoverage and other properties (Keep in mind: Anything in a Place stanza is there to position the aboutness or relevance of your dataset to a particular place. This can be rougher than measured depth values
    - e.g. correlating temperature, salinity, depth) that are actually inside your data. For that, see variableMeasured advice above
  - Depth should be indicated by negative elevation values, which assume WGS84. The value syntax should be “[number] [unit]”, if unit is missing, it is assumed to be metres
  - If / when we figure out how to represent volumes with depth/elevation in GeoSPARQL, this would be included in the Place stanza


### Depth WKT Open GeoSpatial Consortium (OGC) Encoding

- WKT - GeoSPARQL
    - According to this documentation: [Well-known text - GIS Wiki | The GIS Encyclopedia](https://wiki.gis.com/wiki/index.php/Well-known_text)
        - POINT(1 3) is 2D, POINT Z(1 3 4) is now 3D
        - POINT ZM (1 3 4 5) or POINT M(1 3 5) is how you get in the 4D situation
        - Note: m' is 'measure' an extra axis of information not associated with the cartesian x/y/z space. The most common use for 'measure' is actually for 'measurements', the adding of physically known measurements about a feature to the abstract 'feature' represented in x/y space in the GIS. For example, highway management systems often understand the location of facilities in terms of 'mile posts'. So, in addition to x/y coordinates, each vertex is also assigned a 'mile' measurement in 'm' which allows the system to accurately place facility information relative to the 'milepost' system. (Why not just use the x/y coordinates and calculate distances off of them? Because they are representational, the distances calculated from the x/y will not be the same as the actual milepost measurements.)

        - You can use this for variants like LINE Z(), POLYGON Z() for things like trawls / cruise tracks and volumes

CODE BLOCK 1

```json

 {
   "@type": "Place",
   "geo": {
    "@type": "GeoCoordinates",
    "elevation": -1146.0,
    "latitude": 16.76203,
    "longitude": -25.10367
   }
  }
```

CODE BLOCK [x] - Marine Regions reference

```json
 {  
  "@context": { 
     "@vocab": "[https://schema.org/](https://schema.org/)", 
     "geosparql": "http://www.opengis.net/ont/geosparql#" 
   },
   "@type": "Place",
   "@id": "http://marineregions.org/mrgid/4252",
   "name": "Hudson Bay",
   "url": "https://www.marineregions.org/rest/getGazetteerRecordByMRGID.jsonld/4252/", 
   "geo": {
       "@type": "GeoShape",
        "url": "http://marineregions.org/mrgid/4252/geometries?source=25&attributeValue=16",
       "description": "The WKT value of this bay is HUGE. See https://marineregions.org/mrgid/4252/geometries.ttl?source=25&attributeValue=16",  
      "geosparql:asWKT": {
         "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POLYGON ((....))",
         "@type": "geosparql:wktLiteral"
       }
    }
  }
```

## Draft Guidance:


- For external references to geospatial metadata:
  - Best to import and add to your own JSON-LD, so you can validate before pushing to ODIS (don’t want an upstream error to corrupt an otherwise valid record)
  - Min max depth URL examples: http://vocab.nerc.ac.uk/collection/P01/current/MAXWDIST/ and http://vocab.nerc.ac.uk/collection/P01/current/MINWDIST/


## Appendix

### SOSA Example

Example from Adam Shepherd for SOSA, where depth is modeled as part of the FeatureOfInterest (note the xsd:float coming off of it alongside geo:lat, geo:lon)

![SOSA example](https://lh7-us.googleusercontent.com/2TnT7_1Doqlex23HQiS_p5jfurPzlHHfG606qK3avG17AxDrJ844tTHvBotQpkD_CI3EGfTMrbDUWD7UoLGK9oj1U1LeOGqtCr6HnkV_XGR11cwp24brFPpWnXvsj4Dc0hYGRviWIrOOGHY4e7TOga0)

### Links and Resources

- Example NERC term for depth: [NVS](http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/)   (Noted to be narrower than "depth")
- [Place - Schema.org Type](https://schema.org/Place)
- [PropertyValue - Schema.org Type](https://schema.org/PropertyValue) 
- [measurementTechnique - Schema.org Property](https://schema.org/measurementTechnique)
- [variableMeasured - Schema.org Property](https://schema.org/variableMeasured)
- Parameter search at BCO-DMO showing the various depth observations: [Parameter Search | BCO-DMO](https://www.bco-dmo.org/search/parameter/depth)
- [METS RCN Examples](https://github.com/NicoGEOMAR/METS-RCN/tree/main/Examples/Events)
- [elevation - Schema.org Property](https://schema.org/elevation) - expects a number and unit (“1000 m”)
- Still don’t know how to represent volumes with multiple depths in schema or GeoSPARQL
- Some work proposed for this [Extending the GeoSPARQL ontology with full-featured 3D support · Issue #19 · opengeospatial/ogc-geosparql · GitHub](https://github.com/opengeospatial/ogc-geosparql/issues/19) 

