# Background
## Overview

The architecture defines a workflow for objects, a \"digital object
chain\". Here, the digital object (DO) is the data graph such as the
JSON-LD package in a landing page.

The chain is the life cycle connecting; authoring, publishing,
aggregation, indexing and searching/interfaces.


### Flow

![](./images/flow.png)

1. Providers are engaged to provide structured data on the web and
    provide robots.txt and sitemap.xml entries to facilitate indexing.
2. Harvesting will be done using the Gleaner package developed as part
    of NSF\'s EarthCube Project 418/419. Harvesting is simply a further
    leveraging of the web architecture approach and it is expected that
    other harvesters with perhaps community or interface specific goals
    will develop.
3. The results of the Gleaner harvest (data graphs, reports,
    validations and generated indexes) are stored in an S3 compliant
    object store.
4. Generated graph is loaded into a triplestore (Blazegraph in this
    case) for query and analysis. Future options include leveraging the
    approach for spatial or other indexes.
5. From there interfaces can be built such as simple web interfaces,
    GraphQL or other interface options. Spatial, full text or other
    indexes can be built. It\'s also possible to explore connections to
    other research graphs such as the Freya Project or others.

------------------------------------------------------------------------
