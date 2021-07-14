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

# Defined Terms

## About

During generation of the structured data a provide may wish to 
either use or publish a set of controlled vocabulary terms or 
a similar set.  

Within schema.org this could be done by leveraging the "DefinedTerm" 
amd "DefinedTermSet" types.  

These types allow us both to define a set of terms and 
use a set of terms in describing a thing.

Note that DefinedTerm is an intangible and can connect to most 
types in Schema.org.  So we can use them in places such as:

* CreativeWork -> keyword
* LearningResource -> teaches
* PropertyValue -> valueReference
* LearningResource -> competencyRequired
* CreativeWork -> learningResourceType


```{literalinclude} ./graphs/term.json
:linenos:
```




## Organization in List

```{literalinclude} ./graphs/orglist.json
:linenos:
```


```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import jbutils

with open("./graphs/orglist.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```


## References

* [schema.org/DefinedTerm](https://schema.org/DefinedTerm)
* [schema.org/DefinedTermSet](https://schema.org/DefinedTermSet)