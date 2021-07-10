# Spatial

## About

The primary OIH guidance will be to use the OGC [GeoSPARQL](https://www.ogc.org/standards/geosparql)
vocabulary.  The schema.org spatial types and propeties are not well defined and difficult at times
to reliably translate to geometries.  

## Simple GeoSPARQL WKT

This is a simple example of how to embed a WKT string via GeoSPARQL into a record.

```{literalinclude} ./graphs/basic.json
:linenos:
```
## Classic Schema.org


Is is a simple example of the existing Schema.org pattern for a lat long value.  
This pattern is of little use other than perhaps to Google. 

```{literalinclude} ./graphs/sos.json
:linenos:
```

![SOS Guidance image](./graphs/sos.svg)


## Option review, SOS Issue 105

From the referenced SOS issue 105:

```{literalinclude} ./graphs/issue105.json
:linenos:
```



![Issue 105](./graphs/issue105.svg)


## References
* [Science on Schema Issue 105](https://github.com/ESIPFed/science-on-schema.org/issues/105)
  * Leverages [subjectOf](https://schema.org/subjectOf) to connect to a Thing / CreativeWork
* [https://www.unsalb.org/](https://www.unsalb.org/)
* [https://www.un.org/geospatial/](https://www.un.org/geospatial/)
* [schema.org/spatial](https://schema.org/spatial)
* [schema.org/GeospatialGeometry](https://schema.org/GeospatialGeometry)
* SOS patern follows:
  * [spatialCoverage](https://schema.org/spatialCoverage) -> [Place](https://schema.org/Place) -> [geo](https://schema.org/geo) -> [GeoCoordinates](https://schema.org/GeoCoordinates) OR [GeoShape](https://schema.org/GeoShape)
* Some groups are using [GeoNode](geonode.org)
  * [schema.org issues](https://github.com/GeoNode/geonode/issues?q=schema.org)
* OIH is not a spatial server, but will attempt to:
  * parse spatial data from the graph. This information will likely be fed into [Koop](koop.js) where it can be accessed and pulled by participants.
  * Feed the data into a spatial aware triplestore (GeoSPARQL)
* [ICAN & Schema.org](https://docs.google.com/document/d/1Ya7SNm0h6b04nIVMQ_M65LopxZ6_jojXzTxjfaX5Mxw/edit)
* [OGC SELFIE](https://www.ogc.org/projects/initiatives/selfie)
* [Think broad](https://docs.google.com/presentation/d/1HhuL73g1Bi_d86yT9VGfhvO0Xef9nKhJVwEeRYZ9k0c/edit#slide=id.ga724934615_3_0)
* Science on Schema [spatial for dataset guidance](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#spatial-coverage)
