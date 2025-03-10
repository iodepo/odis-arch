# Columbia Meeting Outline
**March 11th, 2025 (Tuesday: 90-minute session)**

This 90-minute workshop at the Columbia Meeting will provide a practical overview of the Ocean Data and Information System (ODIS) and its implementation using JSON-LD, focusing on enabling data discoverability and interoperability. We will begin by outlining the core principles of ODIS, emphasizing standards-based, low-friction methods, and then delve into the foundational architecture of JSON-LD for creating machine-readable linked data. 

Participants will learn the authoring process for data graphs and sitemaps, explore the importance of persistent identifiers (PIDs), and discover various deployment strategies for publishing JSON-LD data on the web. We will also demonstrate indexing and querying techniques using tools like Gleaner and SPARQL, and showcase simple user interfaces. Finally, we will highlight the value proposition of using JSON-LD for improved data discoverability and machine understanding, concluding with a question and answer session.

## Ocean Data and Information System (ODIS) WS

### Agenda
| Section                              | Time | Comments                                                                                     |
|--------------------------------------|------|---------------------------------------------------------------------------------------------|
| Principles and overview of the approach | 5    | Outlines core philosophies and provides an overview emphasizing standards-based, low-friction methods as presented in the ODIS Quickstart documentation |
| Introduction to foundational architecture with JSON-LD | 10   | Explains the underlying structure and machine-readable capabilities of JSON-LD for creating linked data |
| Authoring process for data graphs and sitemaps | 20   | Guides learners through practical steps of creating JSON-LD markup, validating it, and generating sitemaps for web publishing |
| Identifiers and graph IDs            | 10   | Focuses on the importance of persistent identifiers (PIDs) and their role                  |
| Deployment strategies                | 20   | Covers how to publish JSON-LD data on the web, including GitHub page deployment and tools supporting JSON-LD integration |
| Indexing and User interfaces         | 10   | Demonstrates indexing JSON-LD data for search/retrieval using tools like Gleaner and SPARQL, and showcases simple UIs |
| Value Proposition                    | 5    | Highlights benefits of using JSON-LD for improving data discoverability, interoperability, and machine understanding |
| Questions                            | 10   |                                                                                             |

**Total Section Length: 90 minutes**

---

## Principles and Overview of the Approach
This section explores the fundamental principles that guide the creation and publication of structured metadata, aligning with the broader vision of a standardized and interoperable web. We will emphasize standards-based, low-friction methods, as exemplified by the ODIS Quickstart documentation, and informed by core web standards. ODIS provides a real world example of how to implement schema.org in a distributed environment. We will examine the core philosophies of using open web standards, and the low friction methods of implementation, that are used to create interoperable web data. These principles facilitate the creation of data that is easily discoverable, accessible, interoperable, and reusable, fostering a more connected and data-driven web. By adopting low-friction methods, we can lower the barrier to entry for publishing structured data, encouraging wider adoption and contribution. 

The ODIS Quickstart (https://book.odis.org/gettingStarted.html) provides a practical guide to implementing these principles, while the ODIS Book (https://book.odis.org/index.html) offers a more comprehensive overview. The W3C's Data on the Web Best Practices (https://www.w3.org/TR/dwbp/) serve as a foundational reference for creating high-quality structured data.

Functional Goal: Describe the fundamental principles and practical methods for publishing standards-based structured metadata on the web, with a focus on JSON-LD and schema.org.

These principles enable data that is **findable, accessible, interoperable, and reusable**, fostering a connected, data-driven web. Low-friction methods lower the barrier to entry for publishing structured data, encouraging broader adoption.

### Resources
- [ODIS Book](https://book.odis.org/index.html) - Comprehensive overview
- [ODIS Quickstart](https://book.odis.org/gettingStarted.html) - Practical guide to implementing these principles
- [W3C Data on the Web Best Practices—](https://www.w3.org/TR/dwbp/)Foundational reference for high-quality structured data

**Functional Goal**: Describe the fundamental principles and practical methods for publishing standards-based structured metadata on the web, focusing on JSON-LD and schema.org.

---

## Introduction to Foundational Architecture with JSON-LD

In today's interconnected world, making data machine-readable is crucial for enabling seamless information exchange and building intelligent applications. JSON-LD plays a pivotal role in achieving this, by providing a lightweight and flexible way to represent linked data on the web. JSON-LD is a key technology that enables the creation of linked data, a cornerstone of the Semantic Web. It allows us to represent data in a way that can be easily understood and processed by both humans and machines, improving data interoperability and enabling data-driven applications.

This section will introduce the fundamental concepts of JSON-LD, demonstrating how it creates a data graph that can be used to create linked data. We will cover the context, key words, compacted and expanded views, and conversion to RDF. We will also show how framing can be used to shape the data.

### Resources
* [JSON-LD Playground](https://json-ld.org/playground/)
* [JSON-LD Official Site](https://json-ld.org/)
* https://www.w3.org/Talks/2021/09-20-ddi-cdi/?full#1
* [ESIP Tutorials](https://github.com/ESIPFed/science-on-schema.org/tree/main/tutorials/esip-summer-mtg-2022)


---

## Authoring Process for Data Graphs and Sitemaps

This section will show you how to  make your website's data more understandable to search engines and other applications, by guiding you through the process of creating structured data using JSON-LD. First, we'll show you how to describe your data in a way that search engines can understand. Think of it as adding labels to your information. Then, we'll show you how to check your work, to make sure everything is correct. Finally, we'll create a map of your website and data, so search engines can easily find and index your content. For example, if you have a website with information about datasets, you can use JSON-LD to tell search engines the title, author, and description of each dataset.

Learn how to create structured data using JSON-LD, check it for accuracy, and help search engines find your website and data. We will also discuss how to publish your data, including creating sitemaps of your website and data for search engines. The ODIS Book has more information about this process.




### Resources
- [Rustpad](https://rustpad.io/#vertPY)
- [Schema Validator](https://validator.schema.org/) 
- [SHACL](https://github.com/RDFLib/pySHACL)
- [Sitemaps.org](https://sitemaps.org/)
- [ODIS Publishing](https://book.odis.org/publishing/publishing.html)
- [ODIS Graph Publishing](https://book.odis.org/indexing/graphpub.html)

---

## Identifiers and Graph IDs

This section examines the critical role of Persistent Identifiers (PIDs) in strengthening the reliability and discoverability of structured data. It elucidates the necessity of PIDs in establishing robust and interconnected information networks on the web, and their synergistic relationship with schema.org and JSON-LD.

PIDs function as immutable digital identifiers, ensuring enduring accessibility and unambiguous identification of entities, even in the event of changes to associated URLs or metadata. In the context of structured data, PIDs mitigate the risk of link rot and maintain data integrity.


We’ll cover:
- Types of PIDs (e.g., OceanExpert IDs or ORCIDs for researchers, DOI for documents, ROR for organizations)
- Integration with JSON-LD for interconnected data graphs
- Enhancing data provenance and semantic interoperability

The integration of PIDs within structured data contributes to the establishment of a trustworthy and verifiable web of data. By providing stable references, PIDs enhance data discoverability and facilitate the identification of related information. The documentation will present examples of PID implementation within JSON-LD, and provide guidance on the selection of appropriate PID types for diverse data entities


**Functional Goal**: Explore common PIDs and their importance.

### Resources
- [ODIS Variables](https://book.odis.org/thematics/variables/index.html)
- [ODIS Identifiers](https://book.odis.org/thematics/identifier/id.html)
- [RDA PID Strategies](https://www.rd-alliance.org/wp-content/uploads/2023/06/AUSTRALIA20Case20Study20-20National20PID20Strategies.pdf)
- [ARDC PID Guide](https://ardc.edu.au/resource/using-orcid-and-persistent-identifiers-to-connect-link-cite-and-credit-research/)

---

## Deployment Strategies

This section explores diverse strategies for deploying JSON-LD structured data within various web architecture paradigms, enabling seamless integration with existing systems and workflows. We will examine strategies for deploying JSON-LD within both traditional web architectures, and within data service architectures. We will show how JSON-LD can be embedded into HTML pages, delivered via API endpoints, and created dynamically by data services. Data services like ERDDAP, CKAN and pygeoapi are increasingly capable of automatically generating and exposing JSON-LD metadata, facilitating data discovery and interoperability. We will examine how tools like ERDDAP and pygeoapi are able to create JSON-LD dynamically, and show how web frameworks can be used to embed JSON-LD into web pages.

Choosing the appropriate deployment strategy depends on factors such as data volume, update frequency, and target audience. Static website deployment is ideal for stable datasets, while API endpoints are suitable for dynamic data that requires real-time access. Data services that expose JSON-LD make it easy for other systems to consume the data.

Functional Goal: Describe various deployment strategies for JSON-LD structured data in web architectures and data services, and demonstrate how to leverage tools for seamless integration


### Resources
- [Tools and Software reference](./docs/section5/software.md)
- GitHub + sitemap

---

## Indexing and User Interfaces

Building upon the core value of schema.org and structured data—enhanced discoverability and interoperability—this section demonstrates how to effectively index and query JSON-LD data to unlock its full potential. Indexing makes structured data searchable, enabling efficient retrieval of relevant information, while querying allows for complex data exploration and analysis. Tools like Gleaner are used to harvest and index JSON-LD data, creating searchable repositories, and SPARQL, a powerful query language, allows users to retrieve specific information.

The ability to query and access structured data through user interfaces empowers researchers, data analysts, and other users to extract valuable insights, enabling the creation of user-friendly applications. We will demonstrate the process of indexing and querying JSON-LD documents, including those created during this authoring session, and introduce query approaches for the graph. Example user interfaces will highlight how to present this data in an easy-to-understand format, showcasing how these techniques enable efficient data retrieval and exploration for diverse applications.


---

## Value Proposition

Schema.org is a collaborative effort to create and maintain a standardized vocabulary for structured data on the web. By implementing schema.org, website owners can provide search engines and other applications with a clearer understanding of their content, leading to improved discoverability, interoperability, and machine understanding.

For search engines, this translates to richer search results, increased visibility, and more relevant traffic. For website owners, it means improved SEO and enhanced user experience. Users benefit from more informative and relevant search results. Furthermore, the use of schema.org promotes FAIR data principles, making web data more findable, accessible, interoperable, and reusable.

This section will demonstrate how to leverage schema.org and structured data, particularly through JSON-LD, to improve the effectiveness of web content and enable better data exchange. We will provide practical examples and guidance on implementing schema.org to achieve these goals.


### Resources
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [OIH Search](https://oceaninfohub.org/)
- [Schema.org](https://schema.org)
- [ML Commons](https://mlcommons.org/working-groups/data/croissant/)
- [Go FAIR](https://www.go-fair.org/)
- [CODATA CDIF](https://cdif.codata.org/)



---

## By Skill Complexity
| Learning Goal                                      | Learning Outcome                                                                                   |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Knowledge (Remembering)**                        | Become familiar with schema.org and Dataset concepts; identify vocabulary, context, properties     |
| **Comprehension (Understanding)**                  | Understand benefits/use cases of schema.org for datasets; explain value for indexing/discovery    |
| **Application**                                    | Apply schema.org markup to datasets; generate, validate, and embed it into web pages              |
| **Analysis**                                       | Analyze schema.org Dataset profiles (e.g., ESIP, CDIF); compare properties and use cases          |
| **Synthesis (Creating)**                           | Create comprehensive schema.org descriptions for complex datasets with spatial/temporal scoping   |
| **Evaluation**                                     | Evaluate quality/impact of schema.org descriptions; compare with ISO 115, OAI-PMH                |

---
