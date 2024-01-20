# Master Data Product 

## About

This is a quick start for code to generate a "Master Data Product" from a 
provided OIH Release graph.  The graph needs to be in NQuads format and follow
the guidance from the OIH Book in order to express resources that align with the 
queries used.

## Quickstart

> NOTE:  This program can take several minutes to run.  While it does attempt to provide
> feedback on progress, this can be slow also as it can only increment on query completion.
> Also, some of the dataframe transforms can be lengthy too.  

An example command will be like:

> NOTE:  A run for a graph the size of CIOOS takes around 4 to 5 minutes

```Bash
python mdp.py  --source "http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.nq"  --output "./output/cioos.parquet"
```

for s3 something like the following can be used assuming you have set the environment variables
 MINIO_ACCESS_KEY and  MINIO_SECRET_KEY.

```Bash
 python mdp.py  --source "s3://nas.local:49153/public/graphs/test1/africaioc_release.nq"  --output "./output/test.parquet"
```

Can now save to s3 as well:

```Bash
 python mdp.py  --source "s3://nas.local:49153/public/graphs/test1/africaioc_release.nq"  --output "s3://nas.local:54321/public/graphs/products/africaioc.parquet"
```

At present, I only support Parquet and CSV output based on the file extension.  

## mdp2solr.py

```Bash
python mdp2Solr.py --source ./output/cioos.parquet --outputdir ./output/solr
```

## MDP2Solr

```Bash
 python mdp2solr.py  --source "s3://nas.local:49153/public/assets/africaioc.parquet"  --output "./output/solr/
```