#!/usr/bin/env python
# coding: utf-8

# # Graph Analytics Exploration
# 
# * https://stackoverflow.com/questions/39274216/visualize-an-rdflib-graph-in-python
# * https://networkx.org/documentation/stable/reference/algorithms/link_analysis.html
# 
# ## Steps
# 
# * Pull in the OIH RDF graph and load 
# 

# In[1]:


get_ipython().system('pip -q install pydotplus')
get_ipython().system('pip -q install graphviz')
# !pip -q install rdflib
# !pip install -q -e git+https://github.com/RDFLib/rdflib.git#egg=rdflib
get_ipython().system('pip -q install pydotplus')
get_ipython().system('pip -q install mimesis')
get_ipython().system('pip -q install minio ')
get_ipython().system('pip -q install s3fs')
get_ipython().system('pip -q install SPARQLWrapper')
get_ipython().system('pip -q install boto3')
get_ipython().system("pip -q install 'fsspec>=0.3.3'")
get_ipython().system('pip -q install rdflib')
get_ipython().system('pip -q install rdflib-jsonld')
get_ipython().system('pip -q install PyLD==2.0.2')


# In[2]:


import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_digraph
import networkx as nx
import matplotlib.pyplot as plt
import gzip

with gzip.open('oceanexperts_graph.nq.gz', 'rb') as f:
    file_content = f.read()

g = rdflib.Graph()
g.parse(data = file_content, format="nquads")

G = rdflib_to_networkx_digraph(g)
# G = rdflib_to_networkx_multidigraph(result)

# # Plot Networkx instance of RDF Graph
# pos = nx.spring_layout(G, scale=2)
# edge_labels = nx.get_edge_attributes(G, 'r')b
# #nx.draw_networkx_edge_labels(G, pos, labels=edge_labels)
# nx.draw_networkx_edge_labels(G, pos)
# nx.draw(G, with_labels=True)


# In[3]:


pr = nx.pagerank(G,alpha=0.9)
# for key, value in pr.items():
#     print(key, ' : ', value)


# In[4]:


import pandas as pd
prdf = pd.DataFrame.from_dict(pr, orient='index')


# In[5]:


prdf.dtypes


# In[6]:


prdf.sort_values(by=0,ascending=False, inplace=True,)
prdf.head(20)


# In[7]:


nx.draw_circular(G, with_labels = False)
plt.show() # display


# In[8]:


plt.hist([v for k,v in nx.degree(G)])


# In[9]:


plt.hist(nx.centrality.betweenness_centrality(G).values())


# In[ ]:




