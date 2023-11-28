# WMO OIH interfacing

## About

Initial work on aligning OIH holdings to [WMO](https://wmo-im.github.io/wcmp2/standard/wcmp2-DRAFT.html)

## Related GitHub ticket

- https://github.com/iodepo/odis-arch/issues/238 (WMO core metadata profile to ODIS pattern)
- https://github.com/iodepo/odis-arch/issues/304 (Provide sample mapping/GeoJSON to WMO)

## Notes and TODOs

- [ ] ID:  unique ID in catalog that align to the follow pattern.  We can build this and
  add it to the PROV graph.  We need an agreement to allow these records to be sent to WMO 
  ``` 
      "id": "urn:x-wmo:md:xxg:odis:$LOCAL_ID"
      xxg  iso 3166 country list
      g = region association a-f  
  ```
- [ ] keywords -> free, properties.themes (concepts and schema)
- [ ] time, can be null, interval, instant  iso8601
- [ ] properties.theme, need at least one from   "scheme": "https://github.com/wmo-im/wcmp2-codelists/blob/main/codelists/earth-system-discipline.csv"
- [ ] conforms to, points to json schema  (need to get this)   https://github.com/wmo-im/wcmp2/blob/main/schemas/wcmp2-bundled.json  
- [ ] properties.contacts requires:  name and org  (can be one to many)   roles is from a vocabulary
- [ ] look at properties.type for "process"
- [ ] properties.created is the date the metadata record was created (required) 
	- [ ] may need to be the prov
	- [ ] may need to make required
    - [ ] properties.updated is optional
- [ ] properties.wmo:dataPolicy (put recommended for now, while we sort out the details)
- [ ] properties.links (the subject URI)  (can be URI or URL to the landing page)
- [ ] need to the JSON-schema and WMO SHACL for these generated records
- [ ] KPI (key performance indicators)  validation / ranking...   related to FAIR CODATA  ???  would love links to this KPI checks


#### ROA

Resource-Oriented Architecture (ROA) is an architectural style for designing network-based software applications. This style prioritizes resources, their identification, representation, and the links between them over the actions performed on those resources (as in many object-oriented architectures).

Here are key principles of ROA:

1. **Resources:** In a ROA, every piece of information and service is considered a resource. These resources are identifiable and can be accessed through a unique identifier, typically a URI.

2. **Links and Connectedness:** Resources reference each other through links, creating a web of interconnected resources. This allows for easy navigation between related resources.

3. **Standard Methods:** In ROA, resources are manipulated using standard HTTP methods (like GET, POST, PUT, DELETE). This makes the API predictable and easy to understand.

4. **Representation-Oriented:** Rather than being concerned with implementation details, ROA focuses on how resources are represented to clients. Different clients might receive different representations of the same resource.

5. **Stateless:** Similar to RESTful systems, ROA prefers stateless operations, where each request from client to server must contain all the information necessary to understand and respond to the request.

6. **Address-ability:** Every resource has a unique address, typically a URL, which can be bookmarked, typed into a browser, or passed around by an application.

ROA is most notably realized in the design of RESTful APIs, which are intended to interact with web resources. It's focused on leveraging the protocols and technologies of the web (like HTTP, URIs, and MIME types) rather than creating new standards or protocols.


## Notes:

* WMO WCMP 2 target April 2024 for 1.0 stamp ref: https://wmo-im.github.io/wcmp2/ 
* requirements: https://wmo-im.github.io/wcmp2/standard/wcmp2-DRAFT.html#_overview_2 
* https://github.com/wmo-im/wis2-gdc 
  * TODO:  SHACL for Table 2. WCMP record core properties 
* mqtt vs pygeoapi 