# Depth - (DRAFT)

## Introduction

This document, in draft form,  presents approaches for the representation of depth in schema.org and
gepSPARQL, via WKT, to aid in the discovery and filtering of resources of interest based
on depth.  


## Scope

The goal is to provide guidance to publishers of metadata records focused on the representation of
depth and elevation values that can be used for the discovery and filtering of metadata records. 

> It should be noted this is not focused on the representation of depth/elevation in data records, which is more
> a focus of each given domain.  It is a way to represent those values in the metadata.  

We will address two areas for the representation of depth.
Depth can be spatial, like Place, or part of the measured variables both
depending on whether the author is making a positioning claim or
reporting a result.

So these two approaches can be summarized as:

1) Where depth is a spatial property on some geometry associated with the resource.
2) Where depth is expressed in a variable measured.

Note that a resource might have multiple depth values, say min and max, with multiple
variables measured.  It might also then have some other depth associated with the
geometry or a spatial feature associated with the resource.


### Depth WKT Open GeoSpatial Consortium (OGC) Encoding

For more precise representation of spatial information, it is recommended to use the 
[OGC geoSPARQL standard](https://www.ogc.org/standard/geosparql/).  This approach leverages
Well Known Text (WKT) for the geometry.  While it is more common to see WKT used to represent 
geometry in two dimension such as:

```text
POINT (0 0)

LINESTRING (0 0, 0 1, 1 2)

POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))

MULTIPOINT ((0 0), (1 1))

MULTILINESTRING ((0 0, 1 1), (2 2, 3 3))

MULTIPOLYGON (((1 1, 1 3, 3 3, 3 1, 1 1)), ((4 3, 6 3, 6 1, 4 1, 4 3)))
```

There are approaches to representing both elevation, Z, and measurement, M.  

For the Z value an example for POINT would be:

```text
POINT Z (longitude latitude elevation)
```

In the Well-Known Text (WKT) format, the "M" in "POINT M" represents a linear referencing system or a measure value associated with the point geometry. The M value is an additional coordinate used to store a measurement or linear reference along a linear geometry like a line or curve. For points, the M value can represent things like:

* Distance along a path or route
* Time value
* Any other linear measurement or attribute

The format for representing a point with an M value in WKT is:

```text
POINT M (x y m)
```


There is also a 4D representation that includes a measurement M. M is 'measure' an extra axis of information not associated with the cartesian x/y/z space. The most common use for 'measure' is actually for 'measurements', the adding of physically known measurements about a feature to the abstract 'feature' represented in x/y space in the GIS.  This can be seen as:

```text
POINT ZM (longitude latitude elevation depth)
```

For other geometry types like LineString, Polygon, etc., you can follow a similar pattern by including the Z or M values after each coordinate pair. For example, a 3D LineString:

```text
LINESTRING Z (lon1 lat1 elev1, lon2 lat2 elev2, ...)
```


A simple point reference

```json
{
    "@context": {
        "@vocab": "https://schema.org/",
        "geosparql": "http://www.opengis.net/ont/geosparql#" 
    },
    "@id": "https://example.org/id/XYZ",
    "@type": "Dataset",
    "name": "Data set name",
    "spatialCoverage": {
        "@type": "Place",
        "geo":  
            {
                "@type": "GeoShape",
                "url": "http://marineregions.org/mrgid/4252/geometries?source=25&attributeValue=16",
                "description": "an example POINT Z entry",  
                "geosparql:asWKT": {
                    "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POINT Z (30.5 75.2 125.8)",
                    "@type": "geosparql:wktLiteral"
                }
            } 
    }
}
```

It should be noted that it is possible to represent multiple geo entries in various formats in order to align with
potential downstream users.  An intentionally verbose example follows.  

```json
{
    "@context": {
        "@vocab": "https://schema.org/",
        "geosparql": "http://www.opengis.net/ont/geosparql#" 
    },
    "@id": "https://example.org/id/XYZ",
    "@type": "Dataset",
    "name": "Data set name",
    "url": "http://example.org/dataset/X",
    "spatialCoverage": {
        "@type": "Place",
        "geo": [
            {
                "@type": "GeoShape",
                "description": "an basic POINT entry",  
                "geosparql:asWKT": {
                    "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POINT (30.5 75.2)",
                    "@type": "geosparql:wktLiteral"
                }
            },
            {
                "@type": "GeoShape",
                "description": "an example POINT Z entry",  
                "geosparql:asWKT": {
                    "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POINT Z (30.5 75.2 125.8)",
                    "@type": "geosparql:wktLiteral"
                }
            },
            {
                "@type": "GeoShape",
                "description": "an example POINT M entry",  
                "geosparql:asWKT": {
                    "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POINT M (30.5 75.2 404.8)",
                    "@type": "geosparql:wktLiteral"
                }
            },
            {
                "@type": "GeoShape",
                "description": "an example POINT ZM entry",  
                "geosparql:asWKT": {
                    "@value": "<http://www.opengis.net/def/crs/OGC/1.3/CRS84> POINT ZM (30.5 75.2 125.8 404.8)",
                    "@type": "geosparql:wktLiteral"
                }
            }
        ]
    }
}


```


The above example includes four examples for a basic POINT, a POINT Z with Z (elevation), a POINT M with M (measurement)
and an example with POINT ZM which includes both elevation and measurement.  

### Depth schema.org

It is also possible to use the elevation property in Schema.org (ref: [https://schema.org/elevation](https://schema.org/elevation)).  
This property is valid on https://schema.org/GeoCoordinates and https://schema.org/GeoShape.

An example for GeoCoordinate follows.

```json
{
    "@context": {
        "@vocab": "https://schema.org/",
        "geosparql": "http://www.opengis.net/ont/geosparql#"
    },
    "@id": "https://example.org/id/XYZ",
    "@type": "Dataset",
    "name": "Data set name",
    "spatialCoverage": {
        "@type": "Place",
        "geo": {
            "@type": "GeoCoordinates",
            "name": "Depth at a point",
            "description": "An example of expressing a depth as a negative elevation for type GeoCoordinates",
            "elevation": -1146,
            "latitude": 16.76203,
            "longitude": -25.10367
        }
    }
}
```

In this example we are using -1146.0 which would imply a depth measurement in meters.

The property elevation can be either a Number or Text.  In the case of Number, it would be taken as an elevation value following 
[WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System).  

For Text, from the schema.org documentation on elevation, the value of the property may be of the form
'NUMBER UNIT_OF_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should 
be assumed to be a value in meters. 

Note that in this approach elevation would tend to scope an entire geometry and not the individual points that
make up a geometry.    

### Depth Measurement

In cases where the depth information is in the data itself and not connected to a reference geometry 
that can be associated with the metadata, there are still approaches to including depth to aid in discovery in the 
metadata. 

In this case you can use the variableMeasured stanza to describe the depth variables in your dataset.

variable measured example:

```json
   {
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@id": "https://example.org/dataset/12345",
  "@type": "Dataset",
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "depth",
      "description": "Depth (spatial coordinate) relative to water surface in the water body. Definition: The distance of a sensor or sampling point below the sea surface",
      "value": "123.4",
      "propertyID": "https://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/",
      "measurementTechnique": "description of technique used",
      "unitText": "m",
      "unitCode": [
        "https://qudt.org/vocab/unit/M",
        "https://vocab.nerc.ac.uk/collection/P06/current/ULAA/",
        "http://dbpedia.org/resource/Metre"
      ]
    }
  ]
}
```

Note that in the above the type https://schema.org/PropertyValue is presented with a value.  However, in the case
where there is a large range of values including them is not useful.  However, there are two alternative 
properties that might be useful.  In the following example, the value has been replaced with the properties
minValue and maxValue.  

```json
   {
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@id": "https://example.org/dataset/12345",
  "@type": "Dataset",
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "depth",
      "description": "Depth (spatial coordinate) relative to water surface in the water body. Definition: The distance of a sensor or sampling point below the sea surface",
      "minValue": "34.4",
      "maxValue": "123.4",
      "propertyID": "https://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/",
      "measurementTechnique": "description of technique used",
      "unitText": "m",
      "unitCode": [
        "https://qudt.org/vocab/unit/M",
        "https://vocab.nerc.ac.uk/collection/P06/current/ULAA/",
        "http://dbpedia.org/resource/Metre"
      ]
    }
  ]
}
```


## Appendix

### Links and Resources

- Example NERC term for depth: [NVS](http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/)   (Noted to be narrower than "depth")
- Parameter search at BCO-DMO showing the various depth observations: [Parameter Search | BCO-DMO](https://www.bco-dmo.org/search/parameter/depth)
- [METS RCN Examples](https://github.com/NicoGEOMAR/METS-RCN/tree/main/Examples/Events)
- Some work proposed for this [Extending the GeoSPARQL ontology with full-featured 3D support · Issue #19 · opengeospatial/ogc-geosparql · GitHub](https://github.com/opengeospatial/ogc-geosparql/issues/19) 
- Min max depth URL examples: http://vocab.nerc.ac.uk/collection/P01/current/MAXWDIST/ and http://vocab.nerc.ac.uk/collection/P01/current/MINWDIST/

