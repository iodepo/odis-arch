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

# Training

## About

From [https://schema.org/Course](https://schema.org/Course)

Course: A description of an educational course which may be offered as distinct instances at which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.

## Basic Course style

```{literalinclude} ./graphs/course1.json
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

with open("./graphs/course1.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```

 
## Simple Course

```{literalinclude} ./graphs/course2.json
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

with open("./graphs/course2.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```

 

## References

* [RDA Education and Training on handling of research data IG
](https://www.rd-alliance.org/groups/education-and-training-handling-research-data.html)
* [DC Tabular Application Profiles (DC TAP) - Primer](https://www.dublincore.org/groups/application_profiles_ig/dctap_primer/)
* https://www.w3.org/TR/xmlschema11-2/
  * Use YYYY-MM-DDThh:mm:ss or YYYY-MM-DD
* [http://www.marinetraining.eu/](http://www.marinetraining.eu/)
  * [Example page](http://www.marinetraining.eu/node/1001)
* [https://oceanexpert.org/](https://oceanexpert.org/)
* [Example page](https://oceanexpert.org/event/2859)
* [OCTO](https://www.octogroup.org/)
* https://oceansummerschools.iode.org/ 
* https://www.openchannels.org/upcoming-events-list 
* https://catalogue.odis.org/search/type=16 
* https://clmeplus.org/
