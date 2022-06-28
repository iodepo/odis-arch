import kglab as kg
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import kglab

# set up the files we will use here
dg = './datagraphs/lipd.json'
sg = './shapes/oih_checkDownload.ttl'

namespaces = {
            "schema":  "https://schema.org/",
            "shacl":   "http://www.w3.org/ns/shacl#" ,
        }

kg = kglab.KnowledgeGraph(
            name = "Schema.org based datagraph",
            base_uri = "https://example.org/id/",
            namespaces = namespaces,
        )

kg.load_jsonld(dg)

conforms, report_graph, report_text = kg.validate(
            shacl_graph=sg,
            shacl_graph_format="ttl"
        )

print(report_text)

