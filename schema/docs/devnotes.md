# Notes

## Wanted to provide a brief update on the three meetings held this week.

Meeting 1
Sioeli Tonga
Domain:
Software used: CKAN framework
Brief:
Met with Sioeli Tonga with respect to onboarding their domain to OIH.  Their system is based on the CKAN
framework and we reviewed the some of the possible extension to CKAN that they could load to address OIH
needs.  This included the ckanext-dcat that would map the metadata to JSON-LD.   They are in contact with
CKAN developers for help on integration as well. We reviewed the
ckanext-dcat (https://github.com/ckan/ckanext-dcat) and sitemap extension to CKAN and they are going to set up
a dev server with these for use to test with.  

Meeting 2
Tavita Su'a
Domain: [SPREP](https://www.sprep.org/)
Software used: DCAN
Brief:
Met with Tavita Su'a with respect to onboarding their domain to OIH.  Their system is based on the DKAN framework.  
They are not on the latest version due to some dependance on older version functionality.  They have developed
a connection between DKAN and Drupal that does provide some flexibility.  They are currently in a Drupal 7
to Drupal 9 migration that is consuming a lot of their cycles at this time.  However, we did review the architecture
and the the possible use of  the JSON-LD plugin jsonld-schema (https://www.drupal.org/project/json_ld_schema)
for Drupal.  They are going to set up this up and also explore development of the sitemap along side that.

References:
https://pacific-data.sprep.org/dataset/coral-reef-threats-reefs-risk/resource/12ee5cc6-9fd1-4dfb-bef9-2479639a925a
https://pacific-data.sprep.org/dataset/bridging-research-management-gap-using-knowledge-exchange-and-stakeholder-engagement-aid
https://pacific-data.sprep.org/data.json?page=0
https://www.drupal.org/project/json_ld_schema

Meeting 3
Tim Tkint
Domain:
Example URL: https://www.marinetraining.eu/node/4079
Sitemap: https://www.marinetraining.eu/sitemap.xml
Software used:  generic web software
Brief:
Reviewed and made a few updates and fixes to the current JSON-LD.  This domain is almost ready to index.
There are a few items that need to be address a few things for him (not blocks to 
indexing).  Some issues with the sitemap and the range of resources with JSON-LD neither of which 
are major or hold up indexing was the small edits are made.  
We also reviewed approaches for declaring authoritative source in the document and some requested improvements
for the course thematic guidance.  


Meeting 4
Arno
Domain:  AquaDocs
Brief:
This is an interesting use case that may not be all that un-common (not sure).
This is the case of it's easier to generate the graph vs modify the web site.  
Approach, provide a graph distribution (recommend Data Objects package approach)

Meeting 5
Arno
Domain:  AquaDocs
Brief:
Also talked about: https://catalogue.odis.org/search/type=13



```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@graph": [
        {
            "@type": "Course",
          "@id": "https://www.marinetraining.eu/node/3396",
            "name": "RIGHT Project Kick-off meeting",
            "description": "\u003Cp\u003E\u003Cstrong\u003EProgramme\u003C/strong\u003E\u003C/p\u003E\n\n\u003Cp\u003E\u003Cstrong\u003E\u003Cu\u003E21st November\u003C/u\u003E\u003C/strong\u003E\u003C/p\u003E",
            "hasCourseInstance": {
                "@type": "CourseInstance",
                
                "name": "RIGHT Project Kick-off meeting",
                "url": "https://www.marinetraining.eu/node/3396",
                "location": {
                    "@type": "Place",
                    "name": "Zander Kaaes gate 8",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "Zander Kaaes gate 8",
                        "addressLocality": "Bergen",
                        "postalCode": "5015",
                        "addressCountry": "NO"
                    }
                }
            },
            "courseCode": "MTP-C-3396"
        }
    ]
}
```

https://schema.org/AlignmentObject

## DCAT notes

Need to look at what dealing with DCAT might look like.  

* https://data.gov.ie/dataset/national-monitoring-programme-for-phytoplankton-species-occurrence-in-aquaculture-production-areas.rdf
* https://data.gov.ie/dataset/harbour-limits-harbours-act-1996.rdf
* https://data.gov.ie/dataset/national-monitoring-programme-for-phytoplankton-species-occurrence-in-aquaculture-production-areas.ttl
* https://data.gov.ie/dataset/harbour-limits-harbours-act-1996.ttl
* https://data.gov.ie/dataset/collated-marine-habitats.ttl


## Old notes to incorporate above

### Documents

* For "Docs" focus on base CreativeWork type
* do a schema.org/Map example
* How can we leverage the "auto" work in schema.org for vessels
* DKAN and  CKAN are popular to exploring how to help people leverage 
those in OIH patterns is important
* Need a notebook to maintain and inspect the sources sitemaps and 
provide an assessment approach for the various parties. 
* Explore leveraging WikiData linkage with geo -> Place(WikiData) for 
example for things like "Gulf of Mexico"
* Project
  * hasCredentials
  * potentialAction
  * knowsAbout

### Indexing

* Need to ensure a provenance for the graph documents collected.
This will be both the object URN in the object store.  It will 
also be something like a nanopub prov.


## Pacific

SPC: https://www.spc.int/ 
Interested in: documents, spatial, vessels, training, people, org
CKAN

Other main partner: SPREP https://www.sprep.org/ 
Interested in: documents and spatial, training,
DCAN

Pacific Data Hub (https://pacificdata.org)
Pacific Environment Portal (https://pacific-data.sprep.org)

## EU

Peter (SeaDataNet)
Sandra (EurOcean)
Julie (EMODnet)

Kevin:  erdap needs to be leveraged (which is good since it support schema.org well)
CF conventions (netcdf format)   attributes for dataset discovery (in netcdf?)
darwin core (for bio)  (bioschemas.org)
Kevin is working on netcdf profiles

Addressing ambiguity in the graphs (shacl, json-ld parsing, https hell)

Sandra (eurocean):
use seadata cloud (work to match to standards (which ones?))

Julie & Conner (EMODnet):
Inspire standards (metadata and interop)
https://ec-jrc.github.io/dcat-ap-to-schema-org/
https://inspire.ec.europa.eu/metadata-codelist

Multi-lingual and Leveraging https://en.wikipedia.org/wiki/IETF_language_tag

Is there an OAI-PMH to schame.org graph mapping / tool

## Notes on training

20 minute video stack:

1. High-level concepts of OIH/ODIS
2. General introduction to our use of schema.org 
3. One video per pattern, walking through filling them in with correct data (implementation agnostic) 
4. Setting up the standard publishing/contribution environment 
5. Harvesting patterns in JSON/RDF 
6. Querying harvested material Additionally, some walkthroughs of how partners have set up their publishing/harvesting environments.

Each one perhaps 4-5 mins but trying to speak slowly so that we can translate them later :slightly_smiling_face:. I’m not sure what the best split would be, but perhaps following each of the headings on the Architecture page, but also one video per pattern.
We could load these videos on to this resources page as well, in addition to using them for training / awareness raising courses.

* 1 on Authoring (plus 6, one for each theme)
* 1 on Publishing
* 1 on Indexing
* 1 on Interfaces and Services


## CLME Plus

* https://clmeplus.marinetraining.org/
* https://clmeplus.marinetraining.org/advanced-search?search_api_fulltext=coral 
* https://clmeplus.marinetraining.org/advanced-search?search_api_fulltext=blue+economy


- spatial
- type of training (course, webinar, workshop, etc)
- format (online, onsite, blended)
- program type
- country
- city
- provider
- language
- cost
- structual component?
- ISCED  (controlled list?)
- CLME_ SAP catergory


## Books needs

The CLME Plus likely needs additional property  (is drupal 8 based).  

- https://www.drupal.org/project/schema_metatag

* leverage additional property
* language examples
* spatial examples
* need example for known list of terms
  * can be or not be machine dereferencable 
  * http://blog.schema.org/2012/05/schemaorg-markup-for-external-lists.html
  * https://schema.org/DefinedTerm
  


  @Doug - on the scenario Claudia is describing, please open an issue about one schema.org records referencing the same data / record in a system. There should be a comment field or similar that allows the creator to say that "my schema.org corrects an error in ..." 

  @Pier Luigi - will do. I need to see if I can blend that though with the current work for defining the authority for a record. This is more an annotation on a record or a new /corrected version of a resource 

  @Doug Yes, that must also account for the possibility that the authority 
  may be wrong 


  authoratative content and comments on same ID content
