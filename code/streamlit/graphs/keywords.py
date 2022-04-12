import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import numpy as np
import json
import geopandas
import matplotlib.pyplot as plt
import shapely
from streamlit_agraph import agraph, TripleStore, Config
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


oihdev = "https://ts.collaborium.io/blazegraph/namespace/development/sparql"

query_string = """
  prefix prov: <http://www.w3.org/ns/prov#>
  PREFIX con: <http://www.ontotext.com/connectors/lucene#>
  PREFIX luc: <http://www.ontotext.com/owlim/lucene#>
  PREFIX con-inst: <http://www.ontotext.com/connectors/lucene/instance#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX schema: <https://schema.org/>
  PREFIX schemaold: <http://schema.org/>
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

  SELECT   ( COUNT(?kw) as ?count ) ?kw
  WHERE
  {
     ?s schema:keywords ?kw
  }
  GROUP BY ?kw
  ORDER BY DESC(?count)
  """

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


def app():
  st.title("OIH Graph Test 1")
  st.sidebar.title("OIH")
  # query_type = st.sidebar.selectbox("Quey Tpye: ", ["Q1 Test"]) # could add more stuff here later on or add other endpoints in the sidebar.
  # config = Config(height=500, width=700, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True,
                  # collapsible=True)
  # if query_type=="Q1 Test":
    # st.subheader("Q1 Test")
    # with st.spinner("Loading data"):
      # store = get_inspired()
      # st.write(len(store.getNodes()))
    # st.success("Done")
    # agraph(list(store.getNodes()), (store.getEdges() ), config)

  dfkw = get_sparql_dataframe(oihdev, query_string)
  dfkw['count'] = dfkw["count"].astype(int) # convert count c to int
  # dfkw.set_index('kw', inplace=True)


  # Make Aggrid of datafram to present
  # gb = GridOptionsBuilder.from_dataframe(dfkw)
  # gb.configure_pagination()
  # gridOptions = gb.build()

  # AgGrid(dfkw, gridOptions=gridOptions,    update_mode="no_update", fit_columns_on_grid_load=True, theme="blue")
  AgGrid(dfkw, update_mode="no_update", fit_columns_on_grid_load=True, theme="blue")


  @st.cache
  def convert_df(df):
         return df.to_csv().encode('utf-8')


  csv = convert_df(dfkw)

  st.download_button(
     "Download CSV of results",
     csv,
     "OIHkeyords.csv",
     "text/csv",
     key='download-csv'
     )


if __name__ == '__main__':
    app()
