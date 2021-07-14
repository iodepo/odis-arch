import json
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
from pyld import jsonld
import graphviz
import jbutils

with open("./creativework.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@type":     "CreativeWork",
  "author": ""
}

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)

# jd = json.dumps(compacted, indent=4)
# print(jd)

framed = jsonld.frame(compacted, frame)
print(framed)

jbutils.show_graph(compacted)
