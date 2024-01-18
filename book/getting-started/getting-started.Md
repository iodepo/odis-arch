# Getting started with ODIS

## Hello world

This page describes - at a high level - how a system can link itself into the ODIS Federation. 


## Preparing content 

All ODIS nodes share metadata about their holdings (datasets, documents, organisational information, etc) and services (APIs, portals) by exposing metadata catalogues over the web. 

The first step towards joining ODIS is to export metadata about your digital holdings as JSON-LD files, using schema.org Types and properties to handle the semantics within them. 

You can store these files anywhere on the web (under your control), as long as they are accessible using standard web protocols. You can even embed them inside HTML webpages, as many ODIS partners who have landing pages for their datasets or services do. 

### Reusing patterns
### Requesting new patterns
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






