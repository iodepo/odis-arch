# Getting started with ODIS

## Hello world

This page describes - at a high level - how a digital system with access to the Web can link itself into the ODIS Federation.

Any system providing data (in a broad sense, including documents, software code, etc) and/or services that are relevant to ocean science, management, policy, commerce, or other ocean-relevant activities is welcome to connect to ODIS. A light curation of ODIS nodes is performed by IODE's team, and the entire Federation self-regulates, voicing concern if they believe nodes.


## Registering your organisation

Organisations which contribute to the ODIS Federation need an unambiguous identity on the web. This is not (necessarily) the same as your organisation's website: A web identifier is focused on machine-readable metadata and will not change (even if your organisation changes its name). It's important that this digital identity is sanctioned by your organisation's leadership and administration, such that it is an official identifier and kept up to date (like an ORCID for your organisation).

### OceanExpert 

We recommend that your organisation creates and maintains an OceanExpert ID. OceanExpert (OE) is maintained by the IODE and is deeply integrated into ocean data flows. For example, OE is - itself - an ODIS node, thus any data you add there will automatically be shared through the ODIS Federation.

Creating an entry is a matter of a few minutes, and requires no technical skill beyond using a web browser. However, it is key that your organisation is aware of the OE entry and approves its creation. Additionally, an individual should be nominated to maintain the entry. 


## Registering your (meta)data node(s)

Now that your organisation has an identifier on the web, you can register the data systems you wish to connect as ODIS nodes. The ODIS Catalogue of Sources (ODISCat) is the system we use to register, describe, and interlink data sources that feed into ODIS.

Note: One organisation can operate many such nodes (e.g. for different types of data, services, etc). 

To register a source, simply go to the ODISCat website [TODO: Add link], log in with your OE credentials, and create an entry. This should take around 10 minutes.

ODISCat has a dedicated field to let the ODIS Federation know where your metadata is. Leave that blank for now: we'll come back to this after we prepare content to share via ODIS.


## Preparing content 

All ODIS nodes share metadata about their holdings (datasets, documents, organisational information, etc) and services (APIs, portals) by exposing structured metadata catalogues over the web. 

The first step towards joining ODIS is to export metadata about your digital holdings as JSON-LD files, using schema.org Types and properties. Guidelines on how to shape these files is available here [TODO:Add links], and we provide a library of examples [TODO:Add link] and templates in this book to help nodes shape their submissions. Note, however, that any valid schema.org Type can be used to share metadata through the Federation. 

Note: To create and test an initial link to ODIS, you don't need to create metadata for all your holdings - a ssmall test set will do.

Additional semantics (i.e. beyond what schema.org can offer) can be embedded into these files using schema.org's additionalProperty, DefinedTerm, or similar property. More information on how to nest additonal semantics is availabler here: [TODO: Add links] 

You can store these files anywhere on the web (under your control), as long as they are accessible using standard web protocols. Many ODIS partners that have landing pages for their data sets or other digital assets choose to embed the JSON-LD inside HTML webpages [TODO:Add link to example]. 

### Reusing patterns

ODIS Partners have co-developed a library of JSON-LD/schema.org patterns (i.e. extended examples of how to format JSON-LD files using schema.org Types and properties) to help each other share content in a normative way. In general, these patterns give more complete examples of normative usage, beyond those offered by the schema.org pages. 

If you have digital assets that fall within the patterns in our book, then reusing them is typically just a question of copy, paste, fill in the blanks" and then verifying the validity of the resulting files with, e.g., the [schema.org validator](https://validator.schema.org/).

We strongly recommend all partners keep their JSON-LD files as close to the recommended pattern as possible. The more "in pattern" your content is, the more likely it will be discovered and (re)used in predictable ways.


### Requesting modifications to existing patterns

Sometimes, an existing pattern is close you what you need, but there are modifications that would make it a better fit (e.g. modifying spatial metadata to include depth more explicitly). Many of these modifcations are likely to be useful to the whole Federation, thus we encourage you to post an issue on our `odis-arch` GitHub repo [TODO:Add link]. There, you can describe the modification and how it would help improve the description and discovery of ocean data, and the ODIS team can help shape, verify, and integrate it into the core recommendations.


### Requesting new patterns

If there are no patterns that match your needs, or you feel that you're stretching an existing pattern too far, you can request help from the ODIS coordination team to help craft a new one. This process is an excellent opportunity for the  broader ODIS partnership to help review and co-develop the pattern, promoting wider interoperability. As above, post an issue on our `odis-arch` GitHub repo [TODO:Add link] describing the need, and ideally providing some example (meta)data that can be adapted.

What follows will be a few rounds of specification development, before we add the new pattern to the ODIS Book for all to benefit from and interoperate over.


## Creating a Sitemap

Now that you have content to share, you'll have to tell other agents on the web where to find it. This should be done by setting up a sitemap, that points to each JSON-LD file you wish the ODIS Federation to be aware of. 

An example ODIS sitemap can be seen here [TODO:Add link]

Note: If you have many thousands of entries, or you have subsets of links to share, you can use a 'sitemap of sitemaps'  approach, where one sitemap can point to several others.

### Frequency of change

Add metadata on how often you expect records in your sitemap to change - this will tell systems like OIH how often to reindex your holdings.


## Coming full circle: registering your sitemap in ODISCat






