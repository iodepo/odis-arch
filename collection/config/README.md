# Sources 

## About

This file is a simple YAML file defining sources.   The goal will be for this file
to be replaced by queries into the ODISCat source.  

## Generating valid Gleaner configuration files

This directory contains files associated with the production and in progress sources.

To generate a valid Gleaner configuration file the prefix needs to be added.  The 
shell script in this directory does that also does a few clean and checking steps.

## Notes

To convert the YAML to JSON is easy and tools like yq can do this along with piping 
the result into jq for further processing.  If we wanted to parse out a certain item 
we could use

```bash
 cat sources.yaml| yq  'select(objects)|=[.] | map(del(.sources[].logo)) '   
```

The resulting JSON should be ready to connect with the other elements in a config file.
