# Shell code for exploring sitemaps

## Intro

The following command line approaches can be used for simple initial exploration.

Need to try this with:  https://infohub.eurocean.net/sitemap/projects

## Command Line Tooling

We can start exploring the indexing of data on the command line.  Here we will use the curl command which should 
be installed on all Mac OS X and Linux systems and should be found on the Linux Subsystem for Windows. 

This will give us a low level feel for what is going on.  

We will start by exploring a sitemap.  

```bash
curl -s https://samples.earth/sitemap0.xml
```

We can parse out the URLs from the sitemap with the use of the UNIX grep command

```bash
curl -s https://samples.earth/sitemap0.xml |   grep -oP '<loc>\K[^<]*'
```

In do this we see that out sitemap is really just a feed of URLs.  The sitemap provides us with the ability to add 
some extra information for our URLs.  It also providers a machine readable XML format we can work with.  There are many
libraries for working with XML and several for working with the sitemap data model in XML as well. 

Now lets pull down the URL resource and parse out the JSON-LD we find in the ```<script>``` tag of type application/ld+json.

Note, it is possible that there are many of these tags and also that this tag might be placed in by Javascript which means 
we would not see it here.  We will talk more about this as we explore.  For now we will just look for the first one and 
a static example, which we know this to be.  

```bash
curl -s  --header "Accept: text/html"   https://samples.earth/id/documents/c1pnht3h2h44frv6igfg | sed -n '/<script type=\"application\/ld+json\">/,/<\/script>/p'
```

Let's get rid of the ```<script> ``` tags and then parse the JSON-LD. 

```bash
curl -s  --header "Accept: text/html"   https://samples.earth/id/documents/c1pnht3h2h44frv6igfg | sed -n '/<script type=\"application\/ld+json\">/,/<\/script>/p' | sed 's/<\/script>//' | sed 's/<script type=\"application\/ld+json\">//'
```

TODO WORK ON THIS
At this point we could copy this JOSN-LD and visit something like the JSON-LD playground.   We could also 
visit the Structure Data Linter.   We can then play a bit with the JSON-LD there.


Now, lets pass this through another app.  This is the jsonld.js app.  A Javascript app and library that can be found
on GitHub at [digitalbazaar/jsonld.js](https://github.com/digitalbazaar/jsonld.js).   There are many similar libraries,
so you can feel free to try out others.  


```bash
curl -s  --header "Accept: text/html"   https://samples.earth/id/documents/c1pnht3h2h44frv6igfg | sed -n '/<script type=\"application\/ld+json\">/,/<\/script>/p' | sed 's/<\/script>//' | sed 's/<script type=\"application\/ld+json\">//' | jsonld format -q
```

If all goes well we should see the following output.

```
<https://samples.earth/id/documents/c1pnht3h2h44frv6igfg> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://schema.org/Dataset> .
<https://samples.earth/id/documents/c1pnht3h2h44frv6igfg> <https://schema.org/description> "of data assignments." .
<https://samples.earth/id/documents/c1pnht3h2h44frv6igfg> <https://schema.org/distribution> _:b0 .
<https://samples.earth/id/documents/c1pnht3h2h44frv6igfg> <https://schema.org/maintainer> <https://samples.earth> .
<https://samples.earth/id/documents/c1pnht3h2h44frv6igfg> <https://schema.org/name> "Fake: technical and" .
<https://samples.earth> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://schema.org/Organization> .
<https://samples.earth> <https://schema.org/description> "DEMO SITE:  fake data for testing" .
_:b0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://schema.org/DataDownload> .
_:b0 <https://schema.org/contentUrl> "https://samples.earth/id/documents/c1pnht3h2h44frv6igfg.tsv" .
_:b0 <https://schema.org/encodingFormat> "text/tab-separated-values" .
```

So, this was just a simple set of command line calls to give us a feel for the process.  We have seen a sitemap, the URLs 
that make it up and pulled back those URLs and parsed the JSON-LD.  We then wen ahead and converted the JSON-LD into another
RDF representation (triples) that make loading into a graph database easier.

We could easily take these commands and roll them in a simple bash script.  This might not be a production level approach, 
but it's a good exercise and a good way to get started.  We will explore more advanced ways of doing this later.