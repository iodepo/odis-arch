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
# Vessels

## About

Exploring using schema.org to describe research vessels.  Note that schema.org
is a very broad vocabulary and as such specific concepts like research vessel is
not well aligned.

One approach we can use, however, is to leverage schema.org a a discovery layer
and link more directly to detailed institutional metadata records.  


```{literalinclude} ./graphs/ship.json
:linenos:
```



![Doc Guidance image](./graphs/ship.svg)

## References

* [ICES](https://ocean.ices.dk/codes/ShipCodes.aspx)
* POGO
* EurOcean
* https://vocab.nerc.ac.uk/search_nvs/C17/
* [SeaDataNet](https://www.seadatanet.org/)
* [Marine Facilities Planner](https://www.marinefacilitiesplanning.com/)
* [EuroFleets](https://www.eurofleets.eu/)
* Identifiers to use include NOCD Code, Call Sign, ICES Shipcode, MMSI Code, IMO Code 


```{code-cell}
:tags: [hide-input]

import json
import pyld
import os
import requests

SO_CONTEXT = {
    "http://schema.org": "jsonldcontext.jsonld",
    "http://schema.org/": "jsonldcontext.jsonld",
    "https://schema.org": "jsonldcontext.jsonld",
    "https://schema.org/": "jsonldcontext.jsonld",
}

if not os.path.exists("jsonldcontext.jsonld"):
    with open("jsonldcontext.jsonld", "w") as outf:
        outf.write(requests.get("https://schema.org/docs/jsonldcontext.jsonld").text)

def localDocumentLoader(context_map={}):

    def localDocumentLoaderImpl(url, options={}):
        _url = url.lower().strip()
        doc = context_map.get(_url, None)
        if not doc is None:
            res = {
                "contextUrl": None,
                "documentUrl": "https://schema.org/docs/jsonldcontext.jsonld",
                "contentType": "application/ld+json",
                "document": json.load(open(doc, "r")),
            }
            return res
        loader = pyld.jsonld.requests_document_loader()
        return loader(url)
    
    return localDocumentLoaderImpl
    

with open("test1.jsonld") as inf:
    doc = json.load(inf)
options = {"documentLoader": localDocumentLoader(context_map=SO_CONTEXT)}
expanded = pyld.jsonld.expand(doc, options)
print(json.dumps(expanded, indent=2))
```
