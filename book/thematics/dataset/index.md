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

```{literalinclude} ../../../odis-in/dataGraphs/thematics/dataset/graphs/datasetTemplate.json
:linenos:
```

```{tip}
@id around line#6 should point to whatever resolves eventually to the JSON-LD - if you only
have an external JSON-LD file (and not embedded into the html `<script>` tag)
then the @id should point to the .json file itself. Otherwise, @id should point
to the landing page of the record (HTML page), that embeds the JSON-LD.
```

```{note}
schema.org expects a lat long (Y X) coordinate order, so be aware of that when
you are defining your spatialCoverage, in the GeoShape polygon or box parameters.
```

Using a bounding box for your spatialCoverage is recommended, as it is easy to query 
& display downstream, such as:

```{literalinclude} ../../../odis-in/dataGraphs/thematics/dataset/graphs/datasetTemplate-Box.json
:linenos:
:lines: 56-68
:emphasize-lines: 4-6
```

## Demo area  please ignore

This area is being used to test out a new repository structure where the data graphs, 
frames and SHACL shapes are kept in a discrete location.  


```{code-cell}
:tags: [hide-input]

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    
import json
from pyld import jsonld
import os, sys
import urllib
import contextlib

devnull = open(os.devnull, 'w')
contextlib.redirect_stderr(devnull)

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

 
url = "https://raw.githubusercontent.com/iodepo/odis-in/master/dataGraphs/thematics/docs/graphs/map.json"
dgraph = urllib.request.urlopen(url)
doc = json.load(dgraph)

furl = "https://raw.githubusercontent.com/iodepo/odis-in/master/frames/mapFrameID.json"
fgraph = urllib.request.urlopen(furl)
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
