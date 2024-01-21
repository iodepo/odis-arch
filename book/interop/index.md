# System to System Interop

This document outlines the technical aspects of the evolving interaction between the Ocean Data Ingestion System (ODIS) / Ocean  InfoHub
(OIH) platform and the World Meteorological Organization (WMO) Weather Information System Version 2 (WIS2). 

_Key Points:_

ODIS/OIH and WIS2 are collaborating to establish a robust mechanism for data exchange.
This document focuses on the ongoing development of their interoperability.
Specific details regarding data models, communication protocols, and integration points will be elaborated upon.

_Current Interaction Elements:_

Data Scope: The exchange primarily involves oceanographic and meteorological data relevant to both OIH and WIS2 functionalities.

Technical Framework: The integration leverages modern data sharing principles, incorporating standardized protocols and interoperable formats.

Communication Mechanism: The specific communication channels and message types employed for data transfer will be discussed, including any
underlying infrastructure components.

_Future Considerations:_

Scalability and Performance: Optimizing data exchange for efficiency and reliability with high data volumes is crucial.

Security and Confidentiality: Ensuring data integrity and access control within established security protocols is paramount.

Sustainability and Maintenance: Building a long-term sustainable integration model with clear ownership and maintenance responsibilities is crucial.

Overall, this document aims to provide a technical roadmap for the OIH-WIS2 integration, focusing on the current interaction elements and
outlining future considerations for a robust and sustainable data exchange framework.



![overview](./images/wmowis2.svg)

## Diagram Overview

This diagram visually guides you through the activity's progression, with each element positioned from left to right in chronological order.
The stages are detailed below.

_Inputs_

ODIScat represents the source for the settings and values for the providers.  The OIH approach is based on web architecture and so these values include 
standards based representations of the sitemap.xml and robots.txt that are used to discover and resolve the expressed resources for a provider.

The representation of these resources includes a JSON-LD representation typically embedded in the resource HTML page or provided as a distinct document
via content negotiation.  

Standards or approaches used:
* https://www.rfc-editor.org/rfc/rfc9309
* https://www.sitemaps.org/protocol.html
* https://www.w3.org/TR/json-ld/
* https://schema.org/
* https://www.ogc.org/standard/geosparql/
* https://github.com/ESIPFed/science-on-schema.org

_Gleaner (harvesting)_

Gleaner is the name of the software package used by OIH to do the indexing of the resources described and encoded by the previous section.  
However, this package simply uses web architecture approaches, mostly http/https to access the resources.  There are 
several [alternatives](https://book.oceaninfohub.org/indexing/alternatives.html) that groups could use to address this stage.

Standards or approaches used:
* https://www.w3.org/TR/dwbp/


_ODIS Object Store_

One action of Gleaner in the harvesting stage is to store the resources found in an S3 object store.  Any S3 object store could be 
used, so services like AWS S3, Google Cloud, Azure or others could be used.  OIH uses the open source Minio S3 object to address
this.  

The JSON-LD files accessed are stored along with a single n-quads representation of all the JSON-LD data graphs on a per-provider 
basis.  So, a provider exposing 1000 JSON-LD objects will result in those 1000 JSON-LD documents staged in the object store, along 
with a single n-quads file with all the triples from those 1000 files. 


Standards or approaches used:
* https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html (not a standard, a convention)
* https://www.w3.org/RDF/

_MDP Generator & SPARQL_

This software package leverages the above collected objects in combination with the developed SPARQL 
to generate a set of query response files described in the following section.  The primary reason 
for this step is to conduct and store the results for the queries in a format that is more performant.

Using a triplestore to conduct the SPARQL queries in real time involved setting up and maintaining a service
at such a scale and capacity that did not provide sufficient value for the investment.  


Standards or approaches used:
* https://www.w3.org/TR/sparql11-query/

_ODIS Products_ 

The results of the above queries are store in two formats.  One is CSV, for ease of use 
by a broader community.  Additionally,  a version of the query results is also 
stored in parquet.  This is a modern cloud native column based storage format
that allows for fast network based interaction over the network.  OIH leverages parquet
combined with DuckDB to leverage SQL based OLAP based interactions with the results files. 


Standards or approaches used:
* https://www.ietf.org/rfc/rfc4180.txt
* https://github.com/apache/parquet-format


_mdp2wis2_

This software package does a simple ETL of the master data products generated in the 
above process into GeoJSON that addresses the profile needed by WMO-WIS2.  These resources
will again be stored in the OIH object store leveraging the S3 API and made available 
to all users.  The resources will be made discoverable via the OGC API crawl-able catalog.  

Standards or approaches used:
* [OGC API (crawlable catalog)](https://docs.ogc.org/DRAFTS/20-004.html#clause-crawlable-catalog)
* [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946)

## Conclusion

This document delves into the technical details of how a standardized, resource-oriented architecture enables data exchange between
the Ocean InfoHub (OIH) and the World Meteorological Organization's Weather Information System Version 2 (WIS2). 

Key Focus:

    Leveraging a resource-oriented architecture for efficient and standardized data access between OIH and WIS2.
    Guiding WIS2's resource exposure based on best practices for data on the web to facilitate indexing by the OIH Knowledge Graph.

Current Approach:

    The OIH approach is based in standards and open formats.  Data resources are exposed following principles like Resource Description Framework (RDF) 
    and Linked Data, enabling machine-readable descriptions and discoverability by the OIH Knowledge Graph.

Benefits:

    Interoperability: Standardized APIs ensure platform-agnostic data exchange, fostering wider usability and integration with other systems.
    Discovery and Accessibility: Resource-oriented design simplifies data discovery for OIH, facilitating efficient indexing and querying of the objects and data graphs.
    Maintainability and Scalability: Following established web technology best practices promotes a well-defined and extensible architecture for data exchange.

Future considerations:

    Harmonization of Data Models: Aligning data models between OIH and WIS2 can further streamline integration and reduce transformation overhead.
    Performance Optimization: Optimizing resource representations and API responses can improve data acquisition efficiency for large datasets.

Overall, this document highlights the advantages of employing structured data and a resource-oriented architecture for OIH-WIS2 data exchange. 


