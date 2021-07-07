# Indexing Quick Start  

![](./images/composeOptions.png)

## Gleaner (app)

Gleaner the app is the Go based program that performs the actual retrieval and loading of JSON-LD documents from the web.  Essentially a basic ELT workflow.   Gleaner is a Go based program that compiles down to a single binary (app).  It can be compiled into releases that can be run on Linux, Mac OS X and Windows.  

While Gleaner is a stand alone app, it is designed to interact with, at a minimum, an object store to support data storage.  These dependencies can be met with the Gleaner Indexing Services compose file.

### Quick Start steps


#### Grab Gleaner and the support files we need

* Gleaner
* Gleaner config template
* JSON-LD context


####  Obtain the compose file(s) you need

This will be the Gleaner Indexing Services (IS) file or the Gleaner Data Services (DS) compose files.   Why pick one over the other?

> Choose Gleaner IS if you simply wish to retrieve the JSON-LD into a data warehouse to use in your own workflows

> Choose Gleaner DS if you wish to build out a graph and want to use the default contains used by Gleaner.  


* Gleaner DS compose file
* Gleaner DS environment setup script

####  Edit environment variables setup script

```bash
#!/bin/bash

# domains 
export GLEANER_ADMIN_DOMAIN=admin.local.dev
export GLEANER_OSS_DOMAIN=oss.local.dev
export GLEANER_GRAPH_DOMAIN=graph.local.dev
export GLEANER_WEB_DOMAIN=web.local.dev
export GLEANER_WEB2_DOMAIN=web2.local.dev

# Object store keys
export MINIO_ACCESS_KEY=worldsbestaccesskey
export MINIO_SECRET_KEY=worldsbestsecretkey

# local data volumes
export GLEANER_BASE=/tmp/gleaner/
export GLEANER_TRAEFIK=${GLEANER_BASE}/config
export GLEANER_OBJECTS=${GLEANER_BASE}/datavol/s3
export GLEANER_GRAPH=${GLEANER_BASE}/datavol/graph
```


#### Spin up the containers

```bash
docker-compose -f gleaner-ds.yml up -d
```


#### Edit Gleaner config file


```yaml
---
minio:
  address: 192.168.86.45
  port: 32773
  accessKey: worldsbestaccesskey      
  secretKey: worldsbestsecretkey  
  ssl: false
  bucket: gleaner
gleaner:
  runid: oih # this will be the bucket the output is placed in...
  summon: true # do we want to visit the web sites and pull down the files
  mill: true
context:
  cache: true
contextmaps:
- prefix: "https://schema.org/"
  file: "./jsonldcontext.json"  # wget http://schema.org/docs/jsonldcontext.jsonld
- prefix: "http://schema.org/"
  file: "./jsonldcontext.json"  # wget http://schema.org/docs/jsonldcontext.jsonld
summoner:
  after: ""      # "21 May 20 10:00 UTC"   
  mode: full  # full || diff:  If diff compare what we have currently in gleaner to sitemap, get only new, delete missing
  threads: 1
  delay: 0  # milliseconds (1000 = 1 second) to delay between calls (will FORCE threads to 1) 
  headless: http://0.0.0.0:9222  # URL for headless see docs/headless
millers:
  graph: true
  shacl: false
sitegraphs:
- name: aquadocs
  url: https://oih.aquadocs.org/aquadocs.json 
  headless: false
  pid: https://www.re3data.org/repository/aquadocs
  properName: AquaDocs
  domain: https://aquadocs.org 
sources:
- name: marinetraining
  url: https://www.marinetraining.eu/sitemap.xml
  headless: false
  pid: https://www.re3data.org/repository/marinetraining
  properName: Marine Training EU
  domain: https://marinetraining.eu/
- name: oceanexperts
  url: https://oceanexpert.org/assets/sitemaps/sitemapTraining.xml
  headless: false
  pid: https://www.re3data.org/repository/oceanexpert
  properName: OceanExpert UNESCO/IOC Project Office for IODE 
  domain: https://oceanexpert.org/
- name: obis
  url: https://obis.org/sitemap/sitemap_datasets.xml
  headless: false
  pid: https://www.re3data.org/repository/obis
  properName: Ocean Biodiversity Information System
  domain: https://obis.org
```
#### Run gleaner


### I want a graph in the end, what do I do?

You have set up the server environment and Gleaner and done your run.  Things look good
but you don't have a graph you can work with yet.    You need to load the JSON-LD into
the triplestore in order to start playing.

  * Simple script loading 
  * Nabu


### Try out a simple SPARQL query.

