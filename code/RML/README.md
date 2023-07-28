# RML Notes

## Notes

The biggest issue with this is that we are really converting the data to RDF
and not generating a RDF metadata record. So it might be a case where they need to 
make a separate file for the metadata of the dataset, or we have them add some 
columns that mostly just repeated values that get us the properties we need
for a metadata record. 

Note the example.ttl has in it a triple that defines the CSV source URL.

```bash
java -jar rmlmapper-6.2.1-r368-all.jar -m example.ttl -o output.json -s jsonld
```

serialization formats can be (nquads (default), trig, trix, jsonld, hdt)

For the Peace Boat example, try

```bash
 java -jar rmlmapper-6.2.1-r368-all.jar -m peaceMap.ttl -s trig
```

Note, I had to add an ID column to get a unique ID.  However, we could compose columns
together too if it provided a unique value.  Otherwise, there might be something 
in RML that addresses this.  I've not read the docs yet.  

This is an example of how to do a nested reference.  Here I used some made up
URIs, but I suspect I can make a blank node reference too.  If we can not use 
blank nodes we can use the genid pattern.


## Scratch
