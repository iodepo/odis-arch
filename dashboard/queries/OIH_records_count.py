#!/usr/bin/env python
# coding: utf-8

# # OIH Queries 
# 
# What follows are some example SPARQL queries used in OIH for the test interface
# 

# ## Setup and inits

# ### Imports

from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
# import dask, boto3
# import dask.dataframe as dd
import numpy as np
import json
import geopandas
import matplotlib.pyplot as plt
import shapely
# import kglab as kg

oih = "https://ts.collaborium.io/blazegraph/namespace/oih/sparql"
oihdev = "https://ts.collaborium.io/blazegraph/namespace/development/sparql"
oihinvemar = "https://ts.collaborium.io/blazegraph/namespace/invemar/sparql"
oihad = "https://graph.collaborium.io/blazegraph/namespace/aquadocs/sparql"


# ### Support Functions

#@title
def get_sparql_dataframe(service, query):
    """
    Helper function to convert SPARQL results into a Pandas data frame.
    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return pd.DataFrame(out, columns=cols)


# ## Queries
# 
# What follows is a set of queries designed to provide a feel for the OIH graph

# ### Simple Count
# 
# How many triples are there?

rq_count = """SELECT (COUNT(*) as ?Triples) 
WHERE 
  {
      { ?s ?p ?o } 
  }
"""


dfsc = get_sparql_dataframe(oihdev, rq_count)
dfsc.head()




