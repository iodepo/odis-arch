import polars as pl
import xml.etree.ElementTree as ET
import lancedb
from xml.dom import minidom
import pandas as pd
import numpy as np


# TODO look on txt_description
# TODO use chonky chunky?
# TODO feed trhough relik
def relikER(df):

    # TODO explode the txt_description then filter is_not_null

    expl_df = df.explode("txt_description")
    filtered_df = expl_df.filter(expl_df["txt_description"].is_not_null())

    for node in filtered_df.iter_rows(named=True):
        print(node['txt_description'])


    return None

def main():
    source = "sparql_results_grouped_augmented"
    print(f"geom2graphml mode: Processing data from lancedb table {source} to a file")
    dblocation = "../stores/lancedb"
    table_name = source

    # Connect to LanceDB
    db = lancedb.connect(dblocation)
    table = db[table_name]

    # df = table.to_pandas()  # or polars
    lazy = table.to_arrow()
    df = pl.from_arrow(lazy)

    # df = lazy.collect()
    relikER(df)


if __name__ == "__main__":
    main()
