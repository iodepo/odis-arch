# Release Graph work

## About

Notebooks and products related to the OIH Release Graphs.  In the end
I would like the notebooks here to be able to output something like
the markdown file at
[Ocean InfoHub Graph (OIH-Graph)](https://github.com/iodepo/odis-arch/tree/schema-dev-df/docs/releases).

As this will be somewhat dynamic in terms of be based on recent crawls
and also have a released version that can exist at Zenodo there are some ideas
about approaches.

We could simply make a github repo and leverage LFS for the larger files
and do Zenodo archives and DOIs via that classic pattern.  We could also
host the files at the OIH S3 server and build out the visuals in HTMl or
PDF via these codes.

It's also possible a hybrid of those would be nice so we can leverage GitHub Actions
and such but also, perhaps, the S3 storage.  I am not sure how large a repo can
get even with LFS and these graphs, especially with RPOV graphs included, get
grow steadily with time.  

Some testing with use NLP for extracting GPEs from these resources
is in [./dataScience](dataScience/README.md).  These are just some more examples
of looking for approaches to leverage and engage the OIH Graph. 

## Assets

The easiest way to find the current assets is to use/view the 
[assetListing notebook](./assetListing.ipynb).  This will call 
the anonymous OIH bucket and provide a listing of the current files.

### Provider Graphs

This section lists the graphs in NQ format for the current OIH partners.  

### OIH Assets

These are some generated assets like those done in the
[OIH_GraphPreProc notebook](./OIH_GraphPreProc.ipynb).  These are 
mostly SPARQL queries done against the provider graph with the results
stored in parquet files.

The _combined.parquet_ file is all the other parquet files combined.

The exception is the _OIHGraph_25032023.parquet_ file, which is the 
collection of all the quads from the provider graph into one parquet 
file.  So this is RDF in parquet.  

The [OIH_DashBoardQuery notebook](./OIH_DashBoardQuery.ipynb) demonstrates
the use of DuckDB to query the combined.parquet file.  Some users may 
find using SQL useful in come cases.

If you wish to use SPARQL, take a look at the previously mentioned
[OIH_GraphPreProc notebook](./OIH_GraphPreProc.ipynb).   This notebook 
loads the release graphs into RDFLib and runs SPARQL queries against them.

So you can observe how that notebook works.

Improvements, issues and PRs are always welcome.


## Notes

Working on a method to publish a pretty release that can be archived at Zenodo 
and also hosted on the web to allow easy access and citation.  


Testing the use of 
things like [Pretty Jupyter](https://pretty-jupyter.readthedocs.io/en/latest/ ) and 
[Jupyter Book](https://jupyterbook.org/en/stable/advanced/html.html) for this.



