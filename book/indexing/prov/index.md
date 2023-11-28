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
# Prov

## About

This is the start of some discussion on issues around prov tracking in OIH.
This may take two paths.  One would be the prov tracking indexers might do
and the other prov that providers would encode to provide specific prov
the community requests.

## Gleaner Prov

The Gleaner application generates a prov graph of the activity of accessing 
and indexing provider resources.  The main goal of this prov is to connect
an indexed URL to the digital object stored in the object store.  This 
digital object should be the JSON-LD data graph presented by the provider. 

By contrast, the authoritative reference in the various profiles will connect
the the data graph ID, or in the absence of that the data graph URL or the 
referenced resources URL by gleaner, to another reference.  This may be 
an organization ID or a PID of the connected resource. 



```{literalinclude} ./graphs/gleaner.json
:linenos:
```

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

with open("../../../odis-in/dataGraphs/indexing/prov/graphs/gleaner.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/",
  "prov": "http://www.w3.org/ns/prov#"},
  "@explicit": "false",
  "@type":     "prov:Activity",
   "prov:generated": {},
   "prov:endedAtTime": {},
   "prov:used": {}
}


context = {
  "@vocab": "https://schema.org/",
  "prov": "http://www.w3.org/ns/prov#"
}

compacted = jsonld.compact(doc, context)

framed = jsonld.frame(compacted, frame)
jd = json.dumps(framed, indent=4)
print(jd)


```


## Nano Prov

This is a basic nanoprov example. Note, this is a draft and
the ID connections and examples have not been made yet.  


```{literalinclude} ./graphs/nanoprov.json
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

with open("../../../odis-in/dataGraphs/indexing/prov/graphs/nanoprov.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```



## Refs

[Nanopubs Guidance](https://nanopub.org/guidelines/working_draft/)