import kglab
import json
import rdflib
import numpy as np
from icecream import ic
from pathlib import Path
import pyshacl
from pyshacl import validate
from pyshacl import Validator


df = Path('./data/datahub.json').read_text()
dg = rdflib.Graph()
dg.parse(data=df, format="json-ld")

sf = Path('./shapes/dcatsdoOLD.ttl').read_text()
sg = rdflib.Graph()
sg.parse(data=sf, format="ttl")

v = Validator(data_graph=dg, shacl_graph=sg,  options={"inference": "none", "advanced": True})  # turn off rdfs inferencing
conforms, report_graph, report_text = v.run()
expanded_graph = v.target_graph

output = str(expanded_graph.serialize(format="ttl")) #.decode("utf-8"))

#save file
file = open("output.txt", "w")
file.write(output)
file.close()


