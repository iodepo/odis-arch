#!/usr/bin/env python
# coding: utf-8

# # OIH Queries 
# 
# What follows are some example SPARQL queries used in OIH for the test interface
# 

# ## Setup and inits

# ### Imports

# In[1]:


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

# In[23]:


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

# In[24]:


rq_count = """SELECT (COUNT(*) as ?Triples) 
WHERE 
  {
      { ?s ?p ?o } 
  }
"""


# In[25]:


dfsc = get_sparql_dataframe(oihdev, rq_count)
dfsc.head()


# ## Simple org list  (not done)
# 

# In[26]:


rq_orgs = """SELECT (COUNT(*) as ?Triples) 
WHERE 
  {
      { ?s ?p ?o } 
  }
"""


# In[27]:


dfsc = get_sparql_dataframe(oihdev, rq_orgs)
dfsc.head()


# ### Predicate Counts
# 
# This gives an overview of unique predicates that connect a subject to an object.  This gives us both an idea of the properties we are using on things and count of their usage.
# 

# In[28]:


rq_pcount = """SELECT ?p (COUNT(?p) as ?pCount)
WHERE
{
  ?s ?p ?o .
}
GROUP BY ?p
"""


# In[29]:


dfc = get_sparql_dataframe(oihdev, rq_pcount)
dfc['pCount'] = dfc["pCount"].astype(int) # convert count to int
# dfc.set_index('p', inplace=True)


# In[30]:


dfc_sorted = dfc.sort_values('pCount', ascending=False)
dfc_sorted.head(10)


# In[31]:


rcount = len(dfc_sorted)
print(rcount)


# In[32]:


ts = dfc_sorted.tail(38)['pCount'].sum()
print(ts)


# In[33]:


hs = dfc_sorted.head(10)
hs.append({'p':'Other','pCount':ts}, ignore_index=True) 
hs.set_index('p', inplace=True)
hs.head(10)


# In[34]:


plot = hs.plot.pie(y='pCount',x='p',legend=False, figsize=(10, 10))


# ### OIH Base Query

# In[35]:


rq_main = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT ?g  ?s   ?type ?score ?name ?url ?lit ?description ?headline
        WHERE
        {
           ?lit bds:search "coral" .
           ?lit bds:matchAllTerms "false" .
           ?lit bds:relevance ?score .
           graph ?g {
            ?s ?p ?lit .
            ?s rdf:type ?type . 
            OPTIONAL { ?s schema:name ?name .   }
            OPTIONAL { ?s schema:headline ?headline .   }
            OPTIONAL { ?s schema:url ?url .   }
            OPTIONAL { ?s schema:description ?description .    }
          }

        }
        ORDER BY DESC(?score)
        LIMIT 30
        OFFSET 0
        """


# In[36]:


df = get_sparql_dataframe(oihdev, rq_main)
df.head(5)


# ### OIH Gleaner Query

# In[37]:


rq_maingl = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT ?g  ?s  ?wat ?orgname ?domain ?type ?score ?name ?url ?lit ?description ?headline
        WHERE
        {
           ?lit bds:search "coral" .
           ?lit bds:matchAllTerms "false" .
           ?lit bds:relevance ?score .
           graph ?g {
            ?s ?p ?lit .
            ?s rdf:type ?type . 
            OPTIONAL { ?s schema:name ?name .   }
            OPTIONAL { ?s schema:headline ?headline .   }
            OPTIONAL { ?s schema:url ?url .   }
            OPTIONAL { ?s schema:description ?description .    }
          }
           ?sp prov:generated ?g  .
           ?sp prov:used ?used .
           ?used prov:hadMember ?hm .
           ?hm prov:wasAttributedTo ?wat .
           ?wat rdf:name ?orgname .
           ?wat rdfs:seeAlso ?domain
        }
        ORDER BY DESC(?score)
        LIMIT 30
        OFFSET 0
        """


# In[38]:


df = get_sparql_dataframe(oihdev, rq_maingl)
df.head(5)


# ## Query for prov
# 
# Count (count(distinct ?tag) as ?count) 
# 
# Need to look for the date in the prov record too.  I keep it by day granularity, so I should be able to see the difference if I focos on a specific repo or look over the dates

# In[78]:


rq_prov = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

       SELECT   ( COUNT(?hm) as ?count) ?wat  ?orgname ?domain
        WHERE
        {
           ?hm prov:wasAttributedTo ?wat .
           ?wat rdf:name ?orgname .
           ?wat rdfs:seeAlso ?domain
        }
        GROUP BY ?wat ?orgname ?domain
        """


# In[79]:


rq_prov2 = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT ( COUNT(?s) as ?count) ?wat  ?orgname ?domain
        WHERE
        {
           graph ?g {
             VALUES (?type) { ( schema:CreativeWork ) ( schema:Map )  ( schema:Person )  ( schema:Organization )  ( schema:Dataset )  ( schema:Course ) } 
            ?s rdf:type ?type . 
            OPTIONAL { ?s schema:name ?name .   }
            OPTIONAL { ?s schema:headline ?headline .   }
            OPTIONAL { ?s schema:url ?url .   }
            OPTIONAL { ?s schema:description ?description .    }
          }
           ?sp prov:generated ?g  .
           ?sp prov:used ?used .
           ?used prov:hadMember ?hm .
           ?hm prov:wasAttributedTo ?wat .
           ?wat rdf:name ?orgname .
           ?wat rdfs:seeAlso ?domain
        }
                GROUP BY ?wat ?orgname ?domain

        """


# In[83]:


dfp = get_sparql_dataframe(oihdev, rq_prov)
dfp['count'] = dfp["count"].astype(int) # convert count c to int
dfp.set_index('orgname', inplace=True)
dfp


# In[42]:


plot = dfp.plot.pie(y='count',legend=False, figsize=(10, 10))


# In[ ]:


rq_provdate = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

 
       SELECT   ( COUNT(?s) as ?count) ?time ?orgname
        WHERE
        {
           ?s a prov:Activity  .
           ?s prov:endedAtTime ?time .
           ?s prov:generated ?gen .
           ?s prov:used ?used .
           ?used prov:hadMember ?mem .
           ?mem prov:wasAttributedTo ?wat .
           ?wat rdf:name ?orgname .
           ?wat rdfs:seeAlso ?domain
        }
        GROUP BY ?time ?orgname  
        """

dfpd = get_sparql_dataframe(oihdev, rq_provdate)


# In[ ]:


dfpd.head(30)


# In[49]:


dfpd.info()


# In[50]:


# dfpd = get_sparql_dataframe(oihdev, rq_provdate)
dfpd['count'] = dfpd["count"].astype(int) # convert count c to int
dfpd['time'] = pd.to_datetime(dfpd['time'])
dftime = dfpd.sort_values(by='time') 
# dfpd['time'] = dfpd['time'].astype('datetime64[ns]')
# dfpd.set_index('time', inplace=True)


# In[51]:


dftime.set_index('time', inplace=True)

dftime.head(20)


# In[52]:


ax = dftime.plot.bar(rot=80, stacked=True, figsize=(15, 5))


# ## Feed query
# 
# Goal here is see if the prov will give us the elements for an RSS feed.  
# The [RSS specs](https://validator.w3.org/feed/docs/rss2.html) give us the elements we need to populate.  Focus on; title(name), date, author, description
# 
# A recent example from gov at https://www.govinfo.gov/feeds
# 
# Since this could be very large injest, do it by the ingest events above instead?
# 
# * Element 	Description 	Example
# * title 	The title of the item. 	Venice Film Festival Tries to Quit Sinking
# * link 	The URL of the item. 	http://www.nytimes.com/2002/09/07/movies/07FEST.html
# * description 	The item synopsis. 	Some of the most heated chatter at the Venice Film Festival this week was about the way that the arrival of the stars at the Palazzo del Cinema was being staged.
# * author 	Email address of the author of the item. More. 	oprah@oxygen.net
# * category 	Includes the item in one or more categories. More. 	Simpsons Characters
# * comments 	URL of a page for comments relating to the item. More. 	http://www.myblog.org/cgi-local/mt/mt-comments.cgi?entry_id=290
# * enclosure 	Describes a media object that is attached to the item. More. 	<enclosure url="http://live.curry.com/mp3/celebritySCms.mp3" length="1069871" type="audio/mpeg"/>
# * guid 	A string that uniquely identifies the item. More. 	<guid isPermaLink="true">http://inessential.com/2002/09/01.php#a2</guid>
# * pubDate 	Indicates when the item was published. More. 	Sun, 19 May 2002 15:21:36 GMT
# * source 	The RSS channel that the item came from. More. 	<source url="http://www.quotationspage.com/data/qotd.rss">Quotes of the Day</source>

# In[28]:


rq_provdatelist = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

       SELECT  ?time ?orgname ?memval  ?memname ?memdesc
        WHERE
        {
           ?s prov:endedAtTime ?time .
           ?s prov:generated ?gen .
           ?s prov:used ?used .
           ?used prov:hadMember ?mem .
           ?mem prov:value ?memval .
           ?mem schema:name ?memname .
           ?mem schema:description ?memdesc .
           ?mem prov:wasAttributedTo ?wat .
           ?wat rdf:name ?orgname .
        }
        ORDER BY DESC(?time) ASC(?memname)
        LIMIT 1000

        """

         #            ?s a prov:Activity  .

         #   ?wat rdfs:seeAlso ?domain


# In[29]:


get_ipython().run_cell_magic('time', '', 'dfpl = get_sparql_dataframe(oihdev, rq_provdatelist)\ndfpl.head(10)')


# ## Keywords

# In[27]:


rq_keywords = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

       SELECT   ( COUNT(?kw) as ?count) ?kw   
        WHERE
        {
           ?s schema:keywords ?kw
        }
        GROUP BY ?kw  
        ORDER BY DESC(?count)
        """


# In[28]:


dfkw = get_sparql_dataframe(oihdev, rq_keywords)
dfkw['count'] = dfkw["count"].astype(int) # convert count c to int
dfkw.set_index('kw', inplace=True)
dfkw.head(10)


# In[31]:


dfkw.to_csv('keywords.csv', index=False)


# ## Types Breakdown
# 

# In[86]:


rq_types = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

 
       SELECT   ( COUNT(?type) as ?count) ?type   
        WHERE
        {
        
           ?s rdf:type ?type
           FILTER ( ?type IN (schema:ResearchProject, schema:Project, schema:Organization, schema:Dataset, schema:CreativeWork, schema:Person, schema:Map, schema:Course, schema:CourseInstance, schema:Event, schema:Vehicle) )

        }
        GROUP BY ?type  
        ORDER BY DESC(?count)
        """



# In[87]:


dft = get_sparql_dataframe(oihdev, rq_types)
dft['count'] = dft["count"].astype(int) # convert count c to int
dft.set_index('type', inplace=True)
dft.head(10)


# In[67]:


plot_t = dft.plot.pie(y='count',legend=False, figsize=(12, 12))


# In[84]:


rq_typesCHECK = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

 
       SELECT  ( COUNT(?type) as ?count) ?type   
        WHERE
         {
           graph ?g {
            
            ?s rdf:type ?type . 
            OPTIONAL { ?s schema:name ?name .   }
            OPTIONAL { ?s schema:headline ?headline .   }
            OPTIONAL { ?s schema:url ?url .   }
            OPTIONAL { ?s schema:description ?description .    }
          }
           ?sp prov:generated ?g  .
           ?sp prov:used ?used .
           ?used prov:hadMember ?hm .
           ?hm prov:wasAttributedTo ?wat .
          
        }
        GROUP BY ?type  
         ORDER BY DESC(?count)
   
        """

#      GROUP BY ?type  
#         ORDER BY DESC(?count)

#  ( COUNT(?type) as ?count) ?type  

# ?s ?p ?lit .

#  ?wat rdf:name "Ocean Biodiversity Information System" .


# In[85]:


dft = get_sparql_dataframe(oihdev, rq_typesCHECK)
# dft['count'] = dft["count"].astype(int) # convert count c to int
# dft.set_index('type', inplace=True)
dft.head(20)


# ## Check status of spatial predicates
# 
# We have 3500+ items with spatial data using the scheme.org vocabulary.   No current data published using the geosparql WKT patterns.  

# In[35]:


rq_wktcount = """SELECT (COUNT(?s) as ?sCount)
WHERE
{
  {
  ?s <http://www.opengis.net/ont/geosparql#hasGeometry> ?o .
}
UNION
{
  ?s <https://schema.org/spatialCoverage> ?o
  }
}
"""


# In[36]:


dfwc = get_sparql_dataframe(oihdev, rq_wktcount)
dfwc['sCount'] = dfwc["sCount"].astype(int) # convert count to int
# dfc.set_index('p', inplace=True)


# In[37]:


dfwc.head()


# In[46]:


rq_dups = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

 
       SELECT   ( COUNT(?name) as ?count) ?name   
        WHERE
        {
          ?s rdf:type ?type
           FILTER ( ?type IN ( schema:Dataset, schema:CreativeWork) )
           ?s schema:name ?name

        }
        GROUP BY ?name  
        HAVING (?count > 1)
        ORDER BY DESC(?count)
        """


dfdp = get_sparql_dataframe(oihdev, rq_dups)
dfdp['count'] = dfdp["count"].astype(int) # convert count c to int
dfdp.set_index('name', inplace=True)
dfdp.info()
dfdp.head(10)


# In[90]:


qex1 = """PREFIX prov: <http://www.w3.org/ns/prov#> .
PREFIX con: <http://www.ontotext.com/connectors/lucene#> .
PREFIX luc: <http://www.ontotext.com/owlim/lucene#> .
PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#> .
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
PREFIX schema: <https://schema.org/> .
PREFIX schemaold: <http://schema.org/> .
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

SELECT DISTINCT ?s  ?name  
WHERE
        {
           ?lit bds:search "A General formatting system for geo-referenced data" .
           ?lit bds:matchAllTerms "false" .

           graph ?g {
            ?s ?p ?lit .
            FILTER isIRI(?s)
             OPTIONAL { ?s schema:name ?name .   }
           }
        }
GROUP BY    ?name ?s
LIMIT 300
OFFSET 0
"""


# ## OIH Query "lens"
# 
# Exploring how sites like http://portete.invemar.org.co/chm#/table could leverage OIH. Searches like "acidification"  A popular return for that search is https://aquadocs.org/handle/1834/9819 which is found in the OIH graph via [this search](https://oceans.collaborium.io/?search=Optimizaci%C3%B3n+de+los+procesos+de+ensilado+a+partir+de+residuos+de+la+industria+pesquera+y+evaluaci%C3%B3n+de+nuevas+aplicaciones+en+la+alimentaci%C3%B3n+animal.).
# 
# The thought is what would a search site do via the OIH graph that might be interesting.  We can think about looking for the types associated with a result and then seeing what the next level result would be.   
# 
# 

# In[7]:


lens1 = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT  ?t ?ttype ?name
        WHERE

        {
           ?s ?p "https://www.oceandocs.org/handle/1834/9819" .
           ?s ?pp ?t .
           ?t a ?ttype .
           ?t schema:name ?name
  
  }
  """

dflens1 = get_sparql_dataframe(oihdev, lens1)
dflens1.head(10)


# In[8]:


lens2 = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT  ?us ?up ?ao ?uus ?uup
        WHERE

        {
           ?s ?p "https://www.oceandocs.org/handle/1834/9819" .
              ?s <https://schema.org/author> ?auth .
              ?auth <https://schema.org/name> ?ao .
 
              ?us ?up ?ao .
              ?uus ?uo ?us
  
  }
  """

dflens1 = get_sparql_dataframe(oihdev, lens2)
dflens1.head(10)


# In[11]:


lens3 = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

 
       SELECT ?itemp ?itemo
        WHERE
        {
        
           ?s rdf:type 	<https://schema.org/Vehicle> .
            ?s 	<https://schema.org/itemListElement> ?le .
                ?le ?lep ?item .
           ?item ?itemp ?itemo
        }
 
  """

dflens1 = get_sparql_dataframe(oihinvemar, lens3)
dflens1.head(10)


# In[ ]:




