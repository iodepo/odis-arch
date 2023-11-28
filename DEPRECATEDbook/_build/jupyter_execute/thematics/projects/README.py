#!/usr/bin/env python
# coding: utf-8

# # Projects
# 
# ## About
# 
# Project: An enterprise (potentially individual but typically
# collaborative), planned to achieve a particular aim. Use properties from
# Organization, subOrganization/parentOrganization to indicate project sub-structures.
# 
# ## Research Project
# 
# This is what a basic research project data graph might look like.  We have
# the full record below, but this shows some of the basics we would be 
# looking for.
# 
# This type is based on the Schema.org type [Project](https://schema.org/Project) which 
# has a sub-type of [ResearchProject](https://schema.org/ResearchProject).

# In[1]:


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

with open("./graphs/proj.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "ResearchProject",
  "legalName": "",
  "name": "",
  "url": "",
  "description": "",
  "identifier": {} 
}

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)

framed = jsonld.frame(compacted, frame)
jd = json.dumps(framed, indent=4)
print(jd)

jbutils.show_graph(framed)


# ### Details: Identifier
# 
# For each profile there are a few key elements we need to know about.  One
# key element is what the authoritative reference or canonical identifier is for 
# a resource.

# In[2]:


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

with open("./graphs/proj.json") as dgraph:
    doc = json.load(dgraph)

frame = {
  "@context": {"@vocab": "https://schema.org/"},
  "@explicit": "true",
  "@requireAll": "true",
  "@type":     "ResearchProject",
  "identifier": ""
}

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)

framed = jsonld.frame(compacted, frame)
jd = json.dumps(framed, indent=4)
print(jd)

jbutils.show_graph(framed)


# ## Full Research Project
# 
# Here is what our full record looks like.  We have added in several 
# more nodes to cover things like funding source, policy connections,
# spatial area served and parent organization. 
# 
# 
# ```{literalinclude} ./graphs/proj.json
# :linenos:
# ```

# In[3]:


import json
from pyld import jsonld
import os, sys

currentdir = os.path.dirname(os.path.abspath(''))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib import jbutils

with open("./graphs/proj.json") as dgraph:
    doc = json.load(dgraph)

context = {
    "@vocab": "https://schema.org/",
}

compacted = jsonld.compact(doc, context)
jbutils.show_graph(compacted)


# ### References
# 
# * https://schema.org/Project
