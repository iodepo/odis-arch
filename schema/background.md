Background
=====================

[Overview](/background.html?#overview)

[P418](/background.html?#p418)

[Tooling](/background.html?#tooling)

[Next Steps](/background.html?#steps)

------------------------------------------------------------------------

#### Overview

The architecture defines a workflow for objects, a \"digital object
chain\". Here, the digital object (DO) is the data graph such as the
JSON-LD package in a landing page.

The chain is the life cycle connecting; authoring, publishing,
aggregation, indexing and searching/interfaces.

##### Stack

The following image shows a general overview of the architecture.

![](./images/stack.png)

##### Flow

![](./images/flow.png)

1.  Providers are engaged to provide structured data on the web and
    provide robots.txt and sitemap.xml entries to facilitate indexing.
2.  Harvesting will be done using the Gleaner package developed as part
    of NSF\'s EarthCube Project 418/419. Harvesting is simply a further
    leveraging of the web architecture approach and it is expected that
    other harvesters with perhaps community or interface specific goals
    will develop.
3.  The results of the Gleaner harvest (data graphs, reports,
    validations and generated indexes) are stored in an S3 compliant
    object store.
4.  Generated graph is loaded into a triplestore (Blazegraph in this
    case) for query and analysis. Future options include leveraging the
    approach for spatial or other indexes.
5.  From there interfaces can be built such as simple web interfaces,
    GraphQL or other interface options. Spatial, full text or other
    indexes can be built. It\'s also possible to explore connections to
    other research graphs such as the Freya Project or others.
:::

------------------------------------------------------------------------

#### P418


[Science on Schema:](https://github.com/ESIPFed/science-on-schema.org/)
Community guidance on best practices for employing schema.org for
geoscience datasets

[Gleaner](https://gleaner.io/)

New EarthCube Office work: [GeoDex](https://geodex.org/) and [Object
Exchange page
DEMO](https://dx.geodex.org/?o=/iris/107b0c662fa9051d3714b0e93fef981713d2ca48.jsonld)
This demo is driven by web components.

Lessons learned

-   Graphs are generally ugly due to the organic nature of them. Ugly
    graphs are harder to query, parse and display.
-   If we make it easy for publishers in their space -\> becomes hard in
    query space
-   PIDS are important as are explicate IDs in the data graph.
-   Death by http! The http https impedance is becoming, and will
    become, more and more an issue in a federated or distributed model.

[JSON-LD structure and https
testing](https://github.com/fils/JSON-LD_inspection) Worried about
http/https impedance to the digital object cloud for JSON-LD and
schema.org. Doing some exploring.
:::

------------------------------------------------------------------------

#### Tooling

[Gleaner:](https://gleaner.io) (
<https://github.com/earthcubearchitecture-project418/gleaner>) A tool
for harvesting, validating and indexing structured data on the web.

[Fence:](Fence%20https://github.com/earthcubearchitecture-project418/fence)
A testing environment leveraging SHACL, sitemaps and JSON-LD framing
approaches in support of Gleaner development.

[Tangram](https://github.com/earthcubearchitecture-project418/tangram) A
service wrapper around PySHACL to allow web based SHACL validation of
data graphs.

[GROW](https://github.com/fils/goobjectweb) A program that implements
the RDA Digital Object Cloud pattern on top of Amazon S3 API based
object stores. It bridges Gleaner and Mercantile to the web.

![](./images/grow1.png)

![](./images/do.png)

[Mercantile](https://github.com/earthcubearchitecture-project418/mercantile)
A GraphQL server that connects to graph databases. It fronts SPARQL
calls to a data interface defined from the schema.org type Dataset
\"class\" (ref: https://schema.org/Dataset) or other JSON-LD schema.

Other Tools for review:

-   [JSON-LD Playground](https://json-ld.org/playground/) at
    [JSON-LD.org](https://json-ld.org)
-   [SHACL playground](https://shacl.org/playground/)
-   [Google Structured Data testing
    tool](https://search.google.com/structured-data/testing-tool) (going
    away)
-   [Google Dataset for
    developers](https://developers.google.com/search/docs/data-types/dataset)
-   [Press
    article](https://www.schemaapp.com/tools/say-goodbye-to-googles-structured-data-testing-tool-and-hello-to-the-alternatives/)
-   [Rich results](https://search.google.com/test/rich-results)
-   [SchemaApp.com](https://www.schemaapp.com/solutions/structured-data-health-check-diagnostic/)
-   [Linter Structured Data](http://linter.structured-data.org/)
-   [Yandex](https://webmaster.yandex.com/tools/microtest/)
-   [Schema dev](https://test.schema.dev/)
-   [Chrome
    extension](https://chrome.google.com/webstore/detail/ryte-structured-data-help/ndodccbbcdpcmabmiocobdnfiaaimgnk?hl=en)
-   [Google Rich Results](https://search.google.com/test/rich-results)
-   [Datashapes](http://datashapes.org/)


------------------------------------------------------------------------

#### Next Steps {#steps}

-   Focus on schema.org, lay groundwork for connection to other
    vocabularies
-   Focus on the platform (based on web architecture) not any package or
    implementation

[ODIS Arch Fork](https://github.com/fils/odis-arch) [(My
notes)](https://github.com/fils/odis-arch/blob/master/docs/dev/thoughts.md)

+-------------+-------------+-------------+-------------+-------------+
| Authoring   | Publishing  | Harvesting  | Indexing    | Utilization |
+=============+=============+=============+=============+=============+
| JSON-LD (as | Leverage    | [Gleaner    | RDF graph   | Searching   |
| ser         | robots.txt  | ](https://g | from the    | the indexes |
| ialization) | for both    | leaner.io/) | collected   | (           |
|             | crawling    | and others; | JSON-LD     | Mercantile) |
| schema.org  | info and    | [LDSp       | (part of    |             |
| (voc)       | agent       | ider](https | Gleaner     | Data access |
|             | routes      | ://github.c | default     | via the     |
| -   others  |             | om/ldspider | output)     | results     |
|     can be  | Leverage    | /ldspider), |             | (links to   |
|     used    | [sit        | [Squirre    | Full text   | d           |
| -           | emaps](http | l](https:// | index (for  | istribution |
| development | s://www.sit | dice-group. | now via     | nodes)      |
|     of      | emaps.org/) | github.io/s | Lucene in   |             |
|             | with        | quirrel.git | Blaze.      | Notebooks   |
|    guidance | lastmod     | hub.io/over | Perhaps     | to search   |
| -           | date node   | view.html), | later link  | and then    |
|  validation |             | [Nutch      | in Elastic) | access the  |
|             | HTML pages  | (Ap         |             | data or     |
|    (SHACL?) | with        | ache)](http | Spatial     | mine the    |
|             | JSON-LD     | ://nutch.ap | index (and  | metadata    |
| Alignment   | with either | ache.org/), | exchange    | objects at  |
| to other    | static or   | [Laundr     | formats).   | the hub.    |
| best        | dynamic     | omat](https | We have     |             |
| practices   | payload     | ://github.c | workable    | Web         |
| approaches  | injection.  | om/LOD-Laun | pipelines   | components  |
|             | Note        | dromat/LOD- | for this in | to enables  |
| Validation  | DataCite JS | Laundromat) | Gleaner,    | inclusion   |
| (SHACL,     | for dynamic |             | however the | at partner  |
| JSON        | loading of  | Work on     | graphs      | domains.    |
| schema,     | DOI         | notebooks   | typically   |             |
| other?).    | metadata as | and other   | don\'t      |             |
| Validation  | JSON-LD     | tools for   | provide     |             |
| would       |             | testing by  | spatial in  |             |
| address PID | Reviewing   | pa          | a format    |             |
| elements as | plugins or  | rticipants. | easy to     |             |
| well as     | approach    | (           | work with   |             |
| imp         | for         | [Example]   | here. The   |             |
| lementation | platforms   | (https://co | results are |             |
| patterns    | in use:     | lab.researc | spotty.     |             |
| for funding | [Drupal](   | h.google.co |             |             |
| and other   | https://www | m/drive/18R | Connections |             |
| elements    | .drupal.org | VRtgWxNtVoY | to external |             |
|             | /docs/contr | ug09OO4qtWV | graphs.     |             |
| Exploration | ibuted-modu | imVCTuFU?us | Nothing     |             |
| ideas       | les/schemao | p=sharing)) | done on     |             |
| include:    | rg-metatag) |             | this front, |             |
| [Sch        | [CKAN]      |             | but would   |             |
| imatos.org] | (https://ck |             | be great to |             |
| (https://gi | an.org/2018 |             | see.        |             |
| thub.com/sc | /04/30/make |             | Results as  |             |
| himatos/sch | -open-data- |             | nanopubs to |             |
| imatos.org) | discoverabl |             | integrate.  |             |
| there is a  | e-for-searc |             | (Gleaner    |             |
| [demo]      | h-engines/) |             | does basic  |             |
| (http://rsm | ,           |             | nanopub     |             |
| srv01.nci.o | [DSpace](h  |             | prov now)   |             |
| rg.au:8080/ | ttps://jour |             |             |             |
| schimatos/) | nal.code4li |             | Index the   |             |
| [Schem      | b.org/artic |             | data (not   |             |
| arama](http | les/13191), |             | the         |             |
| s://github. | [ERDDAP     |             | metadata)   |             |
| com/google/ | (native     |             | via tika    |             |
| schemarama) | support)](h |             | pipeline.   |             |
|             | ttps://www. |             | Not planned |             |
|             | ncei.noaa.g |             | as part of  |             |
|             | ov/erddap/i |             | this work,  |             |
|             | ndex.html), |             | but was     |             |
|             | [OPeNDAP    |             | done in     |             |
|             | (native     |             | P418, could |             |
|             | sup         |             | be          |             |
|             | port)](http |             | leveraged   |             |
|             | s://www.ope |             | if a group  |             |
|             | ndap.org/). |             | had         |             |
|             |             |             | interest.   |             |
|             |             |             | Likely      |             |
|             |             |             | something   |             |
|             |             |             | to do local |             |
|             |             |             | to a data   |             |
|             |             |             | provider    |             |
|             |             |             | and expose  |             |
|             |             |             | as a        |             |
|             |             |             | generated   |             |
|             |             |             | graph.      |             |
+-------------+-------------+-------------+-------------+-------------+


