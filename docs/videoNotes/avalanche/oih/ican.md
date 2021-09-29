# Spatial Approaches Overview
### Ocean InfoHub

<img src="./assets/logo.png" />

.notes: Pressing 2 will display these notes

.fx: titleslide

# presenter notes 
None at this time

---
# Outline

* General concepts
* Map as Creative Work
* Spatial geometry in schema.org and geosparql (graph query for spatial)
* Other related works

---

# General Concepts

* Schema.org and structured data on the web patterns are NOT a spatial database
* It's a means to discovery, but also potentially a means to alignment
* As seen in previous presentations it is also a means to connecting resources and knowledge

---

# Map as Creative Work

* In schema.org, a map is a CreativeWork, not a spatial gemoetry.  
* Would be used to reference documents (KML, GeoPackage, GeoJSON, etc)
* Could references printable maps etc.
* Is a sub-type of creative work (document) and would be semantically treated as such in searches.

Live visit: [OIH Maps](https://book.oceaninfohub.org/thematics/docs/maps.html)

---

# Spatial geometry in schema.org and geosparql

Live visit: [OIH Spatial Geometry](https://book.oceaninfohub.org/thematics/spatial/README.html)

See Also a special case of connecting concepts to spatial regions: [Marine Regions link example](https://github.com/iodepo/odis-arch/blob/schema-dev/book/thematics/spatial/graphs/gazetteer.json).  This shows connections to a [Marine Regions resource](http://www.marineregions.org/eezdetails.php?mrgid=48957) and [WikiData example](https://www.wikidata.org/wiki/Q16635).  

Using graphs to generate links of spatial resources.  [Geo KG Completion](https://book.oceaninfohub.org/tooling/notebooks/Exploration/GeoKGComplete/geocomplete.html)

