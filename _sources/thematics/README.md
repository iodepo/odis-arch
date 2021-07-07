# Thematic Patterns

## About

Documentation on implementing schema.org for the Ocean Info Hub (OIH) to facilitate the indexing and discovery
of resources.  The approach leverages schema.org which is a community effort and widely
implemented.

## Thematic Profiles

These profiles represent reference implementation of schema.org Types related to the identified ODIS thematic areas.  
They provide a set of minimal elements and notes on more detailed elements.  

These are not final and will evolve with community input.  As this process moves forward we will implement
versioning the profiles to provide stable implementations providers can reliably leverage in their workflows.

1. [Experts and Institutions](./expinst/README.md)
2. [Documents](./docs/README.md)
3. [Projects](./projects/README.md)
4. [Training](./training/README.md)
5. [Vessels](./vessels/README.md)

In support of these five thematic types two additional types were also documented. 

1. [Spatial](./spatial/README.md)
2. [Services](./services/README.md)
3. [Term Lists](./list.md)
4. [Languages](./languages.md)
5. [Prov](./prov/README.md)

```{seealso}
For OIH the focus is on generic documents which can scope reports, data and other resources.
In those cases where the resources being described are of type Dataset you may wish to review
patterns developed for GeoScience Datasets by the ESIP
[Science on Schema](https://github.com/ESIPFed/science-on-schema.org/) community.

```

```{seealso}
For OIH the focus is on generic documents which can scope reports, data and other resources.
In those cases where the resources being described are life sciences resources such as datasets, software, and training materials. we recommend following 
patterns developed by [Bioschemas](https://bioschemas.org/). 

```

## Connections
This document provides an overview of potential connections between the 
various thematic types in OIH.  These are not _all_ the relations but simply 
some to demonstrate the concept as well as give some guidance on the 
connection of value in query results.

![relations](./images/relations.svg)
