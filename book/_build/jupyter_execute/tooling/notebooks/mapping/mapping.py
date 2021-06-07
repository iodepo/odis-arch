#!/usr/bin/env python
# coding: utf-8

# # Mapping
# 
# Testing approaches to mapping DCAT to schema.org
# 
# Current thinking
# 
# * JSON-LD Frame with default values
# * SPARQL construct on these resulting frame to generate the new triples
# 
# Mapping references
# 
# * https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping
# * https://ec-jrc.github.io/dcat-ap-to-schema-org/
# * https://data.gov.au/data/dataset/67ca5de1-8774-4678-9d1b-8b1cb70ab33c.jsonld
# 

# ## Methodology
# 
# We will load the DCAT JOSN-LD example and explore approaches to converting this to a form that can be used for 
# schema.org.  
# 
# Possible approaches include
# 
# * Inferencing
#     * ref: https://derwen.ai/docs/kgl/infer/
# * SPARQL CONSTRUCT
#     * https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html
#     * https://derwen.ai/docs/kgl/ex4_0/
# * JSON-LD APIs
#     * https://w3c.github.io/json-ld-framing/#omit-default-flag
# * Context modification

# In[113]:


import kglab
import json
import rdflib


# In[122]:


# load our JSON into a var to use later
f = open('dcatEx.json',)
j = json.load(f)
f.close()


# ## JSON-LD
# 
# Use a frame to pull the elements we want to map, then alter the context for that 
# frame or otehrwise cast to new namespace.
# 
# Frame with defaults and then work to convert to new names space with SPARQL construct

# ## SPARQL CONSTRUCT example
# 
# Refs:
# * https://derwen.ai/docs/kgl/ex4_0/

# In[123]:


from icecream import ic
from pathlib import Path

txt = Path('dcatEx.json').read_text()

g = rdflib.Graph()
g.parse(data=txt, format="json-ld")


# In[124]:


sparql = """
    SELECT ?s ?p ?o 
    WHERE {
        ?s ?p ?o .
    }
    LIMIT 1
"""


# In[125]:


for row in g.query(sparql):
    ic(row.asdict())


# In[126]:


sparqlc = """
 PREFIX dbpedia: <http://dbpedia.org/resource/>
 PREFIX foaf: <http://xmlns.com/foaf/0.1/>
 PREFIX dc: <http://purl.org/dc/elements/1.1/>
 PREFIX dct: <http://purl.org/dc/terms/>
 PREFIX mo: <http://purl.org/ontology/mo/>
 PREFIX schema: <https://schema.org/>

CONSTRUCT { 
       ?s schema:identifier ?o .
 }
 WHERE { 
       ?s dct:identifier ?o .
 }
"""

qres = g.query(sparqlc)
context = {"@vocab": "https://schema.org/", "@language": "en"}
print(qres.serialize(format='json-ld', context=context, indent=4))

# g.parse(qres, format="nt")
    
# for row in qres:
#     print("-----")
#     print(row)


# In[127]:


import kglab

namespaces =  {
    "adms": "http://www.w3.org/ns/adms#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "gsp": "http://www.opengis.net/ont/geosparql#",
    "locn": "http://www.w3.org/ns/locn#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "time": "http://www.w3.org/2006/time",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  }

kg = kglab.KnowledgeGraph(
    name = "DCAT example",
    base_uri = "https://www.example.org/",
    namespaces = namespaces,
    )

kg.load_jsonld("dcatEx.json")


# In[128]:


sparql2 = """
    SELECT ?s  ?o 
    WHERE {
        ?s dct:description ?o .
    }
"""


# In[129]:


import pandas as pd
pd.set_option("max_rows", None)

df = kg.query_as_df(sparql2)
df.head(20)


# In[130]:


pyvis_graph = kg.visualize_query(sparql2, notebook=True)

pyvis_graph.force_atlas_2based()
pyvis_graph.show("tmp.fig06.html")


# ## SHACL Rules

# In[131]:


import pyshacl


# In[181]:


from pyshacl import validate

conforms, v_graph, v_text = validate(data_graph="./learning.jsonld", 
                shacl_graph='./oih_learning.ttl', 
                data_graph_format="json-ld", 
                shape_graph_format="ttl", 
                inference='none', 
                serialize_report_graph="json-ld")


# In[182]:


print(conforms)
print(v_graph)
print(v_text)


# In[198]:


from pyshacl import Validator

# v = Validator(data_graph=dg_basin, shacl_graph=rule, options={"inference": "rdfs"},ont_graph=ont)
# conforms, report_graph, report_text = v.run()
# expanded_graph = v.target_graph 

df = Path('data.ttl').read_text()
dg = rdflib.Graph()
dg.parse(data=df, format="ttl")

sf = Path('shape.ttl').read_text()
sg = rdflib.Graph()
sg.parse(data=sf, format="ttl")

v = Validator(data_graph=dg, shacl_graph=sg,  options={"inference": "rdfs", "advanced": True})
conforms, report_graph, report_text = v.run()
expanded_graph = v.target_graph 


# In[199]:


# print(conforms)
# print(v_graph)
# print("------------")
# print(v_text)
print(expanded_graph)


# In[201]:


print(expanded_graph.serialize(format="json-ld").decode("utf-8"))


# In[ ]:




