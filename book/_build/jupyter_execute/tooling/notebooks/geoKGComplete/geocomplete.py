#!/usr/bin/env python
# coding: utf-8

# # Geospatial KG Completion
# 

# ## About
# 
# This is a simple test notebook to explore approachs to associating geometries in the OIH graph with named ocean regions.
# From Marine Regions (https://www.marineregions.org/) we downloaded the IHO Sea Areas dataset.  This is a shapefile that is converted to WKT and loaded into a geopandas dataframe.    
#  
#  
# We then create a few points to compare against this.   In this test we are only comparing points to the polygons.  So this is what is called a "point in polygon" test.   Later revisions to this could do polygon intersection or other tests.  This is only a proof of concept notebook.
# 
# We then generate a new dataframe based on the matches.   These matches could then be fed back into the graph as a sort of "Knowledge Graph Completion" workflow.  Alternatively we can do gepsparql calls based on the sea WKT strings and do the search in the geosparql aware triple store.  
# 
# ## References
# * https://geopandas.org/docs/user_guide/set_operations.html
# * https://geopandas.org/docs/user_guide/geocoding.html
# * https://medium.com/analytics-vidhya/point-in-polygon-analysis-using-python-geopandas-27ea67888bff

# In[143]:


#@title
# !apt-get install libproj-dev proj-data proj-bin
# !apt-get install libgeos-dev
get_ipython().system('pip install -q cython')
get_ipython().system('pip install -q cartopy')
get_ipython().system('pip install -q SPARQLWrapper')
get_ipython().system('pip install -q rdflib')
get_ipython().system('pip install -q geopandas')
get_ipython().system('pip install -q contextily==1.0rc2')
get_ipython().system('pip install -q rtree')
get_ipython().system('pip install -q pygeos')


# In[144]:


from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import numpy as np
import json
import geopandas
import matplotlib.pyplot as plt
import shapely

#dbsparql = "http://dbpedia.org/sparql"
# ufokn = "http://graph.collaborium.io/blazegraph/namespace/oihdev/sparql"


# In[166]:


# Point in Polygon function from the cited Vidhya reference.  A few small changes
# to align with our dataframes here

def get_pip (gdf, regions):
    r_list = list(regions.NAME)
    #create empty dataframe
    df = pd.DataFrame().reindex_like(gdf).dropna()
    for r in r_list:
        #get geometry for specific region
        pol = (regions.loc[regions.NAME==r])
        pol.reset_index(drop = True, inplace = True)
        #identify those records from gdf that are intersecting with the region polygon
        pip_mask = gdf.within(pol.loc[0, 'WKT'])
        #filter gdf to keep only the intersecting records
        pip_data = gdf.loc[pip_mask].copy()
        #create a new column and assign the region name as the value
        pip_data['region']= r
        #append region data to empty dataframe
        df = df.append(pip_data)
    #checking there are no more than one region assigned to an event    
    print('Original dataframe count=',len(gdf),'\nNew dataframe count=', len(df))
    if df.loc[df.id.duplicated() == True].shape[0] > 0:
        print("There are id's with more than one region")
    #checking all events have a region
    elif gdf.loc[~gdf.id.isin(df.id)].shape[0] > 0:
        print("There are id's without an assigned region")
    else:
        print("No discrepancies in results!")
    df.reset_index(inplace=True, drop=True)
    df = df.drop(columns='geometry')
    return df


# In[167]:


# load CSV into pandas that holds the WKT strings for the world seas dataset
df = pd.read_csv('./World_Seas_IHO_v3/out.wkt/World_Seas_IHO_v3.csv')  
# df.head(2)


# In[168]:


# convert the WKT strings to WKT geometry
from shapely import wkt
df['WKT'] = df['WKT'].apply(wkt.loads)


# In[169]:


# Load and plot the ocean regions
import contextily as ctx

# Make geopandas from df
gdf = geopandas.GeoDataFrame(df, geometry='WKT', crs={"init": "epsg:3857"}) # contextily requires 3875?
# gdf.head(2)


# In[177]:


# Make geopandas from GeoJSON of the world for plot
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
dftx = geopandas.read_file(url)

# plot
ax = dftx.plot(color='white', edgecolor='black', figsize=(25,15))
gdf.plot(ax=ax, edgecolor='black', color='lightblue')
plt.savefig('map.png')


# In[171]:


# Make test datarame with some lat long pairs to test
# Later these will come from SPARQL calls to the OIH graph

df = pd.DataFrame({ 'Latitude': [38, -1,  -37,  -22,14],
                   'Longitude': [-146, 0, 129,  37,85], 
                   'id':["Off US West Coast","Atlantic","South of Australia", "Africa","Near India"]})

testdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))


# In[155]:


# Call the function and do pip calculations
eq_df = get_pip(testdf, gdf)


# ## Conclusion
# 
# The generated dataframe holds the matches of the test Lat Long pairs to the named seas from the reference shape file.
# These results couild be fed back into the graph as keywords or items from a known list of terms for more explicate relation mapping.
# 
# Specifically,  someting like https://schema.org/DefinedTerm where the property https://schema.org/DefinedTermSet would point back to the Marine Regions source documents and URL.   Similarly these resources could be connected up to WikiData in a similar manner.   
# 
# ```
#         {
#                 "@type": "DefinedTermSet",
#                 "@id": "http://geonetwork.vliz.be/geonetwork/srv/eng/catalog.search#/metadata/f4cfa278-730f-4646-b6cc-a3dceaa3a1e5",
#                 "name": "IHO Sea Areas"
#         },
#         {
#                 "@type": "DefinedTerm",
#                 "name": "Bay of Bengal",
#                 "description": "IHO Sea Area Bay of Bengal",
#                 "inDefinedTermSet": "http://geonetwork.vliz.be/geonetwork/srv/eng/catalog.search#/metadata/f4cfa278-730f-4646-b6cc-a3dceaa3a1e5"
#         },
# ```
# 
# For reference the WikiData resource is: https://www.wikidata.org/wiki/Q38684 which is an instance of "body of water".  So leveraging this type and the IHO names should allow relatively reliable link detection.   Leveraging the top level Thing class in schema.org we would be looking at a simple
# 
# ```
#     "sameAs": "https://www.wikidata.org/wiki/Q38684",
# ```
# 
# in the DefinedTerm type.
# 
# In the final listing below the "id" is the just the random string I associated with the test lat longs. I used a simple online map to just pick some random locations and gave them names.   The "region" cames from the offical Marine Regions file.  

# In[142]:


eq_df.head()


# In[ ]:




