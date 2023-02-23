# ADRs



## Notes

- Git checkout error on Windows: error: invalid path 'workflows/output/2023-02-08T00:09_sitemaps.csv'
- re: book's recommendations for Spatial (spatialCoverage vs WKT vs GeoJSON)
  - came across aShepherd's comments/decision to follow ODIS conventions (bottom comment at https://github.com/ESIPFed/science-on-schema.org/issues/101) which (according to his take) is:
    - schema.org `spatialCoverage` (for Google friendliness)
    - WKT
    - GeoJSON
       -  to discuss today
- PL: patterns separate from Book repo?
  - generic repo for shared patterns
  - Doug: GitHub can link repos
- PL: order of properties in patterns (alphabetic or curated by us)
  - agreed to use alphabetical, as these patterns will be used by so many groups
- PL: for urls and external links, always use the consistent style
- JM: formatting rules
   - spaces only (no tabs)
   - 4 spaces for each sub-property
   - citation needed
     - https://www.ecma-international.org/publications-and-standards/standards/ecma-404/
   - case sensitivity of property/values
     "@type": "Thing"






Make ADRs: 

- Do not include @id for properties under the assumption that they are not issues them as nodes.  Kept for the top level, and clearly state only to this if it is a resolvable IRI.  Making it a FDO.  (ref: https://www.w3.org/TR/json-ld/#node-identifiers)
- Keep each minimal, if a property requires or supports a type, just show the minimal properties for that embedded type, and link out to the full specification in an independent pattern by adding a link in the embedded Type's description property. 
- how to force a string literal to be a URI, or at least indicate/express that a value is of type URL to support confident filtering: We will recommend typing URIs where possible, guidance to be added to documentation (see below)
- When we see that a property expects "Thing" as a value, we understand this as any arbitrary string, PID to an ontology class, etc. We do not understand this as needing a subclass of schema.org:"Thing", as the example for instrument in the Action type notes "pen" as a valid entry.
- In our patterns, we don't necessarily list all properties for each Type, just those we think the ODIS community can work with now. We encourage pull requests or suggestions for more, and will add them based on need / request. 
- For Dates : always use DateTime with ISO 8601 compliance. (YYYY-MM-DD)
- In cases where (like in Niko's records) there is no @id for a JSON record we need an approach that allows us to link resources together
- Symphony related:  If a software package hosts it's own data, then the software description metadata should describe that data as datasets so it can be found
- Assuming that the page supports content negotiation, the @id of the JSON-LD can be the URL of the web page hosting it.  
- detail how to leverage the sitemap index to point to multiple sitemap and then designate one or more as ones for OIH to index via robots.txt


Material for documentation linked to ADRs
- How to declare a literal as a URI


Consider ADR:
- create dedicated repo for patterns to improve management across graphs
- create IRIs for the latest released version of each pattern 
- Add the IRIs for latest released version of each pattern to the respective @id of that pattern 
- add docs for shacl validation 

Lead documentation with: 


```    "identifier": {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/orcid",
        "value": "0000-0002-2257-9127",
        "url": "https://orcid.org/0000-0002-2257-9127",
        "description": "Optional description of this record..."
      },
      ```

To force to URI

```
    "identifier": {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/orcid",
        "value": "0000-0002-2257-9127",
        "url": {
            "@value": "https://orcid.org/0000-0002-2257-9127",
            "@datatype": "http://www.w3.org/2001/XMLSchema/anyURI"
        }
        "description": "Optional description of this record..."
      },
      ```

## References

Some initial work and notes on the use of Architecture Decision Records

* https://github.com/joelparkerhenderson/architecture-decision-record
* https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/templates/decision-record-template-by-michael-nygard/index.md 



