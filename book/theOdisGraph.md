# About this page

This page is aimed at technical teams who wish to link their (meta)data to the ODIS Federation and its allied networks. It clarifies how ODIS Partners should interpret the specifications and standards which are used to share the metadata needed to construct knowledge graphs used for discovery and other purposes.

# Background


> [!NOTE]
> A "graph" is an object that consists of "nodes" (which represent things) and the "edgest connect them (and define how the nodes relate to each other). Intuitively, a graph looks like a network (which is, itself, a kind of graph). 

This page documents some particulars of how the ODIS discovery graph is co-implemented by the partners in the ODIS Federation (henceforth, "Partners"). Consistency in this implementation across Partners is essential for interoperability. 

Each ODIS Partner in the ODIS Federation shares at least one metadata catalogue which lists their digital assets (datasets, software, services, etc), using JSON-LD serialisation/format and, primarily, schema.org semantics. 

Each of these catalogues can be harvested over the Web and converted into a collective knowledge graph (or other construct, like a triplestore).

IODE provides coordination of the ODIS Federation, through its ODIS Programme Component (https://odis.org). To do so, it harvests all ODIS Partner asset catalogues and constructs a knowledge graph which it serves back to the Federation and any other user on the Web. To enable such integration by IODE (or any other user), it is vital that all partners of the ODIS Federation share common implementation norms for their asset / metadata catalogues.

# The ODIS discovery graph: Describing and linking assets across a global partnership

As noted above, the ODIS discovery graph is built from the asset catalogues of the partner systems in the ODIS Federation. Those asset catalogues:
 - tell the Web what entities/resources each ODIS Partner is concerned with (e.g. datasets hosted, services provided, material objects interacted with), representing them as nodes in the graph,
 - provide selected (meta)data about each asset to aid in its discovery and basic characterisation,
 - link (meta)data about each asset to that about others with well-defined relations (i.e. graph edges qualified by, primarily, schema.org terms), and
 - link back to complete digital representations, subject data, or service endpoints of the assets described (where available).

As such, the ODIS discovery graph describes and links a wide range of entities that the global partners in the ODIS Federation work with. 

More technically, the ODIS discovery graph is a linked data graph, which conforms to [the Resource Description Framework (RDF) specifications](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). It is built from asset catalogues serialised in [Java Script Object Notation for Linked Data (JSON-LD)](https://www.w3.org/TR/json-ld/), primarily using [schema.org semantics](https://schema.org/). The sections below will explore this in more detail.

## Serialisation: JSON-LD

JSON-LD allows graph-friendly representation of digital objects and their properties, with practically focused [design principles](https://www.w3.org/TR/json-ld/#design-goals-and-rationale). ODIS follows the [JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#how-to-read-this-document), a non-normative document hosted by the W3C.  To promote global interoperability beyond its domain and community, ODIS attempts to follow this guidance as closely as possible. 

### Objects

> [!NOTE]
> Some JSON-LD objects are, de facto, FAIR Digital Objects, assuming they are accessible, have a reference node (see below) with a persistent, unique, and dereferenceable identifier, well-described semantics, license and provenance information, and other attributes described in the FAIR Data Principles. All ODIS JSON-LD documents are FAIR Digital Objects.


In JSON(-LD) syntax, anything inside a pair of braces ("{}") is an [object](https://datatracker.ietf.org/doc/html/rfc8259#section-4), and one object may have one or more other objects nested within it.  

Below, is a very simple JSON-LD record which contains two objects, one defining the semantic context of the record (i.e. the schema.org vocabulary) which is nested in an object describing a Person named Jane Doe.

```json
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@id": "https://example.org/id/x",
  "@type": "Person",
  "name": "Jane Doe"
}
```

Below, the same "Person" object has another object describing a "Place" nested within it, as the value of the `schema:workLocation` property. In the graph world, this means that the nodes (see below) that are linked to and describe the reference node "https://example.org/id/x" are linked (via the workLocation edge) to another cluster of nodes describing a "Place", with reference node "https://place-ids.org/25432".

```json
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@id": "https://example.org/id/x",
  "@type": "Person",
  "name": "Jane Doe",
  "workLocation": {
    "@type": "Place",
    "@id": "https://place-ids.org/25432",
    "address": "54 Ocean Drive, 23521 Ocean City, CountryName",
    "name": "Place name"
  }
}

```


### Nodes

#### The general concept

JSON-LD nodes are equivalent to RDF nodes:

> node
> A node in an RDF graph, either the subject and object of at least one triple. Note that a node can play both roles (subject and object) in a graph, even in the same triple.
[JSON-LD 1.1 specification - terms imported from other specifications](https://www.w3.org/TR/json-ld/#terms-imported-from-other-specifications)

The JSON-LD records above encode graphs, where each value is a node and each property is an edge. Depending on which side of an edge a node is, it can be understood as an RDF subject or object. For example, the subject of "name" is the reference node "https://example.org/id/x", and the object of "name" is "Jane Doe", i.e. "the name of the resource identified as 'https://example.org/id/x' in the knowledge graph is 'Jane Doe'".

The basic object describing "Jane Doe" represented as a graph structure looks like: 
![image](https://github.com/user-attachments/assets/c7635c29-a043-4a50-85a0-e23a754bb587)

The "Jane Doe" object with the nested "Place" object visualised: 

![image](https://github.com/user-attachments/assets/a3e5ae13-472d-4529-b928-d6cfc0abd017)


#### Typed nodes

>A value with an associated type, also known as a typed value, is indicated by associating a value with an IRI which indicates the value's type.
>[JSON-LD 1.1 specification - Typed values](https://www.w3.org/TR/json-ld/#typed-values)

Some nodes in a JSON-LD graph can be "typed" - in other words, classified as representative of a particular entity. This can be read as "this node is of type X". In the ODIS graph, the primary mode of typing follows the node typing convention specified here: https://www.w3.org/TR/json-ld/#dfn-node-type

As an example, dervied from the JSON-LD specification, consider:

```json
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@id": "http://me.markus-lanthaler.com/",
  "@type": "Person",
  "name": "Markus Lanthaler"
}
```

In other words, the node with `@id` "http://me.markus-lanthaler.com/" (which resolves to a JSON-LD document) is declared to be of type "http://schema.org/Person". 

The Types used in ODIS are always [schema.org Types](https://schema.org/docs/full.html) to ensure cross-Federation interoperability. However, schema.org often lacks domain- or application-specific Types. To resolve this, partners can choose the closest schema.org Type relevant to their asset, and then add further classification (e.g. from other semantic resources) using the schema.org `additionalType` property.

For example, schema.org does not have a Type for "Sensor" (which could be used as a value for schema:`instrument`). One can thus use the schema:`Product` Type, and use semantics from the [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/) to add an additional Sensor Type:

```json
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@id": "http://my-sensor-catalogue.org/23526",
  "@type": "Product",
  "additionalType": [
    "http://www.w3.org/ns/sosa/Sensor",
    "Sensor"
  ]
  "name": "RX-462 magnetometer"
}
```

Notice that both a URL and textual value is included in an array (the value of `additionalType`). This is done to ensure discoverability with both defined URIs/URLs and common string-based names. Text strings used here can be multilingual, to further increase discovery. 


#### Reference nodes and the use of `@id`

In a true linked (open) data implementation, one should be able to unambiguously and efficiently identify any node. In theory, every node could have an IRI or other dereferenceable (persistent) identifier; however, this would dramatically inflate the number of triples, and thus the size of a graph. Instead, one can provide a dereferenceable IRI or PID for _one node_ for every JSON-LD _record_ that defines a (relatively small) graph describing one thing (like a Person, Organization, Dataset, etc). This identified node is known as the _reference node_. Other nodes that are linked to the reference node may not have their own identifiers, but they aren't far away (logically or topologically) from the reference node.

[Add simple visual]

In a JSON-LD file, one should define a reference node using the JSON-specific `@id` and `@type` [keywords](https://www.w3.org/TR/json-ld/#dfn-keyword). The `@id` keyword should have a value that points to its own representation:

> To be able to externally reference nodes in an RDF graph, it is important that nodes have an identifier. IRIs are a fundamental concept of Linked Data, for nodes to be truly linked, dereferencing the identifier should result in a representation of that node. This may allow an application to retrieve further information about a node.
>
> In JSON-LD, a node is identified using the @id keyword:
[JSON-LD 1.1 specification - node identifiers](https://www.w3.org/TR/json-ld/#node-identifiers)

As described above, value of the `@type` keyword defines what the thing described by some metadata is supposed to be. When used in conjunction with an `@id` keyword, this becomes a [node type](https://www.w3.org/TR/json-ld/#dfn-node-type) which tells us what that reference node (and the nodes that describe it) is supposed to represent (e.g. a Person, Dataset, Vehicle, or Software).

>type map
>A type map is a map value of a term defined with @container set to @type, whose keys are interpreted as IRIs representing the @type of the associated node object; the value must be a node object, or array of node objects. If the value contains a term expanding to @type, its values are merged with the map value when expanding. See the Type Maps section of JSON-LD 1.1 for a normative description.
[JSON-LD 1.1 specification - type map](https://www.w3.org/TR/json-ld/#dfn-type-map)

#### Multi-typing

JSON(-LD) allows objects to have multiple types, which allows the use of properties from any of the types included (i.e. a superset of all permissable properties for each type). 

While this will pass technical/syntactic validation in many systems, one must be very careful not to type a (reference) node with semantically incompatible type, simply because one wants to use a bigger set of properties. For example, if one types an object as an "Action" and a "Dataset", a semantic conflict occurs: There is no thing in the world that is both an Action and a Dataset at the same time. 

❌Incompatible type semantics

```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@id": "https://myJSONfiles.org/2534645.json",
    "@type": [
      "Action",
      "Dataset"
    ],
...
```

Some types, however, can co-exist. For example, something like a JSON-LD record can be understood as both a "Dataset" and a "DigitalDocument". 

✔️ Compatible type semantics

Fine - compatible semantics
```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@id": "https://myJSONfiles.org/2534645.json",
    "@type": [
      "DigitalDocument",
      "Dataset"
    ],
...
```



TODO: explain why the StructuredValue + other variable type works
```json
{
    "@context": {
        "@vocab": "https://schema.org/"
    },
    "@id": "URL:  Optional. A URL that resolves to *this* JSON-LD document, NOT the URL of the CreativeWork that this JSON-LD document describes. To link to the CreativeWork itself, please use 'url' and/or 'identifier')",
    "@type": "Action",
    "additionalProperty": {
      "@type": "PropertyValue",
      "propertyID": "https://schema.org/hasDigitalDocumentPermission",
      "value": {
        "@type": [
          "StructuredValue",
          "DigitalDocumentPermission"
          ],
        "permissionType": "ReadPermission"
        }
    },
    "actionStatus":  {"@type": "ActionStatusType"},
...
```

### Edges

# Semantics: schema.org

> active context
> A context that is used to resolve terms while the processing algorithm is running.
[JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#json-ld-specific-term-definitions)

## Topological considerations

### Minimalism 

if you can link to another @id, do so. 

Good: 
```json
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@id": "http://someorg.org/our-metadata/dataProduct-332324.json",
  "@type": "Dataset",
  "name": "A Data Product about X",
  "identifier": "http://someorg.org/our-data/dataProduct-332324.parquet",
  "encodingFormat": "application/vnd.apache.parquet",
  "creator": {
    "@type": "Organization",
    "name": "Some Org",
    "url": "http://www.someorg.com/"
  }
}
```

A better approach is to use a [node reference](https://www.w3.org/TR/json-ld/#dfn-node-reference), which uses the `@id` keyword to point to another JSON-LD document which contains the information of interest.


```json
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@id": "http://someorg.org/our-metadata/dataProduct-332324.json",
  "@type": "Dataset",
  "name": "A Data Product about X",
  "identifier": "http://someorg.org/our-data/dataProduct-332324.parquet",
  "encodingFormat": "application/vnd.apache.parquet",
  "creator": {
    "@id": "http://someorg.org/orgMetadata.json"
  }
}
```
Here, `"@id": "http://someorg.org/orgMetadata.json"` is the node reference and would take one to another JSON-LD document with metadata about the Organisation (typed as `Organization`). 

This has many benefits. For example, if anything in `"@id": "http://someorg.org/orgMetadata.json"` changes, any other metadata records which reference it will remain current, without the need to update each one of them. This is especially useful in federated and/or distributed systems, where updates may not percolate automatically if at all.

In some cases, however, one may wish to "freeze" metadata associated with a reference node, rather than referencing a "live" metadata file externally. In such cases, adding a note about why this was done to the metadata in question is recommended. 

# Describing graph elements: metadata about metadata

```json
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@id": "http://someorg.org/metadata-about-orgMetadata.json",
  "@type": "Dataset",
  "name": "Metadata about Some Organisation",
  "identifier": "http://someorg.org/orgMetadata.json",
  "encodingFormat": "application/json+ld",
  "dateCreated": "2024-02-13",
  "dateModified": "2024-05-23",
  "datePublished": "2024-05-23",,
  "creator": {
    "@type": "Organization",
    "name": "Some Org",
    "url": "http://www.someorg.com/"
  },
  "maintainer": {
    "@type": "Organization",
    "name": "Some Org",
    "url": "http://www.someorg.com/"
  }
}
```

