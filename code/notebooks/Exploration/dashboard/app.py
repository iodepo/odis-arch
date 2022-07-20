

# ### Imports

import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
# import dask, boto3
# import dask.dataframe as dd
import numpy as np
import json
import geopandas
import matplotlib.pyplot as plt
import shapely
import time
import matplotlib.dates as mdates
from datetime import datetime
# import kglab as kg

oih = "https://ts.collaborium.io/blazegraph/namespace/oih/sparql"
oihdev = "https://ts.collaborium.io/blazegraph/namespace/development/sparql"
oihinvemar = "https://ts.collaborium.io/blazegraph/namespace/invemar/sparql"
oihad = "https://graph.collaborium.io/blazegraph/namespace/aquadocs/sparql"

#### Support Functions

#@title
@st.cache(allow_output_mutation=True)
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


### Queries
# 
# What follows is a set of queries designed to provide a feel 
# for the OIH graph

#### Simple Count
# 
# How many triples are there?

rq_count = """SELECT (COUNT(*) as ?Triples) 
WHERE 
  {
      { ?s ?p ?o } 
  }
"""

#@st.cache(allow_output_mutation=True)
dfCount = get_sparql_dataframe(oihdev, rq_count)
#dfCount["Triples"] = dfCount["Triples"].astype(int) # convert count c to int

#### List of orgs

rq_orgs = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

          SELECT ?orgname
            WHERE 
             {
               ?wat rdf:name ?orgname
             }
            ORDER BY ASC(?orgname)
          """
#@st.cache(allow_output_mutation=True)
dfOrgs = get_sparql_dataframe(oihdev, rq_orgs)

#### PROV: count of catalogues

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

#@st.cache(allow_output_mutation=True)     
dfProv = get_sparql_dataframe(oihdev, rq_prov)
dfProv['count'] = dfProv["count"].astype(int) # convert count c to int
#dfProv.info()
#dfProv.set_index('orgname', inplace=True)

#### Types (patterns)
     
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
        
           ?s rdf:type ?type .
           FILTER ( ?type IN (schema:ResearchProject, schema:Project, schema:Organization, schema:Dataset, schema:CreativeWork, schema:Person, schema:Map, schema:Course, schema:CourseInstance, schema:Event, schema:Vehicle) )

        }
        GROUP BY ?type  
        ORDER BY DESC(?count)
        """

#@st.cache(allow_output_mutation=True)        
dfTypes = get_sparql_dataframe(oihdev, rq_types)
dfTypes['count'] = dfTypes["count"].astype(int) # convert count c to int
dfTypes.set_index('type', inplace=True)
#dfTypes.head(10)

#### Keywords

rq_keywords = """prefix prov: <http://www.w3.org/ns/prov#>
        PREFIX con: <http://www.ontotext.com/connectors/lucene#>
        PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
        PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX schema: <https://schema.org/>
        PREFIX schemaold: <http://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT  ?keywords  ( COUNT(?keywords) as ?count )  
        WHERE
        {
           ?s schema:keywords ?keywords
        }
        GROUP BY ?keywords  
        ORDER BY DESC(?count)
        """

#@st.cache(allow_output_mutation=True)
dfKeywords = get_sparql_dataframe(oihdev, rq_keywords)
dfKeywords['count'] = dfKeywords["count"].astype(int) # convert count c to int
dfKeywords.set_index('keywords', inplace=True)
#dfKeywords.head(10)

######
# page setup
######

#st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="ODIS Dashboard",
    page_icon="https://oceaninfohub.org/wp-content/uploads/2020/11/logo-only_OIH_EPS-CMYK-100x100.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
         'Report a bug': "https://github.com/iodepo/odis-arch",
         'Get Help': 'https://oceaninfohub.org/contact-2/',         
         'About': "Dashboard demo by [jmckenna](https://github.com/jmckenna)"
    }   
)

# dashboard title
st.title("ODIS Dashboard")

with st.expander("ODIS Node Summary", expanded=True):

    #use markdown trick, as st.expander label cannot be styled
    #      see https://github.com/streamlit/streamlit/issues/2056
    st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
      font-size: large;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # top-level filters
    #node_filter = st.selectbox("Select an ODIS node", ("Marine Training EU", "AquaDocs", "Ocean Biodiversity Information System", "Ocean Best Practices", "OceanExpert UNESCO/IOC Project Office for IODE", "EDMO SeaDataNet", "EDMERP SeaDataNet", "INVEMAR documents", "INVEMAR Experts", "INVEMAR institution", "INVEMAR training", "INVEMAR vessel"))
    node_filter = st.selectbox("Select an ODIS node", dfOrgs, index=10)

    # creating a single-element container
    placeholder = st.empty()

    # dataframe filter
    dfProvFilter = dfProv[dfProv.orgname == node_filter]

    with placeholder.container():

        # create three columns
        nodeCol1, nodeCol2, nodeCol3, nodeCol4 = st.columns(4, gap="medium")

        with nodeCol1:
            st.write("Types indexed")
            rq_types_org1 = """prefix prov: <http://www.w3.org/ns/prov#>
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
        
                     ?s rdf:type ?type .
                     ?wat rdf:name ?orgname .
                     FILTER ( ?type IN (schema:ResearchProject, schema:Project, schema:Organization, schema:Dataset, schema:CreativeWork, schema:Person, schema:Map, schema:Course, schema:CourseInstance, schema:Event, schema:Vehicle) )
                   """
            rq_types_org2 = "FILTER (?orgname = '" + node_filter + "') ."
            rq_types_org3 = """                   
                   }
                   GROUP BY ?type  
                   ORDER BY DESC(?count)
                   """
        
            #@st.cache(allow_output_mutation=True)
            dfTypesOrg = get_sparql_dataframe(oihdev, rq_types_org1 + rq_types_org2 + rq_types_org3)
            dfTypesOrg['count'] = dfTypesOrg["count"].astype(int) # convert count c to int
            dfTypesOrg.set_index('type', inplace=True)
            st.write(dfTypesOrg.head(10))

        with nodeCol2:
            st.write("Keywords")
            rq_keywords_org1 = """prefix prov: <http://www.w3.org/ns/prov#>
                PREFIX con: <http://www.ontotext.com/connectors/lucene#>
                PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
                PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                PREFIX schema: <https://schema.org/>
                PREFIX schemaold: <http://schema.org/>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

                SELECT DISTINCT  ?keywords  ( COUNT(?keywords) as ?count )
                WHERE
                {
                   ?s schema:keywords ?keywords .
                   ?wat rdf:name ?orgname .
                """
        
            rq_keywords_org2 = "FILTER (?orgname = '" + node_filter + "') ."
            rq_keywords_org3 = """        }
                GROUP BY ?keywords
                ORDER BY DESC(?count)
                """        
            #@st.cache(allow_output_mutation=True)
            dfKeywordsOrg = get_sparql_dataframe(oihdev, rq_keywords_org1 + rq_keywords_org2 + rq_keywords_org3)
            dfKeywordsOrg['count'] = dfKeywordsOrg["count"].astype(int) # convert count c to int
            dfKeywordsOrg.set_index('keywords', inplace=True)
            #st.write(rq_keywords_org1 + rq_keywords_org2 + rq_keywords_org3)
            st.write(dfKeywordsOrg.head(10))  

        with nodeCol3:
            st.write("Number of Catalogues")
            st.subheader(dfProvFilter['count'].sum())
            
        with nodeCol4:
            st.write("Date indexed to Graph")
            df = pd.read_csv('/home/apps/odis-arch-git/code/notebooks/diagrams/data/oihSources.csv')
            names = df['propername'].tolist()
            dates = df['dates'].tolist()
            # Convert date strings (e.g. 2014-10-18) to datetime
            dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
            if "INVEMAR" in node_filter: 
                mask = df['propername'].values ==  "INVEMAR"
            else:
                mask = df['propername'].values ==  node_filter
            df_orgDate = df[mask]
            st.subheader(df_orgDate['dates'].values[0])

# Summary

#st.header("ODIS Graph Summary")
with st.expander("ODIS Graph Summary", expanded=False):

    #use markdown trick, as st.expander label cannot be styled
    #      see https://github.com/streamlit/streamlit/issues/2056
    st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
      font-size: large;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    sumCol1, sumCol2, sumCol3 = st.columns(3, gap="medium")

    with sumCol1:
        st.write("Size of ODIS graph")
        st.subheader(dfCount['Triples'].values[0] + " triples")

    with sumCol2:
        st.write("Number of Nodes")
        st.subheader(len(dfOrgs))

    with sumCol3:
        st.write("Number of Catalogues")
        st.subheader(dfProv['count'].sum())
    
    sumCol4, sumCol5, sumCol6 = st.columns(3, gap="medium")

    with sumCol4:
        st.write("Types indexed")
        st.write(dfTypes.head(10))

    with sumCol5:
        st.write("Timeline: when added to Graph")
        #st.write(dfProv.plot.pie(y='count',legend=False, figsize=(10, 10)))
        #st.pyplot() 
        df = pd.read_csv('/home/apps/odis-arch-git/code/notebooks/diagrams/data/oihSources.csv')
        names = df['propername'].tolist()
        dates = df['dates'].tolist()
        # Convert date strings (e.g. 2014-10-18) to datetime
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
        st.dataframe(data=df, width=None, height=None)

    with sumCol6:
        st.write("Keywords")
        st.write(dfKeywords.head(10))   

with st.expander("About the Dashboard", expanded=False):

    #use markdown trick, as st.expander label cannot be styled
    #      see https://github.com/streamlit/streamlit/issues/2056
    st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
      font-size: large;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.markdown("""
         The ODIS (Ocean Data and Information System) Dashboard 
         shows live queries related to 
         the ODIS Graph, including describing each node in the 
         network.  More information about how to connect to the
         ODIS network can be found at [https://book.oceaninfohub.org/](https://book.oceaninfohub.org/)
    """)
    st.image("https://oceaninfohub.org/wp-content/uploads/2020/12/logo_OIH_PNG-RGB-1.png", width=300)
