# README

## About

Documentation on implementing schema.org for the Ocean Info Hub (OIH) to facility the indexing and discovery 
of resources.  The approach leverages schema.org as a base.  Schema.org or is a community effort and widely
implemented by commercial search services.  The approach is based on web standards and best practices and 
facilities development of community index services.  


## Publishing and Indexing Notes

The stages of the data flow include the authoring, publishing and harvesting or indexing of the published resources. The following sections break these out and provide guidance.

* [Authoring](authoring.md): Guidance on the creation of the JSON-LD data graphs.  Links to documentation
  and tools to validate.
* [Publishing](publishing.md):  The data graphs need to be associated with web resources and exposed
  via sitemaps and robots.txt.
* [Indexing](indexers.md): How to building indexes from information published following structured data on the web practices.  The approaches used by OIH can be leveraged both by commercial indexing services as well as community managed resources.
* [Background](background.md) information on the OIH architecture and some previous work.  This document will likely be incorporated into the above three documents and removed.

## Thematic Areas

Thematic areas represent of a set of profiles defined by the OIH community.  These profiles provide
a set of minimal elements an author should include as well as more detailed elements that can offer
enhanced capacity.

* [Documents](./docs/README.md)
* [Projects](./projects/README.md)
* [Training](./training/README.md)
* [Vessels](./vessels/README.md)
* [Experts and Institutions](./expinst/README.md)
* [Spatial](./spatial/README.md)
* [Services](./services/README.md)

## References

* [Science on Schema](https://github.com/ESIPFed/science-on-schema.org//)
* [Ocean Best Practices on Schema](https://github.com/adamml/ocean-best-practices-on-schema)
* [PID policy for European Open Science Cloud](https://op.europa.eu/en/publication-detail/-/publication/35c5ca10-1417-11eb-b57e-01aa75ed71a1/language-en)
* [DCAT Schema.org mappings](https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping)
* [DCAT US Data.gov reference](https://resources.data.gov/resources/dcat-us/)
* [FAIR Semantics](https://zenodo.org/record/3707985#.X7Jq2-RKjrV)
  * [RDA group meeting notes](https://docs.google.com/document/d/18CyQ2WsOxG_0zzzteubJyPveZzr8KPH4iuvoKVxRo3o/edit)
  * [RDA Plenary meeting](https://www.rd-alliance.org/moving-toward-fair-semantics-2)
