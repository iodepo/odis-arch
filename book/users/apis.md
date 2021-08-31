# APIs

## About

The Ocean InfoHub graph is accessible through several approaches.  
The graph is implemented in RDF and expressed through a standards compliant triplestore.

This triplestore exposes a SPARQL endpoint that can be queried using the [SPARQL 1.1 Query Language](http://www.w3.org/TR/rdf-sparql-query/).
To do this you can visit a web based query interface as discussed in other sections of this document.

It is also possible to access this service following RESTful principles.  

## SPARQL HTTP Protocol

One approach to this RESTful approach is to use the
[SPARQL 1.1 Graph Store HTTP Protocol](https://www.w3.org/TR/2013/REC-sparql11-http-rdf-update-20130321/).
This is a simple HTTP protocol that allows you to query the graph using SPARQL and obtain the results in JSON.

The OIH triplestore exposes the graph following this pattern for queries.

### Examples

```bash
curl -X POST https://graph.collaborium.io/blazegraph/namespace/aquadocs/sparql --data-urlencode 'query=SELECT * { ?s ?p ?o } LIMIT 1' -H 'Accept:application/sparql-results+json'
```

If run this from the command line we will get something like the following.  

```bash
✗ curl -X POST https://graph.collaborium.io/blazegraph/namespace/aquadocs/sparql --data-urlencode 'query=SELECT * { ?s ?p ?o } LIMIT 1' -H 'Accept:application/sparql-results+json'

{
  "head" : {
    "vars" : [ "s", "p", "o" ]
  },
  "results" : {
    "bindings" : [ {
      "s" : {
        "type" : "uri",
        "value" : "https://hdl.handle.net/1834/10030"
      },
      "p" : {
        "type" : "uri",
        "value" : "https://schema.org/propertyID"
      },
      "o" : {
        "type" : "literal",
        "value" : "https://hdl.handle.net/"
      }
    } ]
  }
}                                   
```

While this is unlikely how you will want to interact with the graph, 
it desmonstrates the HTTP based access API that can be used in tools, notebooks
or other applications.

This is the same basic approach the used in the web client.  There the 
axios library (https://axios-http.com/) is used with a code snippet like:

```javascript

 axios.get(url.toString())
      .then(function (response) {
        // handle success
        console.log(response);
        const el = document.querySelector('#container2');
        render(showresults(response), el);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      })
      .then(function () {
        // always executed
      });

```

