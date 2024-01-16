# README

## About

Directory for SPARQL queries associated with the OIH Solr UI

## Align with UI views

Look at the views in /home/fils/src/Projects/OIH/oih-ui/frontend/src/components/results/types
and make sure the queries address this elements.

## Notes

* need a SHACL test for URL that looks for the http pattern
* a sameAs points to URL, which might be text or IRI or blank.
* citation is TXT or CreativeWork

```regexp
^(https?|http):\/\/[^\s/$.?#].[^\s]*$
```

