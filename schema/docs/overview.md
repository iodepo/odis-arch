# Connection Overview

## About

This document provides an overview of potential connections between the 
various thematic types in OIH.  These are not _all_ the relations but simply 
some to demonstrate the concept as well as give some guidance on the 
connection of value in query results.

![](./images/overviewv2.svg)


## Points of Interest

The arrows express in dot follow.  We will attempt to detail them 
in text and with references or examples below this.

```
// Express all creative works express spatial
  CreativeWork -> Place [lhead=clusterSpatial ltail=clusterDoc]
  // Map -> Place [lhead=clusterSpatial]
  // Dataset -> Place [lhead=clusterSpatial]

  Dataset -> Service   [ltail=clusterDoc];
  Project -> Person  
  Service -> Organization

// Express all creative works express connection to people or organizations
  CreativeWork -> Person [ltail=clusterDoc lhead=clusterOrg  dir="both"];

  // Person, Organization, Project -> CreativeWork
  // Person, Organization, Project -> Service

  Vessel -> Organization [label="additionProperty"]
  Person -> Organization
  Course -> Organization [label="author, creator, funder, maintainer"]
  ```


### Documents to Spatial

