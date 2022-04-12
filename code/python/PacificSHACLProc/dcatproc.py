import json
import rdflib
import numpy as np
import urllib.request
import pyshacl
import gzip
from pyshacl import validate
from pyshacl import Validator
from pathlib import Path

# TODO
# Need to add a new context to the data file perhaps
# by doing a context expansion

source = './source_ctxUpdate.json.gz'
output = './output.ttl.gz'

with gzip.open(source, 'rb') as f:
        df = f.read()

# dataUrl = urllib.request.urlopen("https://pacific-data.sprep.org/sites/default/files/pod_data/data.json")
# df = dataUrl.read()
dg = rdflib.Graph()
dg.parse(data=df, format="json-ld")

sf = Path('./shape_dcatsdo.ttl').read_text()
# shapeUrl = urllib.request.urlopen("https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev/book/tooling/notebooks/Mapping/DCATmapping/shapes/dcatsdoOLD.ttl")
# sf = shapeUrl.read()
sg = rdflib.Graph()
sg.parse(data=sf, format="ttl")

v = Validator(data_graph=dg, shacl_graph=sg,  options={"inference": "none", "advanced": True})  # turn off rdfs inferencing
conforms, report_graph, report_text = v.run()
expanded_graph = v.target_graph

og = bytes(expanded_graph.serialize(format="ttl"), 'utf-8') #.decode("utf-8")

with gzip.open(output, 'wb') as f:
        f.write(og)
