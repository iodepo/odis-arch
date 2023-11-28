# Validation

## About

This section contains some initial work on developing some validation
approaches for OIH.  The focus initially is not on validating approaches with
the full publishing guidance.  Rather the focuses is on the the "info hub" as a
search application and develops validation to support that.

### Well Formed JSON-LD 

[SDO Validator](https://validator.schema.org/)

[Structured data Linter](http://linter.structured-data.org/)

[JSON-LD Playground](https://json-ld.org/playground/)


### Shape Validation

Initial approach:

* Develop a base SHACL document that assess a data graph based on elements needed to support search
* [SHACL](https://www.w3.org/TR/shacl/)
* Leverage [SHACL Playground](https://shacl.org/playground/)
* RDFShape at [https://rdfshape.weso.es/](https://rdfshape.weso.es/) and [https://rdfshape.herokuapp.com/](https://rdfshape.herokuapp.com/) 
  
To support this will need an initial data graph to work with.  The type is not
important.  All types will need to satisfy the search needs.

Examples of these needs include:

* Have an @id
* Have a name
* Have a description
* Have a Distribution and contentURL
* Reference authority



