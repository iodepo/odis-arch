import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md("""# Query Qlever to LPG""")
    return


@app.cell
def _():
    import marimo as mo
    from io import StringIO
    from pathlib import Path
    import polars as pl
    import requests
    import kuzu
    from ipysigma import Sigma
    import networkx as nx
    import igraph as ig
    import holoviews as hv
    from holoviews import opts
    import json

    return (
        Path,
        Sigma,
        StringIO,
        hv,
        ig,
        json,
        kuzu,
        mo,
        nx,
        opts,
        pl,
        requests,
    )


@app.cell
def _(StringIO, pl, requests):
    def query_mode(source,   query):
        params = {
            "timeout": "600s",
            "access-token": "doos_7643543846_6dMISzlPrD7i"
        }
        headers = {
            "Accept": "text/csv",
            "Content-type": "application/sparql-query"
        }

        # Read the SPARQL query from file
        with open(query, "r") as file:
            query = file.read()

        # Send the request
        response = requests.post(source, params=params, headers=headers, data=query)

        # Load response into Polars DataFrame
        df = pl.read_csv(StringIO(response.text))

        return df
    return (query_mode,)


@app.cell
def _(query_mode):
    source = "http://0.0.0.0:7019"
    query = "/home/fils/scratch/qleverflow/queries/keywordsPathSearch.rq"
    df = query_mode(source, query)
    return df, query, source


@app.cell
def _(mo):
    mo.md(
        """
        ## Notes:

        The columsn are: ```start pred end source path edge```

        edges are:  path (int)   source, target
        nodes are:   sounce, target (all the uniques)
        """
    )
    return


@app.cell
def _(df, pl):
    combined_uniques = (
            df
            .select([
                pl.concat_list([pl.col('source'), pl.col('target')])
                .alias('nodes')
            ])
            .select([
                pl.col('nodes').explode().unique().sort()
            ])
        ).drop_nulls()    #   .to_series().to_list()
    return (combined_uniques,)


@app.cell
def _(combined_uniques):
    combined_uniques.head()
    return


@app.cell
def _(df):
    # Make edge list
    edge_df = df.select(['source', 'target']).drop_nulls()
    return (edge_df,)


@app.cell
def _(edge_df):
    edge_df.head()
    return


@app.cell
def _(kuzu):
    db = kuzu.Database()
    conn = kuzu.Connection(db)
    return conn, db


@app.cell
def _(conn):
    conn.execute("DROP TABLE IF EXISTS Relations")
    conn.execute("DROP TABLE IF EXISTS Entity")

    conn.execute("CREATE NODE TABLE Entity(nodes STRING, PRIMARY KEY (nodes))")
    return


@app.cell
def _(conn):
    conn.execute("COPY Entity FROM combined_uniques")
    return


@app.cell
def _(conn):
    conn.execute("CREATE REL TABLE Relations(FROM Entity TO Entity)")
    return


@app.cell
def _(conn):
    conn.execute("COPY Relations FROM edge_df")
    return


@app.cell
def _():
    cq = """MATCH (n1:Entity)-[r]->(n2:Entity)
    RETURN n1, n2, r
    """
    return (cq,)


@app.cell
def _(conn, cq):
    r = conn.execute(cq)
    return (r,)


@app.cell
def _(r):
    G = r.get_as_networkx(directed=False)
    return (G,)


@app.cell
def _(G, nx):
    nx.write_gexf(G, 'my_graph.gexf')
    return


@app.cell
def _():
    # pageranks = nx.pagerank(G)
    return


@app.cell
def _():
    # hv.extension('bokeh')
    # graph = hv.Graph.from_networkx(G, nx.spring_layout)
    # graph.opts(width=400, height=400, node_size=10, edge_line_width=1)
    return


if __name__ == "__main__":
    app.run()
