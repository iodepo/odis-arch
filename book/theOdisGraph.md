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

## Nodes

> node
> A node in an RDF graph, either the subject and object of at least one triple. Note that a node can play both roles (subject and object) in a graph, even in the same triple.
[JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#terms-imported-from-other-specifications)


In a JSON-LD file, one can define a reference node using the `@id` and `@type` variables 

## Edges

# Semantics: schema.org

> active context
> A context that is used to resolve terms while the processing algorithm is running.
[JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld/#json-ld-specific-term-definitions)

# Topological considerations

## Minimalism 

if you can link to another @id, do so. 

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

