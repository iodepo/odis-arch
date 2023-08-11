# Graph Exploration

## About

This document describes current approaches to working with the OIH graph.   At present these include

* The Release Graph:   A published and citable version of the graph for use on a local computer
* The SPARQL endpoint:  A public SPARQL endpoint to explore the graph with
* Example SPARQL queries:  A growing collection of quries for us with the above two resoures

## Release Graphs

The release graph page can be found at:  https://github.com/iodepo/odis-arch/tree/master/docs/releases

The release graphs are collections of the data graph resources for each provider provided on a public
S3 compatible object store.  There are also HTTP URLs for each of these as well.  

### Notebook

A draft notebook is underdevelopment at https://github.com/gleanerio/notebooks/blob/master/notebooks/datastore/loadToMemory.ipynb

At present all this does is load the graphs from the server into a memory based RDF graph server.  From there you can issue
queries against the graph just like you would with the SPARQL endpoint.  Since this system is not indexed the performance can
be a bit slower than the dedicated server.

However, the advantage is that you can more easily iterate on queries, and you don't have to share the server with others 
who many be running competing queries.   Also, the current Blazegraph server in use with OIH is prone to memory 
issues with complex queries.

The biggest advantage is that complex queries that run for a long time on the public sever will be cancelled after a 
certain period to prevent runaway queries going on for long periods effectively making the server unresponsive to 
others while it runs.  The local instance has no such limit so complex queries can be left to run for extended periods.  

## SPARQL endpoint

The SPARQL endpoint can be found at:   http://graph.oceaninfohub.org/blazegraph/#splash

Make sure to go to the "Namespace" tab first and make sure the OIH namespace is ```in use```. 

![blazenamespace.png](images%2Fblazenamespace.png)

## SPARQL queries 

There are examples of SPARQL queries at  https://github.com/iodepo/odis-arch/tree/master/code/SPARQL

Use https://www.w3.org/TR/sparql11-overview/ and https://www.w3.org/TR/2013/REC-sparql11-query-20130321/ 
as guides to SPARQL.


### Notes

* Use of the ```LIMIT 1000``` directive allows you to set a number of records, here 1000, to return.  This can be useful
when testing a query.