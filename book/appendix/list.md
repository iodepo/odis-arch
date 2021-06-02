# Defined Terms

## About

During generation of the structured data a provide may wish to 
either use or publish a set of controlled vocabulary terms or 
a similar set.  

Within schema.org this could be done by leveraging the "DefinedTerm" 
amd "DefinedTermSet" types.  

These types allow us both to define a set of terms and 
use a set of terms in describing a thing.

Note that DefinedTerm is an intangible and can connect to most 
types in Schema.org.  So we can use them in places such as:

* CreativeWork -> keyword
* LearningResource -> teaches
* PropertyValue -> valueReference
* LearningResource -> competencyRequired
* CreativeWork -> learningResourceType

## References

* [schema.org/DefinedTerm](https://schema.org/DefinedTerm)
* [schema.org/DefinedTermSet](https://schema.org/DefinedTermSet)

```
[
        {
                "@context": "https://schema.org/"
        },
        {
                "@type": ["DefinedTermSet","Book"],
                "@id": "http://openjurist.org/dictionary/Ballentine",
                "name": "Ballentine's Law Dictionary"
        },
        {
                "@type": "DefinedTerm",
                "@id": "http://openjurist.org/dictionary/Ballentine/term/calendar-year",
                "name": "calendar year",
                "description": "The period from January 1st to December 31st, inclusive, of any year.",
                "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine"
        },
        {
                "@type": "DefinedTerm",
                "@id": "http://openjurist.org/dictionary/Ballentine/term/schema",
                "name": "schema",
                "description": "A representation of a plan or theory in the form of an outline or model.",
                "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine"
        }
]
```
