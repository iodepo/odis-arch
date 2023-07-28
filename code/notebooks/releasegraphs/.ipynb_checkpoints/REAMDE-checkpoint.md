# Release Graph work

## About

Notebooks and products related to the OIH Release Graphs.


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



