# Aggregator

## Intoduction


This section introduces the the OIH approach to indexing. At this stage OIH is 
using the [Gleaner](https://github.com/earthcubearchitecture-project418/gleaner) software to do the indexing and leverages the Gleaner IO 
[gleaner-compose](https://github.com/gleanerio/gleaner-compose) Docker 
compose files for the server side architecture. The gleaner-compose repository holds Docker compose files that can set up three environments
that Gleaner can leverage.

Gleaner the app is a Go based single file binary  
with a required configuration file.  However, it expects at a minimum an object store and 
and optional headless chrome server (for dyanmic/reactive site indexing).  

The figure below gives a quick overview of the various compose options for setting up 
the supporting architecture for Gleaner. 


```{figure} ./images/composeOptions.png
---
name: Compose Options for Gleaner
---
The various compose options for Gleaner
```

Note, the Gleaner ecosystem is not a requirement.  OIH follows the structured data on the web and data on the web best practices patterns.  Being web architecture based, there are many open source tools and scripting solutions you might use.  You may wish to explore the [Alternative Approaches](alternatives.md) section for more on this.


What follows is a bit more detail on the setup used by Gleaner.  Experienced users will 
see where they can swap out elements for their own preference.  Like a different 
triplestore, or wish to leverage a commercial object store?  Simply modify the architecture
to do so.  

## Gleaner

As mentioned Gleaner is simply an app.  It can be run on Linux, Mac OS X or Windows.  It does
not need to be run on the same machine as the supporting services.  You can download and 
compile the code from the previously mentioned github repository or 
the [releases page](https://github.com/earthcubearchitecture-project418/gleaner/releases). 

A single configuration file provides the settings Gleaner needs.  Additionally, a local 
copy of the current schema.org context file should be downloaded locally.  This file is needed
for many operations and access it over the net is slow and often rate limited depending on the 
source.   You can download the file at the [Schema.org for Developers](https://schema.org/docs/developers.html) page.  


## Gleaner Indexing Services (IS)

IS represent the minimum required services to support Gleaner.  With IS you have an object
store in the form of [Minio](https://min.io/) and a headless chrome server in the form of 
[chromedp/headless-shell](https://hub.docker.com/r/chromedp/headless-shell).  

As shown in the figure below, and support the basic harvesting of resources with Gleaner
and loading the JSON-LD objects into Minio.

It does not result in these objects ending up in a graph / triplestore.   You would use
this option if you intend to work on the JSON-LD objects yourself.  Perhaps loading 
them into a alternative graphdb like Janus or working on them with python tooling. 


```{figure} ./images/gleaner1.png
---
name: gleaner-IS
---
Basic Gleaner Indexing Service Activity Workflow
```

## Gleaner Data Services (DS)

If you wish to work with a triplestore and wish to use the default app used by OIH
you can use the compose file that sets up the Gleaner Data Services environment.  

This adds the Blazegraph triplestore to the configuration along with the object store. 

The details of the OIH data services are found in the
 [Data Services](dataservices.md) section.

```{figure} ./images/gleaner2.png
---
name: gleaner-DS
---
Gleaner Data Service Activity Workflow
```

Typically, a user would wish to run the full Gleaner DS stack which supports
both the indexing process and the serving of the resulting data warehouse and graph 
database capacity.  

Combined, these would then look like the following where the indexing and
data services shared a common object store.  

```{figure} ./images/gleaner3.png
---
name: gleaner-ISDS
---
Gleaner Indexing and Data Service Combined
```

This setup show in the above figure is the typical setup for Gleaner and is 
detailed in the [Quick Start](./qstart.md) section.


### Object store pattern

Within in the object store the following digital object pattern is used.  
This is based on the work of the RDA Digital Fabric working group.  

```{figure} ./images/do.png
---
name: gleaner-do
---
Gleaner Digital Object Pattern
```


## Gleaner Web UI (WUI)

The user of the index may take several forms.  A user may be a software developer creating a web based 
interface to the generated index.  It may also be an end user accessing the index (indexes) through notebooks
or special clients.  

Those wishing to run a web site can augemnt the compose files to run their 
preferred web server, object server (to serve files from the object store) or 
software such as node or others to support their deployment pattern.  



```{figure} ./images/gleaner4.png
---
name: gleaner-WUI
---
Gleaner Optional Web UI
```

