# Publishing

## About

This page describes the publishing process for structured data 
on the web we will use.  This model is what people implementing
an approach on existing infrstructure would use.

Note many software packages you might be using are already 
implementing this approach and should make adaption, in that
case, easier.

## Existing support in software

Reviewing plugins or approach for platforms in use:

- [Drupal](https://www.drupal.org/docs/contributed-modules/schemaorg-metatag)
- [CKAN](https://ckan.org/2018/04/30/make-open-data-discoverable-for-search-engines/)
- [DSpace](https://journal.code4lib.org/articles/13191)
- [ERDDAP (native support)](https://www.ncei.noaa.gov/erddap/index.html)
- [OPeNDAP (native support)](https://www.opendap.org/)
- [GeoNode](http://geonode.org/)
  - [schema.org issue ref](https://github.com/GeoNode/geonode/issues?q=schema.org+)

## Basics

The basics of the approach can be seen below.  

### robots.txt

OPTIONAL: Providers may decide to generate or modify their robots.txt file to provide guidance to the aggregators to be used in this sprint. The plan is to use the Gleaner software (gleaner.io) as well as some Python based notebooks and a few other approaches in this test.

Goals here will be to provide guidance to indexers from the providers.

Gleaner used an agent string of EarthCube_DataBot/1.0 and this can be used a robots.txt file to specify alternative sitemaps and guidance. This also allows you to provide guidance to Google and other potential indexers both for allow and disallow directives.

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

Providers in the sprint will be required to expose a set of sample landing pages using a sitemap.xml file. As noted above, providers can expose a test sitemap file to just the target agent in this sprint to avoid indexing test pages by commercial providers.

Information on the sitemap structure can be found at sitemaps.org.

A goal of this section will be to discuss the use of sitemap lastmod to provide guidance to indexers on sample updates. Additionally indexers may test ways to evaluate additions and removals from the sitemap URL set to manage create, update, delete and edit branches.

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

The final tan in the tangram is the landing page. Samples will need a landing page with a JSON-LD data graph placed in it via a

```html
<script type="application/ld+json"></script>
```

entry in the document head.

An example data graph can be seen below but we will be updating this with a better example and also provide some more technical details for publishers for things like schema and validation approaches.

Providers may also wish to provide content negotiation for type application/ld+json for these resources. Some indexers,  like Gleaner, will attempt to negotiate for the specific serialization and this will likely lighten the load on the servers going forward.

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