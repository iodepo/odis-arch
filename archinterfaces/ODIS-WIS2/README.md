# WIS2 (WMO) OIH interfacing

## About

Initial work on aligning OIH holdings to [WMO](https://wmo-im.github.io/wcmp2/standard/wcmp2-DRAFT.html)

## Related GitHub ticket

- https://github.com/iodepo/odis-arch/issues/238 (WMO core metadata profile to ODIS pattern)
- https://github.com/iodepo/odis-arch/issues/304 (Provide sample mapping/GeoJSON to WMO)


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

Needs 
- boilerplate about ODIS and the vision of the interop with OIH and WIS2
- workflow image (need to chat with them about how much to show in that)
- https://docs.ogc.org/DRAFTS/20-004.html#clause-crawlable-catalog 
