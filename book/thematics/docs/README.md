---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
execution:
  allow_errors: true
---

# Documents

## About

Documents: These include datasets, reports or other documents

Maps: A map represented by a static file or document

```{seealso}
For OIH the focus is on generic documents which can scope reports, data and other resources.
In those cases where the resources being described are of type Dataset you may wish to review
patterns developed for GeoScience Datasets by the ESIP
[Science on Schema](https://github.com/ESIPFed/science-on-schema.org/) community.

```

## Creative works (documents)

 Documents will include maps, reports,
guidance and other creative works.  Due to this OIH will focus on a generic example
of [schema.org/CreativeWork](https://schema.org/CreativeWork) and then provide examples
for more focused creative work examples.

[Load in JSON-LD Playground](https://json-ld.org/playground/#startTab=tab-expanded&json-ld=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/creativework.json)

[Load in Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool#url=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/creativework.json)

```{literalinclude} ./graphs/creativework.json
:linenos:
```

## Frame on author type Person

Our JSON-LD documents are graphs that can use framing to subset.  In this 
case we can look closer at the author property which points to a type Person. 


```{code-cell}
:tags: [hide-input]

import json
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from pyld import jsonld
import graphviz
import jbutils

with open("./graphs/creativework.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "CreativeWork",
  "author": ""
}

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)

framed = jsonld.frame(compacted, frame)
jd = json.dumps(framed, indent=4)
print(jd)

jbutils.show_graph(framed)

```

## Maps

A map in this context would be a static file or document of some sort.  Map services like 
those described by an OGC Catalogue Service or other GIS service would be described as a 
service.  

```{note}
In the current context, schema.org Map typically references maps a document.
Here we are likely to reference a KML, Shapefile or GeoPackage.  We may wish to then 
indicate the type of document it is through a mimetype via encoding.  
```

The schema.org type Map only offers one special property beyond
the parent CreativeWork.  That is a [mapType](https://schema.org/Map) which is an
enumeration of types that do not apply to OIH use cases.  However, the use of the
Map typing itself may aid in narrowing search requests later to a specific creative work.

[Load in JSON-LD Playground](https://json-ld.org/playground/#startTab=tab-expanded&json-ld=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/map.json)

[Load in Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool#url=https://raw.githubusercontent.com/fils/odis-arch/master/schema/docs/graphs/map.json)


```{literalinclude} ./graphs/map.json
:linenos:
```


```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import jbutils

with open("./graphs/map.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```


### References

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



