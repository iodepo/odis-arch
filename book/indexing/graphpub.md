# Graph First Approach

## About

During the early adopters meetings and in discussion with others an alternative publication pattern came up.  This is the pattern where it is not possible to update the web resources with the metadata content.  This may be due to access or technical issues.  Regardless, what was possible was to generate the metadata in bulk locally and make the resulting document available.

This approach is not ideal since it is a non-standard pattern and makes the data and information more obscure to other users.  However, it is one the OIH architecture can adapt to and is preferable to the option of excluding those partners in this activity.  

As such, we are making some changes to allow for this pattern.  This means documenting the published graph structure based on the existing thematic patterns and some updates in the indexing workflow to obtain and integrate these graphs into the OIH graph.  

 ```{warning}
 Anti-pattern:
 Using the approach here is not in alignment with 
 Google guidance nor with W3C patterns for structured
 data on the web.  
 
 It is documented here for edge cases
 where this is the minimum viable approach.  The hope is it 
 could act as a gateway to a more standards aligned implementation later.
```

## Graph Only

There are cases where it is only possible to generate the graph
based on the metadata.  Access to the HTML pages is either difficult or the process of inserting the 
data into the pages is not supportable.  

For this case the goal is to create a simple graph in JSON-LD.  To do this we need a collection 
approach that is valid for a range of Things.  

For this it is proposed to use ItemList which can be used on a list of type Thing, ie anything 
type in the Schema.org vocabulary.  

This would define a ListItem with item of any type.  Below is an example for a CreativeWork (map)
and a Course.  Once you are in a "item" any of the details from the other thematic type descriptions 
can be used.  


```JSON
{
  "@context": "https://schema.org/",
  "@type": ["ItemList", "CreativeWork"],
  "@id": "https://example.org/id/graph/X",
  "name": "Resource collection for site X",
  "author": "Creator of the list",
  "itemListOrder": "https://schema.org/ItemListUnordered",
  "numberOfItems": 2,
  "itemListElement": [
    {
      "@type": "ListItem",
      "item": {
           "@id": "ID_for_this_metadata_record1",
           "@type": "Map",
            "@id": "https://example.org/id/XYZ",
            "name": "Name or title of the document",
            "description": "Description of the map to aid in searching",
            "url":  "https://www.sample-data-repository.org/creativework/map.pdf"
      }
    },
    {
      "@type": "ListItem",
      "item": {
           "@id": "ID_for_this_metadata_record2",
            "@type": "Course",
            "courseCode": "F300",
            "name": "Physics",
            "provider": {
                "@type": "CollegeOrUniversity",
                "name": "University of Bristol",
                "url": {
                    "@id": "/provider/324/university-of-bristol"
                }
            }
        }
    }
  ]
}
```

In the case of schema:Dataset one might use schema:DataCatlogue for the following approach.  However, 
since OIH is addressing a wide range of types a more generic collection of Things or CreativeWorks 
approach is needed.

## Item Catalogue Page

It's not hard to generate a simple HTMl page based on the structured metadata file.  This doesn't 
alter the content of the graph, just builds an automated HTMl page around it.

## Publishing and referencing

## Testing

Since we are now dealing with a graph that is pulled as a complete entity there are a few thoughts.

1. How do ensure a connection between a record in the list and a resolvable URL?  Do we need
to:
    1. ensure each record has a IRI it is subject of
    2. in the case where IRI is or can be URL, do a validation of at least a 200 on it
2. How do we publish this?
   1. entry in robots.txt (might be able due to reasons above?)
   2. published and provided to OIH
3. Need guidance on format and structure
