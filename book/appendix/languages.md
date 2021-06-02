# Languages

## About

JSON-LD fully support the identification of the language types.

Properties such as label, description, keyword etc can be 
extended in the context with a container language attribute notiation.

This will allow the use of standard language codes (fr, es, en, de, etc) to
be used when describing these properties. 


```
{
  "@context": {
    "vocab": "http://example.com/vocab/",
    "label": {
      "@id": "vocab:label",
      "@container": "@language"
    }
  },
  "@id": "http://example.com/queen",
  "label": {
    "en": "The Queen",
    "de": [ "Die Königin", "Ihre Majestät" ]
  }
}
```

In graph space the resulting triples from the above are:

```
<http://example.com/queen> <http://example.com/vocab/label> "Die Königin"@de .
<http://example.com/queen> <http://example.com/vocab/label> "Ihre Majestät"@de .
<http://example.com/queen> <http://example.com/vocab/label> "The Queen"@en .
```

with language encoding attributes in place.  These can be used in 
searching and result filters.

Note, this can cause issues in query space since the concept of 

```
"The Queen"
```

and 
 
 ```
 "The Queen"@en
 ``` 
 
 are different and so care must be taken the creation of the SPARQL 
 queries not to accidentally imposed implicate filters through the use 
 of language types. 
 
