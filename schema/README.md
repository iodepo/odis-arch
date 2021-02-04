# README

## About

Documentation on implementing schema.org for the Ocean Info Hub (OIH) to facility the indexing and discovery 
of resources.  The approach leverages schema.org as a base.  Schema.org or is a community effort and widely
implemented by commercial search services.  The approach is based on web standards and best practices and 
facilities development of community index services.  


## Publishing and Indexing Notes

The stages of the data flow include the authoring, publishing and harvesting or indexing of the published resources. The following sections break these out and provide guidance.

* [Authoring](./docs/authoring.md): Guidance on the creation of the JSON-LD data graphs.  Links to documentation
  and tools to validate.
* [Publishing](./docs/publishing.md):  The data graphs need to be associated with web resources and exposed
  via sitemaps and robots.txt.
* [Indexing](./docs/indexers.md): How to building indexes from information published following structured data on the web practices.  The approaches used by OIH can be leveraged both by commercial indexing services as well as community managed resources.
* [Background](./docs/background.md) information on the OIH architecture and some previous work.  This document will likely be incorporated into the above three documents and removed.

## Thematic Areas

Thematic areas represent a set of initial profiles to be defined by the OIH community.  
These profiles will provide a set of minimal elements an author should include as well as more detailed elements they can offer.

1. [Experts and Institutions](./thematics/expinst/README.md)
2. [Documents](./thematics/docs/README.md)
3. [Projects](./thematics/projects/README.md)
4. [Training](./thematics/training/README.md)
5. [Vessels](./thematics/vessels/README.md)
6. [Spatial](./thematics/spatial/README.md)
7. [Services](./thematics/services/README.md)

## Resources

* [References](./docs/references.md)
* [Registries](./docs/registries.md)
* [Controlled Vocabularies](./docs/vocabularies.md)
