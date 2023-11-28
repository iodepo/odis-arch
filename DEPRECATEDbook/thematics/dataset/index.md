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

# Datasets

## About

Datasets

```{seealso}
For OIH the focus is on generic documents which can scope reports, data and other resources.
In those cases where the resources being described are of type Dataset you may wish to review
patterns developed for GeoScience Datasets by the ESIP
[Science on Schema](https://github.com/ESIPFed/science-on-schema.org/) community.

```

## Datasets

 Documents will include maps, reports,
guidance and other creative works.  Due to this OIH will focus on a generic example
of [schema.org/CreativeWork](https://schema.org/CreativeWork) and then provide examples
for more focused creative work examples.

```{literalinclude} ./graphs/datasetTemplate.json
:linenos:
```

**Note**
For a generic `encodingFormat` inside a `distribution` block, you can use 
`image/xyz`, such as for the following, which points to a Digital Terrain Model:
  ```
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "http://222.186.3.18:8888/erddap/files/BATM_NMDIS_2020_Jinli_Seamount/BATM_NMDIS_2020_Jinli_Seamount.dtm",
    "encodingFormat": "image/xyz"
  },
  ```

## Demo area  please ignore

This area is being used to test out a new repository structure where the data graphs, 
frames and SHACL shapes are kept in a discrete location.  


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

with open("../../../code/dataGraphs/map.json") as dgraph:
    doc = json.load(dgraph)

with open("../../../code/frames/mapFrameID.json") as fgraph:
    frame = json.load(fgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)

framed = jsonld.frame(compacted, frame)
jd = json.dumps(framed, indent=4)
print(jd)

jbutils.show_graph(framed)

```
