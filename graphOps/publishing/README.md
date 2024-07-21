# Publishing

## ToDo

- [ ] Add in HuggingFace as another publishing destination

## About

The code here will be used to generate and publish the release graphs.
We will use the sandbox environment available at http://sandbox.zenodo.org.

Note that the sandbox environment can be cleaned at anytime. Also, the 
sandbox environment will issue test DOIs using the 10.5072 prefix 
instead of Zenodo’s normal prefix (10.5281).

## Card

It would be good to generate a metadata card for each release.
This will likely be done using schema.org or the descriptive information, 
however it would be good to look over VoID (https://www.w3.org/TR/void/)
to see if there are some good properties in there to use.


## Resources

* [Zenodo JSON formatter](https://jsonformatter.curiousconcept.com/)
* [Reference structure](https://developers.zenodo.org/#representation)



## Elements 

The following elements are from the Zenodo metadata schema.  We need
to see how these elements map into the OIH sources metadata.

```json
	"contributors":[
		{
			"affiliation":      "",
			"name":             "",
			"orcid":            "optional",
			"type":				"WorkPackageLeader"
		}
	],
	"creators":[
		{
			"affiliation":      "",
			"name":             "",
			"orcid":            "optional"
		}
	],
	"related_identifiers":[
		{
			"identifier":         "",
			"relation":			  "isPublishedIn",
			"scheme":			  "urn",
			"resource_type":      ""
		}
	]
```