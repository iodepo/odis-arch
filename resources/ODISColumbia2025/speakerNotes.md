# Session Notes

This workshop provides a comprehensive introduction to implementing and utilizing structured data for enhanced data discovery and interoperability. 

We will begin by establishing the fundamental principles, exploring the OIDS Book structure and QuickStart, and contrasting this approach with existing data dissemination methods like OAI-PMH. Moving into foundational concepts, we will delve into JSON-LD, emphasizing its role as an effective serialization of the RDF data model, and cover essential elements like context, fields, and keywords using examples from ESIP's Science on Schema.org tutorials. 

Practical authoring techniques will be demonstrated, including validation and editing of JSON-LD documents. Unique identifiers (IDs) will be discussed, highlighting their importance in federated systems and referencing prominent examples like ORCID and ROR. 

We will then cover deployment strategies, showcasing how JSON-LD can be embedded in HTML pages and integrated into existing systems, followed by a demonstration of indexing and searching using tools like Gleaner and Qlever. 

Finally, we will explore the value propositions of this approach, emphasizing its commodity nature, broad applicability, and foundational role in AI and other data-driven workflows, culminating in a question and answer session.


## Section 1 (Principles)

1) Walk through the [OIDS Book](https://book.odis.org/) and discuss its structure
2) Review the [QuickStart](https://book.odis.org/gettingStarted.html)
3) Discuss this approach in terms of the W3C [data on the web best practices](https://www.w3.org/TR/dwbp/) and also contrast with things like OAI-PMH where separate infrastructure is needed.

## Sections 2 (Foundations)

Here we will introduce JSON-LD.  The best source of information on JSON-LD is the official JSON-LD site at [JSON-LD Official Site](https://json-ld.org/).

> note that it is a serialisation of the RDF data model (a graph model)

 Start with context, fields and keywords from ESIP
 
1) https://github.com/ESIPFed/science-on-schema.org/blob/main/tutorials/esip-summer-mtg-2022/01_json-ld-context-type.md
   2) [Schema.org for Developers](https://schema.org/docs/developers.html)
   3) A more complex example of context can be seen in the [spatial example](./docs/section2/spatialIOptions.json)
2) https://github.com/ESIPFed/science-on-schema.org/blob/main/tutorials/esip-summer-mtg-2022/02_basic-fields.md
3) https://github.com/ESIPFed/science-on-schema.org/blob/main/tutorials/esip-summer-mtg-2022/03_keywords.md
   4) https://book.odis.org/thematics/variables/index.html

We can then put [basic1.json](./docs/section2/basic1.json) 
or [odisBookExample.json](./docs/section2/odisBookExample.json) into [JSON Crack](https://jsoncrack.com) and show it.  

> Note that the playground view is a tree view of a graph.  You can view a graph view at: [vizOfDataset.png](images/vizOfDataset.png).



> If people want more, mention the material at https://json-ld.org/learn.html 

## Section 3 (Authoring)

Here will try and demonstrate authoring 
JSON-LD and maybe some basic validation.

We can leverage rust pad.  https://rustpad.io/#IODPOIH

1) Load up an example JSON-LD document from the ODIS book.  Pull the example from: https://book.odis.org/thematics/dataset/index.html or from the [GitHub repo examples.](https://github.com/iodepo/odis-arch/tree/master/resources/ODISColumbia2025/docs/section2)
2) Load it to the shared rust pad https://rustpad.io/#IODPOIH
3) Load it to https://validator.schema.org/
4) Load it to  [JSON-LD Playground](https://json-ld.org/playground/).



Discuss the various elements like time, space and licensing and show editing the JSON-LD with these elements.  Reference the book for these elements.  

Optional:

* Validation with SHACL at https://shacl.org/playground/ 
  * Start with the data graph in [JSON Crack](https://jsoncrack.com/editor) to show the visual overview
* Show framing with [variable frame](./docs/section3/variableMeasuredFrame.json)
* discuss expanding the context with things like GeoSPARQL with examples from [Spatial Geometry](https://book.odis.org/thematics/spatial/index.html).


## Section 4 (IDs)


Discuss the concept of unique IDs.  

Note their use in places like people, bio-diversity, etc. and their 
value in a federated data system.  

Share [this personal example](./docs/section4/pid_application.md) of what a graph looks like with and without PIDs for people. 

Share:
* https://orcid.org/
* https://ror.org/
* https://datacite.org/
* https://oceanexpert.org/ and then https://oceanexpert.org/institution/5852 (as a setup for a later section) 

> Note they can also use domain-specific IDs and even their own IDs.  There are 
> different use cases for all of them.



> Note that this is not a session on PIDs and that such a topic can be a whole
> session in itself.   However, it is a valuable part of a data management approach, especially in a federated system. 

## Section 5 (Deployment)

There are many ways to _deploy_.  You might be using a system like CKAN or others that have it built in.  In that case, deployment is really framework configuration.

[See software table](./docs/section5/software.md)

For example, [this search](https://oceaninfohub.org/results/Dataset?search_text=ocean+temperature&page=0)  returns a top hit from a test we are doing for ERDDAP [demo result](https://osmc.noaa.gov/erddap/tabledap/pmelTaoDySst.html).  

### metadata resources 

Focus first on the deployment of the JSON-LD into the HTML pages and some of the reasons we do this.  

* show an HTML page with JSON-LD in it from the OIH partners [example from OBIS](https://obis.org/dataset/aaacf13e-a138-4b75-ba78-0b5136649365)
* show loading the page URL into [validator.schema.org](https://validator.schema.org/) or the  [direct link](https://validator.schema.org/#url=https%3A%2F%2Fobis.org%2Fdataset%2Faaacf13e-a138-4b75-ba78-0b5136649365)
* show that there are [browser extensions](https://chromewebstore.google.com/search/schema%20) Also note I don't use these, you don't need them.

### sitemaps and site graphs

Resources are expressed using a sitemap ([sitemaps.org](https://sitemaps.org)) and then can be registered in the ODIS Catalogue [IOC Ocean Data and Information System](https://catalogue.odis.org/).  It is also possible to [publish a full graph](https://book.odis.org/indexing/graphpub.html) of holdings if publishing using the web architecture approach is not available. 



Pub test: 
1) put the JSON-LD into a GitHub repo
2) generate a sitemap for them, put the sitemap at the repo

```bash
➜  archetype git:(master) ✗ source .venv/bin/activate
(archetype) ➜  archetype git:(master) ✗ cd bin
(archetype) ➜  bin git:(master) ✗ python github_jsonld_sitemap.py
usage: github_jsonld_sitemap.py [-h] [--token TOKEN] [--output OUTPUT] repo_url directory
github_jsonld_sitemap.py: error: the following arguments are required: repo_url, directory

python github_jsonld_sitemap.py "https://github.com/iodepo/odis-arch"  "/resources/ODISColumbia2025/indexTarget"
```

So the resulting sitemap.xml file is located at:

```bash
https://raw.githubusercontent.com/iodepo/odis-arch/refs/heads/master/resources/ODISColumbia2025/sitemap.xml
```



## Section 6 (Indexing & Use)

Here we will show the indexing of a resource leveraging the 
material in the [Gleaner Archetype](https://github.com/gleanerio/archetype) repo.  

### Environment

For this section, we will demonstrat an indexing process.  This is typically something for someone who wants to be an aggregator.  As such, it is not a procedure a user or even data provider would use.  

For this architecture, the following elements are used

Architecture elements
* docker
* storage and processing tools, these are all open source and cross-platform
  * minio (s3 store) https://min.io/
  * qlever triplestore https://github.com/ad-freiburg/qlever 
  * headless instance (if needed) https://hub.docker.com/r/chromedp/headless-shell 
* gleaner cli from [Gleaner Archetype](https://github.com/gleanerio/archetype) 

Gleaner (to index)

Clone the [Gleaner/Archetype](https://github.com/gleanerio/archetype) repo.  

Start in that directory

```bash
export PATH="$PWD/bin:$PATH"

cliGleaner.sh -a docker -cfg gleanerconfig_columbia.yaml --source demo

mc ls homelab/gleaner/summoned/demo
```


Nabu (to load)
```bash
cliNabu.sh -a docker --cfg nabuconfig.yaml prefix summoned/demo --endpoint demo

 cliNabu.sh  -a docker release --cfg nabuconfig.yaml --prefix summoned/demo
 
 cliNabu.sh -a docker object --cfg nabuconfig.yaml graphs/latest/demo_release.nq --endpoint demo
 ```

we can test this with the SPARQL 

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT * WHERE {
  graph ?g {
  ?sub ?pred ?obj .
  }
} LIMIT 10
```

> We can also show the EDMO indexing as well as GitHub based if there is time.

### Demo sequence for search

1) go to search.oceaninfohub.org and search on "ocean biodiversity"  ([link to the search](https://oceaninfohub.org/results/Dataset?search_text=ocean+biodiversity&page=0))
2) the second result should be from OBIS "Coral Reef Evaluation..."
3) View the page  ([this one in my search](https://obis.org/dataset/aaacf13e-a138-4b75-ba78-0b5136649365))
4) View source and search for __ld+json__, the mimetype for JSON-LD and review the code in page. 
5) Also put the URL into https://validator.schema.org
6) BONUS:  Scroll down and point out their use of Ocean Expert IDs in the markup

Search ([graph search](http://graph.oceaninfohub.org/blazegraph/#query)) and Resource Orgiented Architecture (ROA) based access ([example of S3 based object access](http://oss.oceaninfohub.org/browser/public))

> [Example SPARQL query for use](./docs/section6/simpleSparql.rq)
> 
> [Example visualization from graph](https://github.com/iodepo/odis-arch/tree/master/graphOps/users/graphVisualization)


## Section 7 (Value)

We can review the topics to this point to highlight some 
of the value propositions. 

- **Low friction** web architecture and commodity infrastructure help address scale and sustainability 
- **Standards-based** wide range of [tools and clients](https://github.com/gleanerio/archetype/blob/master/docs/tooling.md) 
- **AI-ready** (e.g., Croissant, CDIF, ODIS, Google Dataset, etc.)


### Resources
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [OIH Search](https://oceaninfohub.org/)
- [Schema.org](https://schema.org)
- [ML Commons](https://mlcommons.org/working-groups/data/croissant/)
- [Go FAIR](https://www.go-fair.org/)
- [CODATA CDIF](https://cdif.codata.org/)


## Question time

