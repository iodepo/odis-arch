# Data Services

The typical functional goal of this work is the development and use of a Graph that can be accessed via a triplestore (Graph Database).  To do that we need a set of additional containers to support this and expose these services on the web through a single domain with https support.  

* Object Store \
An S3 compliant object store supporting S3 APIs including S3Select.  For open source this is best satisfied with the Minio Object Store.  For commercial cloud AWS S3 or hosted Ceph services will work.  
* Graph Database
* Web Router (technically optional)



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

### Object store pattern

Within in the object store the following digital object pattern is used.  
This is based on the work of the RDA Digital Fabric working group.  

```{figure} ./images/do.png
---
name: gleaner-do
---
Gleaner Digital Object Pattern
```





At this point the graph and data warehouse (object store) can be exposed to the net for use by clients such as jupyter notebooks or direct client calls to the S3 object APIs and SPARQL endpoint.

Gleaner Data Services (DS) Environment Variables
The Docker Compose file used to launch the Gleaner DS has a set of configurable elements that can be set and passed to the orchestration system with environment variables.  

These can be set manually or through the command line.  A simple script to set the variables could look like:

-- Environment Var settings script

The actual services can be deployed via a Docker Compose file (also works with Podman).  An example of that file and details about it follow.  

Let's take a look at this.

```{literalinclude} ./docs/setenv.sh
:linenos:
```


-- Break down the compose file here

```{literalinclude} ./docs/gleaner-DS-NoRouter.yml
:linenos:
```



NOTE:  DS also needs the object -> graph sync (via Nabu)
NOTE:  Should also add in (here or to the side) the ELT local Data Lake to Data Warehouse path (ala CSDCO VaultWalker)


![](../publishing/images/do.png)
