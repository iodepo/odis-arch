import polars as pl
import xml.etree.ElementTree as ET
import lancedb
from xml.dom import minidom
import pandas as pd
import numpy as np

# Example Usage
def main():    # Example DataFrame with a list column
    dfnode = pl.DataFrame({
        'id': [1, 2, 3],
        'name': ['A', 'B', 'C'],
        'list_column': [[1, 2], [2, 3, 4], [1, 4]]
    })

    # Get unique values
    unique_values = dfnode['list_column'].explode().unique()
    print(unique_values)  # [1, 2, 3, 4]
    unique_set = set(unique_values)
    print(unique_set)  # {1, 2, 3, 4}

    print("-*" * 20)

    # Using the same example DataFrame
    df = pl.DataFrame({
        'id': [1, 2, 3],
        'list_column': [[1, 2], [2, 3, 4], [1, 4]]
    })

    # Get value counts
    value_counts = df['list_column'].explode().value_counts()
    print(value_counts)
    print("-*" * 20)

    # Using the same example DataFrame
    df = pl.DataFrame({
        'source': [1, 2, 3],
        'contype': ['edge type A', 'edge type B', 'edge type C'],
        'target': [[1, 2], [2, 3, 4], [1, 4]]
    })

    # Explode and get unique combinations
    unique_pairs = df.explode('target').unique()
    print(unique_pairs)

    # -------------------------------------------
    # Define a set of nodes
    nodes = {"A", "B", "C"}

    # Define edges as a Polars DataFrame
    edges_data = {
        "source": ["A", "A", "B"],
        "target": ["B", "C", "C"]
    }
    edges_df = pl.DataFrame(edges_data)


if __name__ == "__main__":
    main()
