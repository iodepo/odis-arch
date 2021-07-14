# Sargassum Project Template 

## About

When looking at the [Sargassum Projects](https://sargassumhub.org/sargassumexperts/) page we 
can see some map interfaces.  In the first we are able to view and export the data in 
a table.  If we pull this data out as a .csv file we can load it into 
[OpenRefine](https://openrefine.org/) and from there use the 
[templating exporter](https://docs.openrefine.org/manual/exporting#templating-exporter) to 
generate a valid JSON-LD document.   


```{figure} ./images/sargassumtemplate.png
---
name: Sargassum Project Template
---
A view of the template export in OpenRefine with the following sections inserted
```

The following are the templates sections for the OpenRefine
export template command.

There are four sections

## PREFIX

``` 
{
     "@context": {
        "@vocab": "https://schema.org/" 
    },
    "@type": ["ItemList", "ResearchProject"],
    "name": "Sargassum Information Hub Projects",
    "author": "Sargassum Information Hub",
    "about": {
      "@type": "ResearchProject"
    },
    "itemListElement": [

```

## ROW TEMPLATE

:::{admonition} Note
:class: tip

In the following row template the entries such as:

```
  {{jsonize(cells["Organization Description"].value)}}
```
will present a value with quotes around it.

Where

```
${x}
```

will present the value from the noted colum, x, with no quotes around it.

When generating the JSON we may or may not need to include quotes depending 
on where we are in the serialization.

:::


``` 
{
    "@context": {
        "@vocab": "https://schema.org/" 
    },
    "@type": "ResearchProject",
    "description":  {{jsonize(cells["Organization Description"].value)}},
    "name" : {{jsonize(cells["Organization name"].value)}},
    "url":  {{jsonize(cells["Sargassum Activity Website"].value)}},
       "geosparql:hasGeometry": {
        "@type": "http://www.opengis.net/ont/sf#Point",
        "geosparql:asWKT": {
            "@type": "http://www.opengis.net/ont/geosparql#wktLiteral",
            "@value": "POINT(${y} ${y})"
        },
        "geosparql:crs": {
            "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
    }
}
```

## ROW SEP

``` 
,
```


## SUFFIX

``` 
 ]
}
```

## NOTES

``` 


{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": "Course",
    "courseCode": "F300",
    "name": "Physics",
    "provider": {
        "@type": "CollegeOrUniversity",
        "name": "University of Bristol",
        "url": {
            "@id": "/provider/324/university-of-bristol"
        }
    }
}


    {
      "ID" : {{jsonize(cells["ID"].value)}},
      "type" : {{jsonize(cells["type"].value)}},
      "description" : {{jsonize(cells["description"].value)}},
      "name" : {{jsonize(cells["name"].value)}},
      "provider.name" : {{jsonize(cells["provider.name"].value)}},
      "provider.url" : {{jsonize(cells["provider.url"].value)}},
      "CourseInstance" : {{jsonize(cells["CourseInstance"].value)}},
      "courseMode" : {{jsonize(cells["courseMode"].value)}},
      "enddata" : {{jsonize(cells["enddata"].value)}},
      "startdate" : {{jsonize(cells["startdate"].value)}}
    }


```
