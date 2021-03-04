# Publishing

## About

This page describes the publishing process for structured data 
on the web approach OIH will use.  

Note many software packages you might be using are already 
implementing this approach and could make implementation, in that
case, easier.  
See the section [Existing support in software][## Existing support in software]

## Basics

The basics of the approach can be seen below.  

![](./images/example1Flow.png)

A brief overview of this elements is provide here.  For more
detail see the [Elements in detail][## Elements in detail]
section below.

### robots.txt (optional)

This is an optional step, but a robots.txt file can be used to define 
the sitemap and even option agent names to associate with the sitemaps.
This document is not required, but for those who use such a document
and wish to leverage it, that is an option.

### sitemap

Following the approaches below an XML document that points to the 
various resources to be indexed needs to be generated.  Of 
particular use is the lastmod node to indicate the date of
last modification to allow continued indexing without the need
for a full site index each time.

### JSON-LD in landing pages

The last element is the creation of the JSON-LD data graphs 
describing the resources leveraging the schema.org vocabulary. 
These JSON-LD documents need to be placed in the pages referenced
by the sitemap.  

## Overview 
![](./images/flow.png)

The architecture defines a workflow for objects, a \"digital object
chain\". Here, the digital object (DO) is the data graph such as the
JSON-LD package in a landing page.

The chain is the life cycle connecting; authoring, publishing,
aggregation, indexing and searching/interfaces.

1. Providers are engaged to provide structured data on the web and
    provide robots.txt and sitemap.xml entries to facilitate indexing.
2. Harvesting will be done using the Gleaner package developed as part
    of NSF\'s EarthCube Project 418/419. Harvesting is simply a further
    leveraging of the web architecture approach and it is expected that
    other harvesters with perhaps community or interface specific goals
    will develop.
3. The results of the Gleaner harvest (data graphs, reports,
    validations and generated indexes) are stored in an S3 compliant
    object store.
4. Generated graph is loaded into a triplestore (Blazegraph in this
    case) for query and analysis. Future options include leveraging the
    approach for spatial or other indexes.
5. From there interfaces can be built such as simple web interfaces,
    GraphQL or other interface options. Spatial, full text or other
    indexes can be built. It\'s also possible to explore connections to
    other research graphs such as the Freya Project or others.


## Elements in detail 

### robots.txt

OPTIONAL: Providers may decide to generate or modify their robots.txt 
file to provide guidance to the aggregators. 
The plan is to use the Gleaner software (gleaner.io) as well as some 
Python based notebooks and a few other approaches in this test.

Gleaner uses an agent string of EarthCube_DataBot/1.0 and this can be 
used a robots.txt file to specify alternative sitemaps and guidance. 
This also allows a provider to provide guidance to Google and other potential 
indexers both for allow and disallow directives.

```txt
Sitemap: http://samples.earth/sitemap.xml

User-agent: *
Crawl-delay: 4
Allow: /

User-agent: Googlebot
Disallow: /id

User-agent: EarthCube_DataBot/1.0
Allow: /
Sitemap: http://samples.earth/test.
```

### sitemap.xml

Providers will need to expose a set of resource
landing pages using a sitemap.xml file. As noted above, providers 
can expose a sitemap file to just the target agent 
to avoid indexing test pages by commercial providers.  You may wish 
to do this during testing or for other reasons.  Otherwise, 
a sitemap.xml file exposed in general from somewhere in your site is 
perfectly fine.  

Information on the sitemap structure can be found at sitemaps.org.

It is encouraged to use the sitemap lastmod node 
to provide guidance to indexers on page updates. 
Additionally indexers may test ways to evaluate additions and 
removals from the sitemap URL set to manage new or removed resources.  

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/site0.9">
   <sitemap>
      <loc>http://samples.earth/sitemap_websites_sampleseaxml</loc>
      <lastmod>2004-10-01T18:23:17+00:00</lastmod>
   </sitemap>
   <sitemap>
      <loc>http://samples.easitemap_doclouds_igsndatagraphs.xml</loc>
      <lastmod>2005-01-01</lastmod>
   </sitemap>
</sitemapindex>
```

### Including JSON-LD in your resource page

Resources  will need a landing page with a JSON-LD data graph placed in it via a

```html
<script type="application/ld+json"></script>
```

entry in the document head.

An example data graph can be seen below.   However, check the various 
thematic sections for more examples for a given thematic area.  

Providers may also wish to provide content negotiation for type application/ld+json 
for these resources. Some indexers,  like Gleaner, will attempt to negotiate for i
the specific serialization and this will likely lighten the load on the servers going forward.

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@type": ["Service", "ResearchProject"],
    "legalName": "Example Data Repository",
    "name": "ExDaRepo",
    "url": "https://www.example-data-repository.org",
    "description": "The BCO-DMO resource catalog offers free and open access to publicly funded research products whose field of study are biological and chemical oceanography.",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.example-data-repository.org/logo.jpg"
    },
    "contactPoint": {
      "@id": "https://www.example-data-repository.org/about-us",
      "@type": "ContactPoint",
      "name": "Support",
      "email": "info@example-data-repository.org",
      "url": "https://www.example-data-repository.org/about-us",
      "contactType": "customer support"
    },
    "funder": {
      "@type": "FundingAgency",
      "@id": "https://dx.doi.org/10.13039/10000001",
      "legalName": "National Science Foundation",
      "alternateName": "NSF",
      "url": "https://www.nsf.gov/"
    }
}
```

## Existing support in software

Many content management approaches and packages may already have support for this pattern.  A list of
some of these and some links to starting points for their support follows.  

- [Drupal](https://www.drupal.org/docs/contributed-modules/schemaorg-metatag)
- [CKAN](https://ckan.org/2018/04/30/make-open-data-discoverable-for-search-engines/)
- [DSpace](https://journal.code4lib.org/articles/13191)
- [ERDDAP (native support)](https://www.ncei.noaa.gov/erddap/index.html)
- [OPeNDAP (native support)](https://www.opendap.org/)
- [GeoNode](http://geonode.org/)
  - [schema.org issue ref](https://github.com/GeoNode/geonode/issues?q=schema.org+)


