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

# Experts and Institutions

## About

Expert:  A person who has a deep understanding of a particular subject area.

Institution: A group of people working together to provide a particular service.
  
## Example: Person Graph

The following graph present a basic record we might present about a person.  
We can break down some of the key attributes of this record.

OIH is using [schema.org/Person](https://schema.org/Person) for this type.
Any of the properties of Person seen there are valid to use in such a record.

At the core though there are a few key items OIH is looking for in a Person record.


```{literalinclude} ./graphs/person.json
:linenos:
:emphasize-lines: 5-7, 10, 27-32
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

with open("./graphs/person.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```


### Details: Authoritative Reference

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

with open("./graphs/person.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Person",
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


### Details: Knows About

Knows about provide connections to resources a person is
connected with.  The property, [schema.org/knowsAbout](https://schema.org/knowsAbout),
can connect a Person or Organization to Text, URL or any Thing type.  

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

with open("./graphs/person.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Person",
  "knowsAbout": ""
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


## Example: Institution Graph

Here we have an example of an data graph for type [schema.org/Organization](https://schema.org/Organization).  
For the identifier we are using the a GRID, but this could also be something like a ROR.  


```{literalinclude} ./graphs/organization.json
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

with open("./graphs/organization.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)

```


### Details: Authoritative Reference

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

with open("./graphs/organization.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "Organization",
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




## References

* [schema:Person](https://schema.org/Person)
* [scheme:Organization](https://schema.org/Organization)
* [Science on Schema Repository](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/DataRepository.md)
* [https://oceanexpert.org/](https://oceanexpert.org/)
  * [Example page expert](https://oceanexpert.org/expert/44151)
  * [Example page institution](https://oceanexpert.org/institution/10171)
  * [Ocean Expert: refernce: Adam Leadbetter](https://gist.github.com/adamml/58ebdc7fc3f8ab8dad5d8852a28fb28c)
