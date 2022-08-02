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
Ocean Variables.   

A rough description of these links leveraging pseudo schema.org terms follows with a detailed
and valid data graph as an example after that.  

Reference image:

![notes image](./eov.png)


The image above details out some of the key points to be encoded.  These include:

* Links to and description of methods
* QA/QC references
* Links to GOOS Specification sheets
* Information on variables measured
* Connections to the event measured and potential associated instruments
* Spatial coverage
* Temporal coverage

The valid data graph follows the reference section and details follow that.  The highlighted lines
in the data graph represented the detailed sections.   

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

```{note}
There can be multiple links in the proertyID property.  Preference should be given to those with semantic descriptions.
```

```{note}
In cases where a single value can be associated with a variable, or a min max value, this can be provided along with a
unitCode property.   In cases where a variable represents a large collection of data this can be omitted and the data obtained
in a distribution reference.  
```



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

For this section on EOVs, it is used to link in the specification sheets for the measured variables.  This can also be used to link
in QA/QC documentation.  There is no direct connection between the creative works linked here and the measured variables though convention 
would be to keep the order the same if possible.  Such order is not maintained through potential serialization of the JSON-LD records though 
list order can be maintained with an @list keyword.  

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

This section is an attempt to leverage schema.org to link instrument information.  This is done via the Event type with a
connected Action type.  


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

Representation of temporal coverage follows [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) patterns.  ESIP Science on Schema
as has patterns for Deep Time (geologic time) patterns.  

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




