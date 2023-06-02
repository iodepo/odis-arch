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

# Spatial Maps

## About

Map: A map represented by a static file or document



The schema.org type Map only offers one special property beyond
the parent CreativeWork.  That is a [mapType](https://schema.org/mapType) which is an
enumeration of types that do not apply to OIH use cases.  However, the use of the
Map typing itself may aid in narrowing search requests later to a specific creative work.

Schema.org type Map is a subtype of CreativeWork. As such, we can all the approaches 
described in the [Documents](./index.md) section for this type as well.  The use 
of type Map would be focused on documenting files such as KML, GeoJSON or others as a
creative work that may be downloaded and used either in a workflow or directly.  

A map in this context would be a static file or document of some sort.  Map services like 
those described by an OGC Catalogue Service or other GIS service would be described as a 
service.  Potential approaches for doing can be seen the service type.    

```{note}
In the current context, schema.org Map typically references maps as a document.
Here we are likely to reference a KML, Shapefile or GeoPackage.  We may wish to then 
indicate the type of document it is through a mimetype via encoding.  
```

```{literalinclude} ../../../odis-in/dataGraphs/thematics/docs/graphs/map.json
:linenos:
```


```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/map.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```


### Details: Identifier

For each profile there are a few key elements we need to know about.  One
key element is what the authoritative reference or canonical identifier is for 
a resource.  

```{code-cell}
:tags: [hide-input]

import json
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from pyld import jsonld
import graphviz
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/map.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "Map",
  "identifier": ""
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

### Keywords

We can see three different approaches here to defining keywords.


```{code-cell}
:tags: [hide-input]

import json
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from pyld import jsonld
import graphviz
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/map.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "Map",
  "keywords": ""
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



