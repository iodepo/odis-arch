# Notebooks and Products related to the OIH Release Graphs

> NOTE:  This work is all very early access right now.  OIH will be doing this as part of the production indexing.  However, the 
> files here are still very much prototypes at this point.  Feel free to raise issues in this repo about
> the release graph approach if you have feedback. 

## Background

The Ocean InfoHub Project supports a global network of distributed information 
and data resources related to the ocean. The project facilitates discovery and 
interoperability of existing information systems through the lightweight Ocean 
Data and Information System (ODIS) architecture. This enables users from Member
States and other partners to discover and more easily access global oceans information,
data and knowledge products for management and sustainable development. The Project
has had a focus on co-design with three pilot regions in particular: Africa, Latin
America and the Caribbean (LAC), and the Pacific Small Island Developing States 
(PSIDs), to meet their unique user community (thematic and language) requirements.

References: 
* [About Ocean InfoHub](https://oceaninfohub.org/project-overview/) 
* [Home page and search](https://oceaninfohub.org/)

### Ocean InfoHub Introduction Video
[![Ocean InfoHub Intro Video](https://img.youtube.com/vi/KrxeZrPg0u8/0.jpg)](https://www.youtube.com/watch?v=KrxeZrPg0u8)


## Ocean InfoHub Knowledge Graph

The **Ocean InfoHub Knowledge Graph** is a comprehensive, interconnected web of information that encapsulates the vast array of data, knowledge, and resources related to the world's oceans. It is an integral part of the Ocean InfoHub project, which aims to enhance the discovery and interoperability of existing oceanic information systems through the **Ocean Data and Information System (ODIS)** architecture.

This knowledge graph is designed to serve users from Member States and other partners, enabling them to discover and access global oceans information, data, and knowledge products more easily. These resources are crucial for effective management and sustainable development of our oceans. The project has been co-designed with three pilot regions in mind: Africa, Latin America and the Caribbean (LAC), and the Pacific Small Island Developing States (PSIDs), each with their unique user community requirements, including thematic and language needs.

The Ocean InfoHub Knowledge Graph is structured around six key concepts:

- Experts and Institutions
- Documents
- Spatial Maps
- Projects
- Training
- Vessels

Each of these concepts forms a node in the graph, with edges representing the relationships between them. 
This structure allows for a high degree of interconnectivity and cross-referencing, facilitating a 
more holistic understanding of the available information.

The knowledge graph leverages **schema.org** as its vocabulary, a semantic framework used for 
structuring data on the internet. This choice ensures that the data within the graph is organized 
in a standardized, universally understood manner, making it easier for users to navigate and extract 
meaningful insights.

In essence, the Ocean InfoHub Knowledge Graph is a powerful tool that brings together diverse oceanic 
information in a structured, accessible, and user-friendly format, promoting better decision-making 
and sustainable practices for the world's oceans.



## Release Graph

To better support the use by and the engagment with the ODIS community, the OIH graph is assembled into 
publishable components.  Additionally, a set of notebooks to provide guidance on how to interact and use
these components have been developed. 

The resource can be accessed through the links provided below. As the project progresses, 
these resources will be auto-generated, and updated versions of the graph will be periodically released on 
Zenodo, complete with DOI and citation methodologies, ensuring the traceability and credibility of the information.

The preliminary exploratory code, which probes the application of Natural Language Processing (NLP) 
for extracting Geopolitical Entities (GPEs) from these resources, can be located 
in [./dataScience](dataScience/README.md). This signifies the commencement of our journey into exploring potential 
strategies to maximize the utility of the OIH Graph.


## Notebooks

[Release Builder](./sparqlGeoPandas.ipynb) :  Used to gather the various release graphs built by 
Gleaner and Nabu into publishable products.

[Asset Listing ](./assetListing.ipynb) : A simple template that calls out to the current assets 
as a foundation for working with them.  Really just a template notebook for others to start with.

[Extraction: OIH Dashboard](./extraction_OIHDashboard.ipynb) : Example of using DuckDB on the 
release assets to do dashboard or EDA like operations. 

[Extraction WMO](archinterfaces/ODIS-WIS2/extraction_WMO.ipynb) : Some early work building 
assets from the release graph for the World Meteorological Organization. 

[GeoCoverage](graphOps/analytics/ds_geocoverage.ipynb) : Just a simple notebook playing 
with some approaches to using NLP and NER to pull geopolitical names from the description 
text. 

## Assets

You can locate the current assets by utilizing the [assetListing notebook](./assetListing.ipynb). This tool interacts with the anonymous OIH bucket, generating a list of the existing files and offering fundamental methods for file manipulation. 

Additionally, these files can be accessed directly through the anonymous S3 URL:

```
http://ossapi.oceaninfohub.org/public
```

Alternatively, the files can also be accessed via the URLs provided in the subsequent notes.





### OIH Assets

Assets similar to those generated in the [release_builder.ipynb](sparqlGeoPandas.ipynb) are available. These primarily consist of SPARQL queries executed against the provider graph, with the results stored in parquet files.

The [extraction_OIHDashboard.ipynb](extraction_OIHDashboard.ipynb) showcases how DuckDB can be used to query the combined.parquet file. Some users may find the use of SQL beneficial in certain scenarios.

For those interested in utilizing SPARQL, the [release_builder.ipynb](sparqlGeoPandas.ipynb) is a valuable resource. This notebook loads the release graphs into RDFLib and executes SPARQL queries against them, providing a practical demonstration of its operation.

We always appreciate any improvements, issue reports, and pull requests.


> NOTE: Some partners use http://schema.org/ and others use https://schema.org/ as the 
> prefix URI for the schema.org vocabulary.  We will fix this miss alignment in the next
> release but be aware those two URIs are both used in this set of files.  

### Collection files

The _combined.parquet_ file is the union of all the files listed in the _Query result files_ section.
These results are from the following SPARQL query


```sparql
PREFIX schema: <https://schema.org/>
PREFIX schemawrong: <http://schema.org/>


SELECT ?g ?s ?type ?desc ?name ?url ?keywords
WHERE
{
     ?s rdf:type ?type
    FILTER ( ?type IN (schema:ResearchProject, schema:Project, schema:Organization,
    schema:Dataset, schema:CreativeWork, schema:Person, schema:Map, schema:Course,
    schema:CourseInstance, schema:Event, schema:Vehicle,   schemawrong:ResearchProject, schemawrong:Project, schemawrong:Organization,
    schemawrong:Dataset, schemawrong:CreativeWork, schemawrong:Person, schemawrong:Map, schemawrong:Course,
    schemawrong:CourseInstance, schemawrong:Event, schemawrong:Vehicle  ) )
    OPTIONAL {?s schema:description | schemawrong:description  ?desc .}
    OPTIONAL {?s schema:name | schemawrong:name ?name }
    OPTIONAL { ?s schema:url | schemawrong:url ?url .   }
    OPTIONAL {?s schema:keywords | schemawrong:keywords ?keywords}
 }
```

run against each of the RDF files from section _Graphs_.

The _OIHGraph_25032023.parquet_ file, is the 
collection of all the quads from the provider graphs in the _Graphs_ section into one parquet 
file.  This is then stored in parquet.   

> NOTE:  The [KGLab](https://derwen.ai/docs/kgl/) python library and more exactly some of the documentation at [https://derwen.ai/docs/kgl/ex2_0/](https://derwen.ai/docs/kgl/ex2_0/) can be used to load RDF in parquet into python graph workflows.

> Note:  The links to the object in the following README are only HTTP not HTTPS, so your browser may not let you download
these directly due to mixed protocol security issue.  I am working to get these resolved with the
Belgium group hosting the services.   You may need to copy the URLs and download directly fro your terminal.  You can also typically paste them into the browser URL box directly and 
it will work.  It's the mixing of http and https that browser bark at. 

| File Name                  | Notes                                                                                                                | URL |
|:---------------------------|:---------------------------------------------------------------------------------------------------------------------|:--- |
| OIHGraph_25032023.parquet | This file is a collection of the RDF triples from all the providers in one parquet file                              | [OIHGraph_25032023.parquet](http://ossapi.oceaninfohub.org/public/assets/OIHGraph_25032023.parquet) |
| combined.parquet          | This file is a collection of the results from the SPARQL query above from all the providers in into one parquet file | [combined.parquet](http://ossapi.oceaninfohub.org/public/assets/combined.parquet) |

Parquet schema for combined.parquet

```
message combined_scheme {
    optional binary s (STRING)
    optional binary type (STRING)
    optional binary name (STRING)
    optional binary keywords (STRING)
    optional binary url (STRING)
    optional binary desc (STRING)
    optional binary provder (STRING)
    optional int64 __index_level_0__
}
```

Parquet schema for OIHGraph_25032023.parquet

```
message OIHGraph_25032023_scheme {
    optional binary subject (STRING)
    optional binary predicate (STRING)
    optional binary object (STRING)
}
```

### Query result files

These files represent the results of the SPARQL query listed above on the RDF graph of each of the 
providers.  In the following section, links to these RDF files are provided.

| File Name | URL                                                                                                     |
|:--------- |:--------------------------------------------------------------------------------------------------------|
| africaioc.parquet | [africaioc.parquet](http://ossapi.oceaninfohub.org/public/assets/africaioc.parquet)                     |
| cioos.parquet | [cioos.parquet](http://ossapi.oceaninfohub.org/public/assets/cioos.parquet)                             |
| edmerp.parquet | [edmerp.parquet](http://ossapi.oceaninfohub.org/public/assets/edmerp.parquet)                           |
| edmo.parquet | [edmo.parquet](http://ossapi.oceaninfohub.org/public/assets/edmo.parquet)                               |
| emodnet.parquet | [emodnet.parquet](http://ossapi.oceaninfohub.org/public/assets/emodnet.parquet)                         |
| inanodc.parquet | [inanodc.parquet](http://ossapi.oceaninfohub.org/public/assets/inanodc.parquet)                         |
| invemardocuments.parquet | [invemardocuments.parquet](http://ossapi.oceaninfohub.org/public/assets/invemardocuments.parquet)       |
| invemarexperts.parquet | [invemarexperts.parquet](http://ossapi.oceaninfohub.org/public/assets/invemarexperts.parquet)           |
| invemarinstitutions.parquet | [invemarinstitutions.parquet](http://ossapi.oceaninfohub.org/public/assets/invemarinstitutions.parquet) |
| invemartraining.parquet | [invemartraining.parquet](http://ossapi.oceaninfohub.org/public/assets/invemartraining.parquet)         |
| invemarvessels.parquet | [invemarvessels.parquet](http://ossapi.oceaninfohub.org/public/assets/invemarvessels.parquet)           |
| marinetraining.parquet | [marinetraining.parquet](http://ossapi.oceaninfohub.org/public/assets/marinetraining.parquet)           |
| obis.parquet | [obis.parquet](http://ossapi.oceaninfohub.org/public/assets/obis.parquet)                               |
| obps.parquet | [obps.parquet](http://ossapi.oceaninfohub.org/public/assets/obps.parquet)                               |
| oceanexperts.parquet | [oceanexperts.parquet](http://ossapi.oceaninfohub.org/public/assets/oceanexperts.parquet)               |
| pdh.parquet | [pdh.parquet](http://ossapi.oceaninfohub.org/public/assets/pdh.parquet)                                 |
| test_obis.parquet | [test_obis.parquet](http://ossapi.oceaninfohub.org/public/assets/test_obis.parquet)                     |

### Graphs

This section provides an overview of the graphs, in the NQ format, associated with the existing OIH partners.

| File Name | URL                                                                                                                                 |
|:--------- |:------------------------------------------------------------------------------------------------------------------------------------|
| summonedafricaioc_v1_release.nq | [summonedafricaioc_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedafricaioc_v1_release.nq)                     |
| summonedaquadocs_v1_release.nq | [summonedaquadocs_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedaquadocs_v1_release.nq)                       |
| summonedcioos_v1_release.nq | [summonedcioos_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.nq)                             |
| summonededmerp_v1_release.nq | [summonededmerp_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonededmerp_v1_release.nq)                           |
| summonededmo_v1_release.nq | [summonededmo_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonededmo_v1_release.nq)                               |
| summonedemodnet_v1_release.nq | [summonedemodnet_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedemodnet_v1_release.nq)                         |
| summonedinanodc_v1_release.nq | [summonedinanodc_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinanodc_v1_release.nq)                         |
| summonedinvemardocuments_v1_release.nq | [summonedinvemardocuments_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinvemardocuments_v1_release.nq)       |
| summonedinvemarexperts_v1_release.nq | [summonedinvemarexperts_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinvemarexperts_v1_release.nq)           |
| summonedinvemarinstitutions_v1_release.nq | [summonedinvemarinstitutions_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinvemarinstitutions_v1_release.nq) |
| summonedinvemartraining_v1_release.nq | [summonedinvemartraining_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinvemartraining_v1_release.nq)         |
| summonedinvemarvessels_v1_release.nq | [summonedinvemarvessels_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedinvemarvessels_v1_release.nq)           |
| summonedmarinetraining_v1_release.nq | [summonedmarinetraining_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedmarinetraining_v1_release.nq)           |
| summonedobis_v1_release.nq | [summonedobis_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedobis_v1_release.nq)                               |
| summonedobps_v1_release.nq | [summonedobps_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedobps_v1_release.nq)                               |
| summonedoceanexperts_v1_release.nq | [summonedoceanexperts_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedoceanexperts_v1_release.nq)               |
| summonedpdh_v1_release.nq | [summonedpdh_v1_release.nq](http://ossapi.oceaninfohub.org/public/graphs/summonedpdh_v1_release.nq)                                 |


