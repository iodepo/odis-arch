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

# Essential Ocean Variables

This section details initial documentation of approaches for describing elements of a 
[schema:Dataset](https://schema.org/Dataset) with a focus on approaches supporting Essential 
Ocean Variables.   This includes the ability to link to supporting documents for quality assurance
and control (QA/QC) and specification sheets.  Also shown here are methods to encode the 
event and associated instruments along with spatial and temporal elements.  

A rough description of these links leveraging pseudo schema.org terms follows with a detailed
and valid data graph as an example after that.  We will then frame out and break down some of the 
specific elements.  

Reference image:

![notes image](./eov.png)

## References:

* [GOOS reference](https://www.goosocean.org/index.php?option=com_content&view=article&layout=edit&id=283&Itemid=441)
* [Goos example spec sheet](https://www.goosocean.org/index.php?option=com_oe&task=viewDocumentRecord&docID=17465) and
* [OBIS examples](https://manual.obis.org/examples/)


```{literalinclude} ./graphs/obisData2.json
:linenos:
:emphasize-lines: 10,13,14-30,31,32-50,56-67,77-101,104
```

## license

As licenses are an important cross-cutting item there is a separate section on licenses
at:  [License chapter](../license/README.md)

## keywords

As keywords are an important cross-cutting item there is a separate section on keywords
at:  [Keywords chapter](../terms/list.md)

## variableMeasured

A key section detailing approaches to describing variables.  This property expects either of text or
the more detailed [schema:PropertyValue](https://schema.org/PropertyValue).

```{seealso}
See also:  [Science on Schema variable](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#variables)
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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "variableMeasured": ""
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

## measurementTechnique

[https://schema.org/measurementTechnique](https://schema.org/measurementTechnique) is used to provide either
text about or a URL to information about the techniques or technology used in a Dataset.

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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "measurementTechnique": ""
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

## publishingPrinciples

As defined in the [Linking to Principles](https://book.oceaninfohub.org/thematics/sdg/index.html#publishingprinciples) 
section on publishing principles, This can be used to connect CreativeWork, Organization, or Person to either of 
CreativeWork or URL. So this allows us to link a CreativeWork to a policy or principle statement. 
This has some very useful use cases where resources can be grouped based on their connection to those principles and policies.

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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "publishingPrinciples": ""
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

## spatialCoverage

More details on spatial elements are found
at:  [Spatial Geometry](https://book.oceaninfohub.org/thematics/spatial/README.html)

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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "spatialCoverage": ""
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

## about

```{seealso}
See also [Identifier and Prov subjectOf and inverse about](https://book.oceaninfohub.org/thematics/identifier/id.html#subjectof-and-inverse-about).
[schema:about](https://schema.org/about) connects the subject matter of the content.
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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "about": ""
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

## temporalCoverage

```{seealso}
This section is based on the 
[Science on Schema Temporal Coverage](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#temporal-coverage)
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

with open("./graphs/obisData2.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "Dataset",
  "temporalCoverage": ""
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

### Science on Schema temporalCoverage

Example from Science on Schema recommendations:

```{literalinclude} ./graphs/temporalCoverage.json
:linenos:
```




