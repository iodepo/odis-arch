# About this page

This page is aimed at technical teams who wish to link their (meta)data to the ODIS Federation. It clarifies how ODIS Partners should interpret the specifications and standards which are used to share the metadata needed to construct the knowledge graphs used for discovery and other purposes facilitated by linked open data.

# Background

Each ODIS Partner operating one or more Nodes in the ODIS Federation shares at least one metadata catalogue which lists their digital assets (datasets, software, services, etc). Each of these catalogues can be converted into a knowledge graph, and they can be combined to form a Federation-wide knowledge graph to help agents discover, access, and use each Partner's capacities.

A "graph" is a mathematical object that consists of "nodes" and the "edges" that connect them. Intuitively, a graph looks like a network (which is actually a kind of graph). 

This page documents some particulars of how the ODIS discovery graph is implemented. Consistency in this implementation across Partners is essential for interoperability. 

# The ODIS discovery graph: a metadata graph

The foremost concept guiding the ODIS discovery graph's implementation is that it is a graph of metadata ( i.e. its nodes and edges describe something other than themselves). This means that the foundational element of the graph is a node (i.e. a reference node) that is about something other than itself (like a Dataset, Person, Organization, etc). 

It's a linked data graph, comformant to [an RDF graph](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph)

# Serialisation: JSON-LD

JSON-LD is a format from which graphs can easily be constructed. ODIS follows the [JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#how-to-read-this-document), a non-normative document hosted by the W3C. 

To promote global interoperability beyond its domain and community, ODIS attempts to follow this guidance as closely as possible. 

## Objects

In JSON(-LD) syntax, anything inside a pair of braces is an [object](https://datatracker.ietf.org/doc/html/rfc8259#section-4), and one object may have one or more other objects nested within it.  

[Add simple representation]

Some JSON-LD objects are, de facto, FAIR Digital Objects, assuming they have a reference node (see below) with a persistent, unique, and dereferenceable identifier, well-described semantics, license and provenance information, and other attributes described in the FAIR Data Principles.

## Nodes

### The general concept

JSON-LD nodes are equivalent to RDF nodes:

> node
> A node in an RDF graph, either the subject and object of at least one triple. Note that a node can play both roles (subject and object) in a graph, even in the same triple.
[JSON-LD 1.1 specification - terms imported from other specifications](https://www.w3.org/TR/json-ld/#terms-imported-from-other-specifications)

### Typed nodes

[JSON-LD 1.1 specification - Typed values](https://www.w3.org/TR/json-ld/#typed-values)

### Reference nodes

In a true linked (open) data implementation, one should be able to unambiguously and efficiently identify any node. In theory, every node could have an IRI or other dereferenceable (persistent) identifier; however, this would dramatically inflate the number of triples, and thus the size of a graph, immensely. Instead, one can provide a dereferenceable IRI or PID for _one node_ for every JSON-LD _file_ that defines a (relatively small) graph describing one thing (like a Person, Organization, Dataset, etc). This identified node is known as the _reference node_. Other nodes that are linked to the reference node may not have their own identifiers, but they aren't far away (logically or topologically) from the reference node.

[Add simple visual]

In a JSON-LD file, one should define a reference node using the JSON-specific `@id` and `@type` [keywords](https://www.w3.org/TR/json-ld/#dfn-keyword). The `@id` keyword should have a value that points to its own representation:

> To be able to externally reference nodes in an RDF graph, it is important that nodes have an identifier. IRIs are a fundamental concept of Linked Data, for nodes to be truly linked, dereferencing the identifier should result in a representation of that node. This may allow an application to retrieve further information about a node.
>
> In JSON-LD, a node is identified using the @id keyword:
[JSON-LD 1.1 specification - node identifiers](https://www.w3.org/TR/json-ld/#node-identifiers)

The value of the `@type` keyword defines what the thing described by some metadata is supposed to be. When used in conjunction with an `@id` keyword, this becomes a [node type](https://www.w3.org/TR/json-ld/#dfn-node-type) which tells us what that reference node (and the nodes that describe it) is supposed to represent (e.g. a Person, Dataset, Vehicle, or Software)

>type map
>A type map is a map value of a term defined with @container set to @type, whose keys are interpreted as IRIs representing the @type of the associated node object; the value must be a node object, or array of node objects. If the value contains a term expanding to @type, its values are merged with the map value when expanding. See the Type Maps section of JSON-LD 1.1 for a normative description.
[JSON-LD 1.1 specification - type map](https://www.w3.org/TR/json-ld/#dfn-type-map)

## Edges

# Semantics: schema.org

> active context
> A context that is used to resolve terms while the processing algorithm is running.
[JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#json-ld-specific-term-definitions)

# Topological considerations

## Minimalism 

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

Better:
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
Where `"@id": "http://someorg.org/orgMetadata.json"` would take one to another JSON-LD document with metadata about the Organisation (typed as `Organization`). 

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

# Other approaches

## Subjects as reference nodes
## Self-describing documents

