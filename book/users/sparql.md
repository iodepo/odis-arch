---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
execution:
  allow_errors: true
---


# SPARQL

## About

This page will hold some information about the SPARQL queries we use and 
how they connect with some of the profile guidance in this document.    We will
show how this relates to and depends on the Gleaner prov as well as the 
Authoritative Reference elements of the patterns.  It is expected that the Gleaner 
prov will be present, though this can be made optional in case other 
indexing systems are used that do not provide this prov shape.    The SPARQL will 
be looking for both Gleaner prov and the Authroitative Reference elements. 

This will be different for different patterns.  For example, it might 
relate to the publisher provider elements for Creativeworks, but to 
the identity element for People and Organizations. 


```{literalinclude} ./graphs/basic.rq
:linenos:
:emphasize-lines: 11-13, 17-20, 22-27, 29-31
```

## Lines 11-13

bds 

## Lines 17-20

OPTIONAL keyword

## Lines 22-27

prov

## Lines 29-31

ORDER LIMIT OFFSET