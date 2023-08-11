import json
from pyld import jsonld
from utils import jbutils

with open("dataGraphs/doc1.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/",
  "prov": "http://www.w3.org/ns/prov#",},
  "@explicit": "false",
  "@type":     "prov:Activity",
   "prov:generated": {},
   "prov:endedAtTime": {},
   "prov:used": {}
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
