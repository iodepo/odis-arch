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