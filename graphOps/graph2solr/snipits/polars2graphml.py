import polars as pl
import xml.etree.ElementTree as ET
import lancedb
from xml.dom import minidom
import pandas as pd
import numpy as np

def generate_graphml_polars(df, output_file="graph.graphml"):
    # Create the base GraphML structure
    graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns",
                         xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                         xsi_schemaLocation="http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")

    # Create the graph element
    graph = ET.SubElement(graphml, "graph", id="G", edgedefault="directed")

    # add id nodes for keywords
    df_expl = df.explode('txt_keywords').unique()
    unique_kw = df_expl.filter( pl.col("txt_keywords").is_not_null() & (pl.col("txt_keywords") != "None"))

    for node in unique_kw.iter_rows(named=True):
            node_xml = ET.SubElement(graph, "node", id=str(node['txt_keywords']))
            # ET.SubElement(node_xml, "data", key="type").text = str(node['name'])

    unique_id = unique_kw['id'].unique()   # where keywords, get all the unique IDs
    for node in unique_id:
        node_xml = ET.SubElement(graph, "node", id=str(node))

    # Add edges
    for edge in unique_kw.iter_rows(named=True):  # TODO no unique here, as that removes some edges?   unless it is row-wise
            edge_xml = ET.SubElement(graph, "edge", source=str(edge['id']), target=str(edge['txt_keywords']))
            # ET.SubElement(edge_xml, "data", key="ctype").text = str(edge['contype'])

    # Convert to a pretty-printed XML string
    rough_string = ET.tostring(graphml, encoding="utf-8", method="xml")
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # Write to file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(pretty_xml)
    print(f"GraphML file generated with pretty print: {output_file}")


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
    generate_graphml_polars(df)


if __name__ == "__main__":
    main()
