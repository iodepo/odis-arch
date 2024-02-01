# Getting started with ODIS

## Hello world

This page describes - at a high level - how a digital system with access to the Web can link itself into the ODIS Federation.

Any system providing data (in a broad sense, including documents, software code, etc) and/or services that are relevant to ocean science, management, policy, commerce, or other ocean-relevant activities is welcome to connect to ODIS. A light curation of ODIS nodes is performed by IODE's team, and the entire Federation self-regulates, voicing concern if they believe nodes.

## Preparing content 

All ODIS nodes share metadata about their holdings (datasets, documents, organisational information, etc) and services (APIs, portals) by exposing structured metadata catalogues over the web. 

The first step towards joining ODIS is to export metadata about your digital holdings as JSON-LD files, using schema.org Types and properties. Guidelines on how to shape these files is available here [TODO:Add links], and we provide a library of examples [TODO:Add link] and templates in this book to help nodes shape their submissions. Note, however, that any valid schema.org Type can be used to share metadata through the Federation. 

Additional semantics (i.e. beyond what schema.org can offer) can be embedded into these files using schema.org's additionalProperty, DefinedTerm, or similar property. More information on how to nest additonal semantics is availabler here: [TODO: Add links] 

You can store these files anywhere on the web (under your control), as long as they are accessible using standard web protocols. Many ODIS partners that have landing pages for their data sets or other digital assets choose to embed the JSON-LD inside HTML webpages [TODO:Add link to example]. 

### Reusing patterns

ODIS Partners have co-developed a library of JSON-LD/schema.org patterns (i.e. extended examples of how to format JSON-LD files using schema.org Types and properties) to help each other share content in a normative way. In general, these patterns give more complete examples of normative usage, beyond those offered by the schema.org pages. 

If you have digital assets that fall within the patterns in our book, then reusing them is typically just a question of copy, paste, fill in the blanks" and then verifying the validity of the resulting files with, e.g., the [schema.org validator](https://validator.schema.org/).


### Requesting new patterns

If there are no patterns that match your needs, you can request help from the ODIS coordination team to help craft a new one. This process is an excellent opportunity 


### Requesting modifications

## Creating a Sitemap

Now that you have content to share, you'll have to tell other agents on the web where to find it. This should be done by setting up a sitemap, that points to each JSON-LD file you wish the ODIS Federation to be aware of. 

If you have many thousands of entries, or you have subsets of links to share, you can use a 'sitemap of sitemaps'  approach, where one sitemap can point to several others.

### Frequency of change

Add metadata on how often you expect records in your sitemap to change - this will tell systems like OIH how often to reindex your holdings.

## Registering your organisation

Once you have some content you're ready to share across the ODIS Federation, you'll have to register your organisation so that it has an unambiguous identity on the web. It's important that this digital identity is sanctioned by your organisation's leadership and administration, such that it is an official identifier and kept up to date (like an ORCID for your organisation).

## OceanExpert 

## Alternatives

## Registering your (meta)data node(s)

Now that your organisation has an identifier on the web, you can register the data systems you wish to connect as ODIS nodes. One organisation can operate many such nodes (e.g. for different types of data, services, etc). 

### ODISCat

ODISCat has a dedicated field for you to let the ODIS Federation where your sitemap is, so they can access your metadata catalogue and explore your holdings.






