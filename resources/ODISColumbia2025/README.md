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
This section explores the fundamental principles guiding the creation and publication of structured metadata, aligning with the vision of a standardized and interoperable web. We emphasize **standards-based, low-friction methods**, as exemplified by the ODIS Quickstart documentation and informed by core web standards. ODIS provides a real-world example of implementing **schema.org** in a distributed environment.

We will examine:
- Core philosophies of open web standards
- Low-friction implementation methods for interoperable web data

These principles enable data that is **findable, accessible, interoperable, and reusable**, fostering a connected, data-driven web. Low-friction methods lower the barrier to entry for publishing structured data, encouraging broader adoption.

### Resources
- [ODIS Book](https://book.odis.org/index.html) - Comprehensive overview
- [ODIS Quickstart](https://book.odis.org/gettingStarted.html) - Practical guide to implementing these principles
- [W3C Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) - Foundational reference for high-quality structured data

**Functional Goal**: Describe the fundamental principles and practical methods for publishing standards-based structured metadata on the web, focusing on JSON-LD and schema.org.

---

## Introduction to Foundational Architecture with JSON-LD
In an interconnected world, **machine-readable data** is key to seamless information exchange and intelligent applications. **JSON-LD** provides a lightweight, flexible way to represent linked data on the web, a cornerstone of the Semantic Web. It enables data to be understood by both humans and machines, improving interoperability and supporting data-driven applications.

This section introduces:
- Fundamental concepts of JSON-LD
- How it creates a data graph for linked data
- Context, keywords, compacted/expanded views, RDF conversion, and framing

### Resources
- [ESIP Tutorials](https://github.com/ESIPFed/science-on-schema.org/tree/main/tutorials/esip-summer-mtg-2022)
- [JSON Crack](https://jsoncrack.com)
- [JSON-LD Playground](https://json-ld.org/playground/)
- [JSON-LD Official Site](https://json-ld.org/)
- [W3C Talk on JSON-LD](https://www.w3.org/Talks/2021/09-20-ddi-cdi/?full#1)


---

## Authoring Process for Data Graphs and Sitemaps
This section guides you through making your website’s data understandable to search engines and applications using **JSON-LD**. We’ll cover:
1. Describing data with JSON-LD (like labeling information)
2. Validating your work for accuracy
3. Creating a sitemap for search engines to index your content

**Example**: For a website about books, use JSON-LD to specify titles, authors, and descriptions for search engines.

Learn to create, validate, and publish structured data, including sitemaps. More details are in the ODIS Book.

### Resources
- [Rustpad](https://rustpad.io/#vertPY)
- [Schema Validator](https://validator.schema.org/) 
- [SHACL](https://github.com/RDFLib/pySHACL)
- [Sitemaps.org](https://sitemaps.org/)
- [ODIS Publishing](https://book.odis.org/publishing/publishing.html)
- [ODIS Graph Publishing](https://book.odis.org/indexing/graphpub.html)

---

## Identifiers and Graph IDs
This section examines the critical role of **Persistent Identifiers (PIDs)** in enhancing reliability and discoverability of structured data. PIDs ensure enduring accessibility and unambiguous identification, mitigating link rot and maintaining data integrity.

We’ll cover:
- Types of PIDs (e.g., ORCID for researchers, DOI for documents, ROR for organizations)
- Integration with JSON-LD for interconnected data graphs
- Enhancing data provenance and semantic interoperability

**Functional Goal**: Explore common PIDs and their importance (leverage NIH graphs/images).

### Resources
- [ODIS Variables](https://book.odis.org/thematics/variables/index.html)
- [ODIS Identifiers](https://book.odis.org/thematics/identifier/id.html)
- [RDA PID Strategies](https://www.rd-alliance.org/wp-content/uploads/2023/06/AUSTRALIA20Case20Study20-20National20PID20Strategies.pdf)
- [ARDC PID Guide](https://ardc.edu.au/resource/using-orcid-and-persistent-identifiers-to-connect-link-cite-and-credit-research/)

---

## Deployment Strategies
This section explores strategies for deploying **JSON-LD structured data** in various web architectures, enabling seamless integration with existing systems. We’ll examine:
- Embedding JSON-LD in HTML pages
- Delivering via API endpoints
- Dynamic creation by data services (e.g., ERDDAP, CKAN, pygeoapi)

Choosing a strategy depends on data volume, update frequency, and audience. Static deployment suits stable datasets; APIs suit dynamic data.

**Functional Goal**: Describe deployment strategies for JSON-LD in web architectures and data services, demonstrating tool integration.

### Resources
- Tools document (TBD)
- GitHub + sitemap

---

## Indexing and User Interfaces
This section demonstrates how to index and query **JSON-LD data** for enhanced discoverability and interoperability. Indexing makes data searchable; querying enables complex analysis. Tools like **Gleaner** harvest/index data, while **SPARQL** retrieves specific info.

We’ll show:
- Indexing/querying JSON-LD from this session
- Example UIs for presenting data clearly

### Resources
- Gleaner (bash/python examples)
- [Gleaner Archetype](https://github.com/gleanerio/archetype)
- Qlever indexing/query process
- UI examples

---

## Value Proposition
**Schema.org** standardizes structured data on the web, improving discoverability, interoperability, and machine understanding. Benefits include:
- Richer search results and visibility for search engines
- Better SEO and UX for website owners
- More relevant results for users
- Support for FAIR data principles

This section shows how to leverage schema.org and JSON-LD for effective web content.

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

## Why this way (Architecture Focus)?
- **Low friction**
- **Standards-based** (consumed by many clients)
- **AI-ready** (e.g., Croissant, CDIF, ODIS, Google Dataset)
