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
# Service


## About 

This section will provide information on the service type.  This is not 
one of the main OIH types.  However, we will provide guidance here on describing
services using schema.org.

It should be noted that this might be a simple link to an OpenAPI or some 
other descriptor document.  Also, schema.org is not rich enough for complex 
descriptions and itself borrows from the [Hydra](https://www.hydra-cg.com/spec/latest/core/)
vocabulary.  It may be required to leverage Hydra if complex descriptions are 
needed.

The graph describes a service than can be invoked with:

```bash
curl --data-binary "@yourfile.jpg" -X POST https://us-central1-top-operand-112611.cloudfunctions.net/function-1
```

This with POST a jpeg to the service and get back a simple text response with some information
about the image.


```{literalinclude} ../../../odis-in/dataGraphs/thematics/services/graphs/service.json
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

with open("../../../odis-in/dataGraphs/thematics/services/graphs/serviceBase.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)
```

## References

* https://schema.org/docs/actions.html
* https://schema.org/Action
* https://www.w3.org/TR/web-share/
* https://www.hydra-cg.com/spec/latest/core/


