import json
import rdflib
import numpy as np
import urllib.request
import pyshacl
from pyshacl import validate
from pyshacl import Validator
from pathlib import Path

# TODO
# Need to add a new context to the data file perhaps
# by doing a context exapansion

df = Path('./dataNewCtx.json').read_text()
# dataUrl = urllib.request.urlopen("https://pacific-data.sprep.org/sites/default/files/pod_data/data.json")
# df = dataUrl.read()
dg = rdflib.Graph()
dg.parse(data=df, format="json-ld")

sf = Path('./dcatsdoOLD.ttl').read_text()
# shapeUrl = urllib.request.urlopen("https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev/book/tooling/notebooks/Mapping/DCATmapping/shapes/dcatsdoOLD.ttl")
# sf = shapeUrl.read()
sg = rdflib.Graph()
sg.parse(data=sf, format="ttl")

v = Validator(data_graph=dg, shacl_graph=sg,  options={"inference": "none", "advanced": True})  # turn off rdfs inferencing
conforms, report_graph, report_text = v.run()
expanded_graph = v.target_graph

output = str(expanded_graph.serialize(format="ttl")) #.decode("utf-8"))

#save file
file = open("output.rdf", "w")
file.write(output)
file.close()

