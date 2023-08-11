# Personas

## About 

During the design process of the Ocean InfoHub (OIH), many of the design approached leverage three
personas that help define the various archtypes of people who engage with OIH.  It should not be assumed
these scope all the potential persona or that a person or organization scope only one.  It is quite possible
to many.   These are simply design approaches representing potential models or characters.   They 
are tools used in the design process of OIH.

````{grid}

```{grid-item}
![](../images/personna.svg) 

Publisher: A key persona whose activities are covered in detail in [Publishing patterns for OIH](../publishing/publishing.md)
```

```{grid-item}
![](../images/personna.svg) 

Aggregator: Leverages web architecture to retrieve structured data on the web and generate usable indexes.
```

```{grid-item}
![](../images/personna.svg) 

User: The end user of the publishing and aggregation activities.  May leverage
the web for discovery or tools such as Jupyter for analytics and visualization.  
```

````


## Persona: Publisher

In OIH the Publisher is engaged authoring the JSON-LD documents and publishing them 
to the web.  This persona is focused on describing and presenting structured data on the web
to aid in the discovery and use the resources they manage. 
 Details on this persona can be found in the [Publisher](../publishing/publishing.md) section.  
Additionally, this persona would be leveraging this encoding described in the [JSON-LD Foundation](../foundation/foundation.md) section and the 
profiles described in the [Thematic Patterns](../thematics/index.md).

## Persona: Aggregator

In OIH the Aggregator is a person or organization who is indexing resources on the 
web using the structured data on the web patterns described in this documentation.  
Their goal is to efficiently and efficiently index the resources exposed by the Publisher 
persona and generate usable indexes.  Further, they would work to exposed these indexes in 
a manner that is usable by the User persona.
Details on the approach used by OIH and potential alternatives can be found in the 
[Aggregator](../indexing/index.md) section.

## Persona: User

The user is the individual or community who wished to leverage the indexes generated
as a result of the publishing and aggregation activities. The user may be using the 
developed knowledge graph or some web interface built on top of the knowledge graph or 
other index.  They may also use query languages like SPARQL or other APIs or even 
directly work with the underlying data warehouse of collected data graphs.  

User tools may be web sites or scientific notebooks.  Some examples of these 
user experiences are described in the [User](../users/index.md) section.
