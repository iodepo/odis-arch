# Interfaces

## About

In the end the goal is to provide use of the generated index.  There are several
possible used for an index.

* Web UI such as the reference client at [oceans.collaborium.io](https://oceans.collaborium.io)
  * A variation on this is the development of web components that can be easily included in 
    domain sites to perform operations on the OIH index
* graph access via SPARQL
* access to the graph and objects via workflows like Jupyter notebooks
  
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

