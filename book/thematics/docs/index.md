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

```{literalinclude} ../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json
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
with open("../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```



### Details: Indentifier

For each profile there are a few key elements we need to know about.  One
key element is what the authoritative reference or canonical identifier is for 
a resource.  

```{code-cell}
:tags: [hide-input]
import json
from pyld import jsonld
import os, sys
import urllib

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


with open("../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "CreativeWork",
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


### Publisher and provider

Our JSON-LD documents are graphs that can use framing to subset.  In this case
we can look closer at the `provider` and `publisher` properties, which are both 
of type `Organization`. 


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

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "CreativeWork",
  "provider": {},
  "publisher": {}
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


### Author type Person

Our JSON-LD documents are graphs that can use framing to subset.  In this 
case we can look closer at the author property which points to a type Person. 


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

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json") as dgraph:
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

### License


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

with open("../../../odis-in/dataGraphs/thematics/docs/graphs/creativework.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "CreativeWork",
  "license": {}
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

#### License as URL  

```json
{
  "@context": "https://schema.org/",
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
```



#### License as CreativeWork 

```json
{
  "@context": "https://schema.org/",
  "license": {
    "@type": "CreativeWork",
    "name": "Creative Commons Attribution 4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/"
  }
}

```
 

#### License as SPDX URL 

- Use a simple URL
- [SPDX](https://spdx.org/licenses/) creates URLs for many licenses including those that don't have URLs
- From a source that <em>harvesters</em> can rely on (e.g. use URL to lookup more information about the license)

```json
{
  "@context": "https://schema.org/",
  "license": "https://spdx.org/licenses/CC-BY-4.0"
}
```

OR, include both the SPDX and the Creative Commons URLs in an array:

```json
{
  "@context": "https://schema.org/",
  "license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"]
}
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
*[EMODnet](https://emodnet.ec.europa.eu/en)  (Coner Delaney)
  * ERDAP also
  * Are we talking links from schema.org that link to OGC and ERDAP services 
  * Are these methods?  
  * Sounds like may link to external metadata for interop they have developed in the community
* NOAA connected as well
  * Interested in OGC assets  
  * ERDAP data platform



