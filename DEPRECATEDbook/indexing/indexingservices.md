# Indexing Services

Gleaner can not run alone and relies on a couple of Open Container Initiative (OCI) containers to support it.  For this document, we will assume you are using Docker but this will work with Podman or other OCI compliant orchestration environments.   These Gleaner Indexing Services are necessary to use Gleaner.   The exception to this would be if you are using a 3rd party objects store like AWS S3 or Wasabi.

* Object Store \
   An S3 compliant object store supporting S3 APIs including S3Select.  For open source this is best satisfied with the Minio Object Store.  For commercial cloud AWS S3 or hosted Ceph services will work.  
* Headless Chrome (technically optional) \
  This is only needed where you expect the sources you index to use Javascript to include the JSON-LD in the pages.  If you know your sources do not use this publishing pattern and rather include the JSON-LD in the static page, then you don't need this container running.  


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



Gleaner Indexing Services (IS) Environment Variables
The Docker Compose file used to launch the Gleaner IS has a set of configurable elements that can be set and passed to the orchestration system with environment variables.  

These can be set manually or through the command line.  A simple script to set the variables could look like:

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

The actual services can be deployed via a Docker Compose file (also works with Podman).  An example of that file and details about it follow.  

-- Break down the compose files here  link to them