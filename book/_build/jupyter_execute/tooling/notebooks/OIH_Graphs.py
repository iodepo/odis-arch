#!/usr/bin/env python
# coding: utf-8

# # OIH Graph testing
# 

# In[21]:


import rdflib
import gzip

with gzip.open('./oceanexperts_graph.nq.gz', 'rb') as f:
    file_content = f.read()

g = rdflib.Graph()
g.parse(data = file_content, format="nquads")


# In[22]:


qres = g.query(
    """prefix schema: <https://schema.org/>
    SELECT DISTINCT ?s ?name
       WHERE {
          ?s a schema:Course .
          ?s schema:name ?name
       }
       LIMIT 10""")

for row in qres:
    print("%s Course Name: %s" % row)


# In[ ]:





# In[ ]:




