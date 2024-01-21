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


This thematic type provides a way to describe the experts and institutions. 
In this case the following definitions are used:
  
> Expert:  A person who has a deep understanding of a particular subject area.
>
> Institution: A group of people working together to provide a particular service.
> 
## Example: Person Graph

The following graph present a basic record we might use for a person.  
We will break down some of the key properties used in this graph.

As Ocean InfoHub is levergaing Schema.org we are 
using [schema.org/Person](https://schema.org/Person) for this type.
Any of the properties of Person seen there are valid to use in such a record.

While publishers are free to use as many elements as they wish, our goal 
with this documentation is provide a simple example that address some of the search
and discovery goals of OIH along with those properties most useful in the linking 
of resources between OIH participants.   


```{literalinclude} ../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json
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

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json") as dgraph:
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

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json") as dgraph:
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


### Details: nationality

Nationality provide connections to languages a person is
connected with.  The property, [schema.org/nationality](https://schema.org/nationality),
is used to present that.  In the OIH we need to state what the semantics of 
nationality are for our use case. 


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

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Person",
  "nationality": ""
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


```{note}
The visual above demonstrates an issue that can be seen in several of the graph.  Where we 
don't use an @id the graph will be represented as a ["blank node"](https://en.wikipedia.org/wiki/Blank_node).  
These will be uniquely identified in the graph, however, in the construction of the visual
this is a common blank node and results in the double arrows pointing to an underscore.
This is a visualization issue and not a proper representation of the graph structure. 
```



### Details: knowsLanguage

Knows about provide connections to languages a person is
connected with.  The property, [schema.org/knowsLanguage](https://schema.org/knowsLanguage),
is used to present that.   Multiple languages can be expressed using the JSON
array [] syntax.   

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

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Person",
  "knowsLanguage": ""
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

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/person.json") as dgraph:
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



```{literalinclude} ../../../odis-in/dataGraphs/thematics/expinst/graphs/organization.json
:linenos:
:emphasize-lines: 18-29
```

### On the property membership

Line 18-29 show the inclusion of a [schema.org/member](https://schema.org/member)
property.  There are issues to note here both for consumers (aggregators) and 
providers (publishers).   The Person type is show connected simply on a type and 
id.  This provides the cleanest connection.  If a member is added by type and id, as 
in the case of the "Organization A" link, there is the problem of additional triples
being added.  Here, the name and description properties are going to add triples to the
OIH KG.  In so doing, we run the risk or adding potentially un-authoritative information.
The aggregator doesn't know if triples here are or are not provided by an actor
authoritative for those properties.  This could be addresses with framing or validation 
workflows, or ignored.  The prov elements stored could be leveraged to later track
down sources, but don't provide further information on the issue of authority.  

It is recommended that best practice is to attempt to link only on ids (with a type in 
all cases) where possible.  If you are connecting with a type, do not provide additional 
properties.  In cases where such an id can not be provided, you may wish to fill out 
basic properties you can provide with confidence. 


```{code-cell}
:tags: [hide-input]

import json
from pyld import jsonld
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/organization.json") as dgraph:
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
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from pyld import jsonld
import graphviz
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("../../../odis-in/dataGraphs/thematics/expinst/graphs/organization.json") as dgraph:
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
  * [Ocean Expert: reference: Adam Leadbetter](https://gist.github.com/adamml/58ebdc7fc3f8ab8dad5d8852a28fb28c)
