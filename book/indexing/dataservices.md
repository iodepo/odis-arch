# Data Services

The typical functional goal of this work is the development and use of a Graph that can be accessed via a triplestore (Graph Database).  To do that we need a set of additional containers to support this and expose these services on the web through a single domain with https support.  

* Object Store \
An S3 compliant object store supporting S3 APIs including S3Select.  For open source this is best satisfied with the Minio Object Store.  For commercial cloud AWS S3 or hosted Ceph services will work.  
* Graph Database
* Web Router (technically optional)

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
