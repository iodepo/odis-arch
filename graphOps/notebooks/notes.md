# Notes

## TODO

* need one notebook that pulls and builds release_builder.ipynb
    * Query results to CSV and Parquet where the query is documented
    * Full RDF graph as .nq.gz and Parquet and maybe HDT?
    * generate a Huggingface JOSNL dataset from the descriptions

* WMO notebook   extraction_WMO.ipynb
* OIH Dashboard notebook   extraxtion_OIHDashboard.ipynb
* Spatial coverage notebook, including S2  extraction_spatial.ipynb
* Solr indexing set for OIH SOLR schema extraction_solr.ipynb

```
data = [
    {
        'id': f'{uid}-{i}',
        'text': chunk,
        'source': url
    } for i, chunk in enumerate(chunks)
]
len(data)
```

