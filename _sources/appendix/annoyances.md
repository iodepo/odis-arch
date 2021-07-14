# Known Issues

## About

This document will collect some of the various issues we have encounter in publishing
the JSON-LD documents.  

### control characters in URL string for sitemap or in the JSON-LD documents

Make sure there are no control characters such as new line, carriage returns, 
tabs or others in the document.  These can be problematic both for processing and
display.  

### context is a map (changed from 1.0)

Be sure to use a context style like:

```
    "@context": {
        "@vocab": "https://schema.org/"
    },
```

The context section must be a map starting in JSON-LD 1.1

### data graphs need @id

Be sure to include an @id in your graph that points to the identifier or the 
web address of the resource providing the metadata.  This is not the material the
metadata is about, but rather the metadata record itself.

### string literals must be valid

The string literals must be sure to not have quotation marks or other invalid
characters without escaping or encoding them.  
