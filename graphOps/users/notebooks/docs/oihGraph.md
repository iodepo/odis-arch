## Introduction

Ocean InfoHub has developed a collection of guidance and procedures for the development of a Knowledge Graph based on the contributions of the ODIS partners. The **Ocean InfoHub Knowledge Graph** is a comprehensive, interconnected web of information that encapsulates the vast array of data, knowledge, and resources related to the world's oceans. It is an integral part of the Ocean InfoHub project, which aims to enhance the discovery and interoperability of existing oceanic information systems through the **Ocean Data and Information System (ODIS)** architecture.

This knowledge graph is designed to serve users from Member States and other partners, enabling them to discover and access global oceans information, data, and knowledge products more easily. These resources are crucial for effective management and sustainable development of our oceans. The project has been co-designed with three pilot regions in mind: Africa, Latin America and the Caribbean (LAC), and the Pacific Small Island Developing States (PSIDs), each with their unique user community requirements, including thematic and language needs.

The Ocean InfoHub Knowledge Graph is structured around six key concepts:

- Experts and Institutions
- Documents
- Spatial Maps
- Projects
- Training
- Vessels

Each of these concepts describes a type in the graph, with edges representing the relationships between instances of these types. This structure allows for a high degree of interconnectivity and cross-referencing, facilitating a more holistic understanding of the available information.

The knowledge graph leverages **schema.org** as its vocabulary, a semantic framework used for structuring data on the internet. This choice ensures that the data within the graph is organized in a standardized, universally understood manner, making it easier for users to navigate and extract meaningful insights.

In essence, the Ocean InfoHub Knowledge Graph is a powerful tool that brings together diverse oceanic information in a structured, accessible, and user-friendly format, promoting better decision-making and sustainable practices for the world's oceans.

## Release Graph

To better support the use by and the engagement with the ODIS community, the OIH graph is assembled into publishable components. Additionally, a set of notebooks to provide guidance on how to interact and use these components have been developed.

The resource can be accessed through the links provided below. As the project progresses, these resources will be auto-generated, and updated versions of the graph will be periodically released on Zenodo, complete with DOI and citation methodologies, ensuring the traceability and credibility of the information.

The preliminary exploratory code, which probes the application of Natural Language Processing (NLP) for extracting Geopolitical Entities (GPEs) from these resources, can be located in [./dataScience](https://github.com/iodepo/odis-arch/blob/master/graphOps/releaseGraphs/dataScience/README.md "Ctrl+Click to open URL"). This signifies the commencement of our journey into exploring potential strategies to maximize the utility of the OIH Graph.

THOUGHT: talk about this procedure as a FAIR Implementation Network and use the components of that to define the components to detail.

### Guidance

In this section discuss the elements of the book at book.oceaninfohub.org

* Treat metadata as a first class citizen

### Architecture

- Data on the Web best practices
- FAIR
- Web architecture
- Validation

### Implementation

This section is really just to focus on the actual implementation that OIH used to implement
the preceding architecture.

Here talk about and show the use of Gleaner, Dagster, Docker and the configuration files.

Talk also about the GitHub actions and PySHACL

### OIH Graph: The role

The OIH Graph as Master Data Repository. The term, Master Data Repository (MDR), is often used when referring to a centralized repository that stores high-quality, standardized, and consistent master data, such as customer data, product data, or employee data.  In case of OIH Graph this is the authored metadata describing the resources and their connections.

From this MDR we have developed queries that can process the data into products for various functions and groups.  

One such product is for the OIH Solr text index that is used to power the OIH Search UI.  Solr is used since it provides millisecond text searches across the graph literal values.  Text literal searches is a key user method for searching for resources.  Once a set of resources is found, the graph can then be used to provide more detailed connections.

Additional functions and queries are also be used to extract data for the World Meterological Organization (WMO).  However, WMO uses MQTT, so that would mean we need to express our graph to that representation.  

The graph has also been evaluated for its potential to connect resources both in and outside the graph.  An experiment was done to leverage Machine Learning techniques to connect OIH Graph resources with UN Sustainable Development Goals (SDGs).  This approach is detailed in the attachment (attach Tom's document here somehow).


