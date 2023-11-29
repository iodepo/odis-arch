# Indexing with Gleaner 

![compose options](./images/composeOptions.png)

## Gleaner (app)

The Gleaner applications performs the retrieval and loading of JSON-LD documents 
from the web following structured data on the web patterns.  Gleaner is available for Linux, Mac OS X and Windows.  

While Gleaner is a stand alone app, it needs to interact with
an object store to support data storage and other operations.  These dependencies are met within the 
Gleaner Indexing Services or Data Service Docker compose files.

```{warning}
This documentation is in development.  The primary testing environments are Linux and other UNIX based platforms
such as Mac OS X.   If you are on Windows, there may be some issues.  If you can use a Linux subsystem on Windows, 
you may experience better results.  We will test with Windows eventually and update documentation as needed. 
```

### Quick Start steps

This quick start guide is focused on setting up and testing Gleaner in a local environnement.  It is similar to
how you might run Gleaner in a production environment but lacks the routing and other features likely desired for 
such a situation.


```{note}
This documentation assumes a basic understanding of Docker and experience with basic Docker activities like
starting and stopping containers.  It also assumes an understanding of using a command line interface and 
editing configuration files in the YAML format. 
```

```{admonition} Command
:class: tip
From this point down, the documentation will attempt to put all commands
you should issue in this admonition style box. 
```

In the end, this is the table of applications and config files you will need.  In this guide we will go through 
downloading, setting them up and running Gleaner to index documents from the web.  

```{list-table} Required Applications and Their Config Files
:header-rows: 1

* - Gleaner
  - Docker
  - Minio Client
* - config.yaml
  - ```setenv.sh ``` 
  - ```load2blaze.sh``` 
* - schemaorg-current-https.jsonld
  - gleaner-DS-NoRouter.yml
  - 
```

#### Grab Gleaner and the support files we need

We will need to get the Gleaner binary for your platform and also the Gleaner configuration file 
template.  To do this, visit the [Gleaner Releases page ](https://github.com/earthcubearchitecture-project418/gleaner/releases) 
and pick the release _Ocean InfoHubdev rc1_.  Under the _Assets_ drop down you should see the files we need.  Get:

* Gleaner for your platform
* Gleaner config template: template_v2.0.yaml
* Gleaner indexing service compose file: gleaner-IS.yml
* Helper environment setup script: setenvIS.sh

For this demonstration, we will be running on linux, so this would look something like:

:::{admonition} Command
:class: tip
```bash
curl -L -O https://github.com/earthcubearchitecture-project418/gleaner/releases/download/2.0.25/gleaner
curl -L -O https://github.com/earthcubearchitecture-project418/gleaner/releases/download/2.0.25/gleaner-IS.yml
curl -L -O https://github.com/earthcubearchitecture-project418/gleaner/releases/download/2.0.25/setenvIS.sh
curl -L -O https://github.com/earthcubearchitecture-project418/gleaner/releases/download/2.0.25/template_v2.0.yaml
```
:::

```{note}
You can download these with any tool you wish or through the browser.  Above we downloaded used the command
line curl tool.  For GitHub, be sure to add the -L to inform curl to follow redirects to the object to download.
```

:::{admonition} Command
:class: tip

You may need to change the permission on your gleaner file to ensure it can be run.   On Linux this would 
look something like the following.  

```bash
chmod 755 gleaner
```
:::


We then need to visit [Schema.org for Developers](https://schema.org/docs/developers.html) to pull down the 
appropriate JSON-LD context.  For this work we will want to pull down the _schemaorg-current-https_ in JSON-LD format.  
It also should work to do something similar to the following:

:::{admonition} Command
:class: tip
```bash
curl -O https://schema.org/version/latest/schemaorg-current-https.jsonld
```
:::

#### About the compose file(s)

The above steps have collected the resources for the indexer.   We now want to set up the services that
Gleaner will use to perform the indexing.  To do that we use Docker or an appropriate run time alternative like
Podman or others.   For this example, we will assume you are using the Docker client. 

As noted, a basic understanding of Docker and the ability to issue Docker cli commands to start and stop
containers is required. If you are new do Docker, we recommend you visit and read: 
[Get Started with Docker](https://www.docker.com/get-started).

We need to select the type of services we wish to run.  The various versions of these Docker compose
file can be found in the [Gleaner-compose deployment directory](https://github.com/gleanerio/gleaner-compose/tree/master/deployment).

Why pick one over the other?

> Choose Gleaner IS if you simply wish to retrieve the JSON-LD into a data warehouse to use in your own workflows


> Choose Gleaner DS if you wish to build out a graph and want to use the default contains used by Gleaner.  


```{note}
We wont look at this file in detail here since there will hopefully be no
required edits.  You can see the file in detail in the Index Services
section.
```  


#### Edit environment variables setup script

We have Docker and the appropriate compose file.  The compose files require a set of environment variables
to be populated to provide the local hosts information needed to run.  You can set these yourself or
use or reference the setenv.sh file in the Gleaner-compose repository in the  
[Gleaner-compose deployment directory](https://github.com/gleanerio/gleaner-compose/tree/master/deployment).
You may also need to visit information about permissions at
[Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) if you are
having permission issues.

Let's take a look at the script.

```{literalinclude} ./docs/setenvIS.sh
:linenos:
```

You may wish to edit file to work better with your environment.  By default it will attempt to
use localhost to resolve with and host local runtime data in a /tmp/gleaner directory.  

#### Spin up the containers

Load our environment variables to the shell:

:::{admonition} Command
:class: tip
```bash
source setenv.sh
```
:::

Then start the containers:

:::{admonition} Command
:class: tip
```bash
docker-compose -f gleaner-IS.yml up -d
```
:::

If all has gone well, you should be able to see your running containers with 

:::{admonition} Command
:class: tip
```bash
docker ps
```
:::

and see results similar to:

```bash
CONTAINER ID        IMAGE                            COMMAND                  CREATED             STATUS              PORTS                    NAMES
c4b7097f5e06        nawer/blazegraph                 "docker-entrypoint.s…"   8 seconds ago       Up 7 seconds        0.0.0.0:9999->9999/tcp   test_triplestore_1
ca08c24963a0        minio/minio:latest               "/usr/bin/docker-ent…"   8 seconds ago       Up 7 seconds        0.0.0.0:9000->9000/tcp   test_s3system_1
24274eba0d34        chromedp/headless-shell:latest   "/headless-shell/hea…"   8 seconds ago       Up 7 seconds        0.0.0.0:9222->9222/tcp   test_headless_1
```

#### Edit Gleaner config file

We have all the files we need and we have our support services running.  The next and
final step is to edit our Gleaner configuration file.  This will let Gleaner know
the location of the support services, the JSON-LD context file and the locations
of the resources we wish to index.  

Let's take a look at the full configuration file first and then break down each section.  

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
```


##### Object store

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 2-8
```

The minio section defines the IP and port of the object store.  For this case, we are 
using minio and these are the IP and port from our docker compose steps above.  Note,
if you were to use Ceph or AWS S3, this section is still labeled minio.  You simply
need to update the property values.

##### Gleaner

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 9-12
```

This passes a few high level concpets.

* runid:
* summon
* mill

##### Context sections

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 13-19
```

Comments for the context sections

##### Summoner section

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 20-25
```

Comments for the summoner sections

##### Millers section

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 26-28
```

Comments for the miller sections


##### Site graphs section

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 29-35
```

Comments for the sitegrpah sections


##### Sources section

```{literalinclude} ./docs/gleaner-cfg.yml
:linenos:
:lines: 36-66
```

Comments for the sources sections


#### Run gleaner

For this example we are going to run Gleaner directly.  In a deployed instance you may 
run Gleaner via a script or cron style service.  We will document that elsewhere.

We can do a quick test of the setup.

:::{admonition} Command
:class: tip
```bash
 ./gleaner -cfg template_v2.0 -setup
```
:::


For now, we are ready to run Gleaner.  Try:

:::{admonition} Command
:class: tip
```bash
 ./gleaner -cfg template_v2.0
```
:::


```{note}
Leave the suffix like .yaml off the name of the config file.  The config system can also read
json and other formats.  So simply leave the suffix off and let the config code inspect the 
contents. 
```

### Load results to a graph and test

You have set up the server environment and Gleaner and done your run.  Things look good
but you don't have a graph you can work with yet.    You need to load the JSON-LD into
the triplestore in order to start playing.

#### Minio Object store

To view the object store you could use your browser and point it on the default minio 
port at 9000.  This typically something like localhost:9000.  

If you wish to continue to use the command line you can use the Minio client at
[Minio Client Quickstart guide](https://docs.min.io/docs/minio-client-quickstart-guide.html).

Once you have it installed and working, you can write an entry for our object store with:

:::{admonition} Command
:class: tip
```bash
 ./mc alias set minio http://0.0.0.0:9000 worldsbestaccesskey worldsbestsecretkey
```
:::

#### Load Triplestore

We now want to load these objects, which are JSON-LD files holding RDF based graph
data, into a graph database.  We use the term, triplestore, to define a graph database
designed to work with the RDF data model and provide SPARQL query support over that
graph data.  

* Simple script loading
* Nabu
* Try out a simple SPARQL query

## References

The following are some reference which may provide more information on the various
technologies used in this approach.

* [Google: Understanding how structured data works](https://developers.google.com/search/docs/advanced/structured-data/intro-structured-data)
* [Google Dataset Search By the Numbers](https://arxiv.org/abs/2006.06894) 
* [Google Dataset Search: Building a search engine for datasets in an open Web ecosystem](https://research.google/pubs/pub47845/)
* [W3C SPARQL](https://www.w3.org/TR/sparql11-query/)
* [SHACL](https://www.w3.org/TR/shacl/)
* [Triplestores](https://en.wikipedia.org/wiki/Triplestore)