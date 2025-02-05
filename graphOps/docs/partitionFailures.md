# Issues

# ------------------------------- Likely our side -------------------------------

## Aquadocs

Indexing OK, error in the stats section?

* Index:  working
* Release:  working

Error seems only to be in the summary building (memory?)

```text
partition: aquadocs
Indexing fine
UnboundLocalError: local variable 'service' referenced before assignment
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0
```

## OBPS


* Index:  working
* Release:  working

Check sitemap/sitegraph validation code

```text
partition: obps
(sitegraph)  Got 1 record
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0
```

## Eurocean


* Index:  working
* Release:  working

Stat building error most likely

```text
partition: euroceanvessels
KeyError: 'Source'

partition: euroceanprojects
KeyError: 'Source'
```

## ODIS hosted: MASPAWIO, Caribbean Marine Atlas Benguel ACC

these 404

```test
partition: maspawio
ValueError: https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-maspawio/maspawio-simple-graph.json

partition: caribbeanmarineatlas
ValueError: https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-caribbeanmarineatlas/caribbeanmarineatlas-simple-graph.json

partition: benguelacc
ValueError: https://raw.githubusercontent.com/iodepo/odis-arch/master/collection/tempHosting/data-benguelacc/benguelacc-simple-graph.json
```

# ------------------------------- Likely their side -------------------------------

## UNEP

Headless rendering issue.  Script is appended at the end outside the body and html.

This may not be valid, checking

```text
partition: unep
KeyError: 'Source'
```

## R2R

404 on run, but seems fine now

Sitemap file is one 5 MB single line.

Might be an XML parsing issue.

```text
partition: r2r
urllib.error.HTTPError: HTTP Error 404: Bad URL source: r2r bad url: https://service.rvdata.us/api/sitemap/
```


## Ocean Expert


* Index:  working
* Release:  working

nbsp in URI?

```text
partition: oceanexpert
Indexing fine
rdflib.exceptions.ParserError: Invalid line (Failed to eat <([^:]+:[^\s"<>]*)> at <http://orcid.org/0000-0002-4645-1662 > <urn:gleaner.io:oih:oceanexpert:data:95286c6898657b8b3ddb115f5f1efe4dac02211f> .):
'<https://oceanexpert.org/expert/19355> <https://schema.org/identifier> <http://orcid.org/0000-0002-4645-1662\xa0> <urn:gleaner.io:oih:oceanexpert:data:95286c6898657b8b3ddb115f5f1efe4dac02211f> .'
```


## INVEMAR

All these seem to be just not responding

```text
partition: invemarvessels
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

partition: invemartraining
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

partition: invemarinstitutions
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

partition: invemargeo
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

partition: invemarexperts
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

partition: invemardocuments
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 0

```

## GBIF


* Index:  working
* Release:  working

space in URI

```text
partition: gbif
rdflib.exceptions.ParserError: Invalid line (Failed to eat <([^:]+:[^\s"<>]*)> at <https://orcid.org/0000-0001-7940-4398 > <urn:gleaner.io:oih:gbif:data:642f4135e6e33e3471f0deb1c153fc55fae76711> .):
'<https://gleaner.io/xid/genid/csk3gigp0jgs73fmp5vg> <https://schema.org/identifier> <https://orcid.org/0000-0001-7940-4398\u202f> <urn:gleaner.io:oih:gbif:data:642f4135e6e33e3471f0deb1c153fc55fae76711> .'

rdflib.exceptions.ParserError: Failed to eat <([^:]+:[^\s"<>]*)> at <https://orcid.org/0000-0001-7940-4398 > <urn:gleaner.io:oih:gbif:data:642f4135e6e33e3471f0deb1c153fc55fae76711> .
```

