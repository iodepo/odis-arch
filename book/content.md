# Structured Data on the Web

## About

Structured data on the web is a way to provide semantics and linked data in an
approachable manner.  This approach expresses concepts in JSON-LD which is a
JavaScript notation popular among developers which easily expresses  concepts
(terms) and links to related resources (things).   This structured data on the
web approach has been popularized by the large commercial search providers like
Google, Bing, Yandex and others via schema.org  As described at schema.org:
"Schema.org is a collaborative, community activity with a mission to create,
maintain, and promote schemas for structured data on the Internet, on web pages,
in email messages, and beyond."

The popularity of leveraging the schema.org approach in the earth sciences can
be attributed to both this ease of developer adoption and also to its
foundational use of web architecture. A web architecture foundation aids
adoption by the operations side as well as the developer side.  It also takes
advantage of the scale and resilience of the web.  

The broad nature of schema.org even scopes to the concepts of Datasets.  It is
the existence of schema.org/Dataset that was a focus of several EarthCube
projects (Project 418, Project 419 and the Resource Registry) from which spun up
the ESIP Science on Schema work.  

Additionally, Google leveraged schema.org/Dataset to develop and populate the
Google Data Set Search and provides guidance to developers to facilitate this.  


## Web architecture approach

OIH is focused on leveraging the web architecture as the foundation for this
approach.  There are several key reasons for this vs approaches like OAI-PMH or
others.

A key point is that in the processes of establishing a web presence, a standard
step for groups, they have already begun to build the infrastructure needed for
structured data on the web.  Setting up special servers or establishing and
maintaining special APIs to support harvesting is not required.  

Also, a large collection of tooling already exists around JSON that is directly
usable in JSON-LD.  That scale extends to the use of schema.org patterns which
have become common in the commercial web.  Allowing us to bring those same
patterns and the tooling to the science community.

Additionally, this approach keeps the metadata and its representation a product
of the data providers.  The actor in the life cycle most aware of needed edits,
new records or other events.  That same record then serves multiple consumers
able to generate various value add products.  This benefits the provider by
facilitating multiple and varied discovery vectors for their holdings.  

Another key factor is the web native and semantic nature of this representation
of metadata.  Traditional metadata, such as ISO, by itself does not express a
web referenceable instance of concepts.  In doing this, structured data on the
web allow connections to be made and discovered by people and machines across
many holdings.  This aids in both serendipitous discovery and can also be
leveraged to aid discovery via semantic relations.

## Terminology

A CSV file is a text file containing spreadsheet information following a data
model that is encoded using a convention of rows and commas defining columns.  

A JSON-LD fle is a text file containing graph information following the RDF data
model that is encoded using a convention based on JSON syntax.

JSON-LD is a way to serialize RDF that uses JSON notation.  It is really no
different then than RDF-XML, turtle, n-triples, etc.  There are several ways to
represent the RDF data model in text files (and some emerging binary ones like
CBOR and parquet patterns).

Schema.org is a vocabulary for describing things similar to DCAT, FOAF, Dublin
Core.  It does this by using RDF as the underlying data model to represent this
"ontology".

The confusion comes from the collision of outcomes.  JSON-LD came about, partly,
to allow the use of the RDF data model by a broader audience.  This is done by
leveraging a more popular notation for the data model, JSON, in the form of
JSON-LD.  Schema.org also wanted to advance the use of structured [meta]data by
making it easier to use and connecting structured data to web pages.  At the
start, there were three approaches; RDFa, microformats and JSON-LD, to putting
schema.org in web pages.  However, the JSON-LD approach to incorporating this
structured data has grown in popularity far beyond the others. As the popularity
of both JSON-LD and schema.org grew,  they often got conflated with each other.

The term  "structured data on the web" is perhaps a more neutral way to discuss
the use of vocabularies encoding in JSON-LD used in web pages.  However,  the
phrase "schema.org" is starting to become the term for "structured data on the
web using JSON-LD as a serialization".    Even in cases where you combine other
vocabularies such as DCAT with JSON-LD with no schema.org involved, it seems the
way to convey this is to say: "We will use the schema.org 'pattern' with DCAT".

It is arguably not the best or most accurate communications strategy.  It can
 conflate data models, serialization and vocabularies.  However, it is concise
 and ubiquitous and not likely to change.

## Intellectual Merit

OIH leverages structured data on the web patterns in the form of 
Schema.org and JSON-LD encoding.  This means that much of what is done
to address OIH implementation by providers also is available both to existing
commercial indexing approaches as well as emerging community practices  

Additionally, both the publishing and indexing approaches are based
on several web architecture patterns.  Meaning that existing organization skills
are leveraged and staff experience is enhanced.   This helps to address both 
the sustainability of the OIH connection and the efficiency of 
organizational operation.   

## Broader Impacts

By leveraging existing technology and approaches a larger community is enabled
to engage and make more samples discoverable and usable.

The nature of structured data on the web also provides the ability to apply
semantic context to samples.  This means richer discovery and information about
samples, the past uses and potential future uses is more readily available.

Simplified architecture also means easier development of tools and interfaces to
present the data.  Allowing the presentation of samples and their information in
a manner aligned with a given community's needs.    A simplified architecture
aids sustainability from both a technical and financial perspective.  


