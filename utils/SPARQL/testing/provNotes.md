# Notes

Prov is made with:

```json
urn:gleaner.oih:af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74```

Nabu loads with 

```json
urn:gleaner.oih:edmo:ce91bdb5c10c761d4f3876f0d45e8543d5a6c82f
```


## Prov example
```json
{
		"@context": {
		  "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
		  "prov": "http://www.w3.org/ns/prov#",
		  "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
		},
		"@graph": [
		  {
			"@id": "https://www.re3data.org/repository/seadatanet/edmo",
			"@type": "prov:Organization",
			"rdf:name": "EDMO SeaDataNet",
			"rdfs:seeAlso": "https://edmo.seadatanet.org"
		  },
		  {
			"@id": "https://edmo.seadatanet.org/report/3550",
			"@type": "prov:Entity",
			"prov:wasAttributedTo": {
			  "@id": "https://www.re3data.org/repository/seadatanet/edmo"
			},
			"prov:value": "https://edmo.seadatanet.org/report/3550"
		  },
		  {
			"@id": "https://gleaner.io/id/collection/af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74",
			"@type": "prov:Collection",
			"prov:hadMember": {
			  "@id": "https://edmo.seadatanet.org/report/3550"
			}
		  },
		  {
			"@id": "urn:gleaner.oih:af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74",
			"@type": "prov:Entity",
			"prov:value": "af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74.jsonld"
		  },
		  {
			"@id": "https://gleaner.io/id/run/af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74",
			"@type": "prov:Activity",
			"prov:endedAtTime": {
			  "@value": "2023-06-17",
			  "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
			},
			"prov:generated": {
			  "@id": "urn:gleaner.oih:af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74"
			},
			"prov:used": {
			  "@id": "https://gleaner.io/id/collection/af4e9ac0354eb4bbbf5a12168ce3760cf6a23c74"
			}
		  }
		]
	  }

```