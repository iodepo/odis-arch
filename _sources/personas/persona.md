# Personas

## About 

The OIH system can be viewed as involving three personas.  These are
briefly presented here.

```{panels}
:column: col-4
:card: border-2
![](../images/personna.svg) 
Publisher
^^^
A key persona whose activities are covered in detail in [Publishing patterns for OIH](../publishing/publishing.md)
---
![](../images/personna.svg) 
Aggregator
^^^
Leverages web architecture to retrieve structured data on the web and generate usable indexes.
---
![](../images/personna.svg) 
User
^^^
The end user of the publishing and aggregation activities.  May leverage 
the web for discovery or tools such as Jupyter for analytics and visualization.  
```

## Persona: Publisher

In OIH the Publisher is the one authoring the JSON-LD documents and publishing them 
to the web.  Details on this persona can be found in the [Publisher](../publishing/publishing.md) section.  Additionally, this persona would be leveraging this encoding described in the [JSON-LD Foundation](../foundation/foundation.md) section and the 
profiles described in the [Thematic Patterns](../thematics/README.md). 

## Persona: Aggregator

In OIH the Aggregator is a person or organization who is indexing resources on the 
web using the structured data on the web patterns described in this documentation.  
Details on the approach used by OIH and potential alternatives can be found in the 
[Aggregator](../indexing/index.md) section.

## Persona: User

The user is the individual or community who wished to leverage the indexes generated
as a result of the publishing and aggregation activities. The user may be using the 
developed knowledge graph or some web interface built on top of the knowledge graph or 
other index.

User tools may be web sites or scientific notebooks.  Some examples of these 
user experiences are described in the [User](../users/referenceclient.md) section.