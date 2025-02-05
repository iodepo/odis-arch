import argparse
import datetime
import io
import sys
import warnings
import pandas as pd
from icecream import ic
import pyoxigraph
from pyoxigraph import *
from defs import graphshapers
from defs import load_queries
from defs import readSource
from defs import saveobject

warnings.simplefilter(action='ignore', category=FutureWarning)  # remove pandas future warning

def main():
    # Params
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--query", type=str, help="Query URL")
    parser.add_argument("--output", type=str, help="Output file")
    parser.add_argument("--ssl", type=lambda x: (str(x).lower() == 'true'), help="Enable SSL flag")


    args = parser.parse_args()

    if args.ssl:
        print("SSL is enabled")

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.query is None:
        print("Error: the --query argument is required")
        sys.exit(1)

    if args.output is None:
        print("Error: the --output argument is required")
        sys.exit(1)

    u = args.source
    qu = args.query
    o = args.output
    ssl = args.ssl

    sq = load_queries.read_file(qu)
    # print(sq)

    # Load graph
    print("RDF downloading", datetime.datetime.now())
    dg = readSource.read_data(u, ssl)
    print("RDF loading", datetime.datetime.now())

    r = graphProcessor(dg, sq, o, ssl)
    print("Issues: " + str(r))




# get the value of a triple object from pyoxigraph
def getvalue(x):
  return x.value

# This map is necessary to get the values from the pyoxigraph.QuerySolutions
def extract_value(cell):
    if isinstance(cell, (pyoxigraph.Literal, pyoxigraph.NamedNode, pyoxigraph.BlankNode)):
        return cell.value
    return cell

# Process the graphs
def graphProcessor(dg, q, o, ssl):
    print("RDF aligning", datetime.datetime.now())
    r = graphshapers.contextAlignment(dg)


    print("RDF Loading", datetime.datetime.now())
    store = Store()
    mime_type = RdfFormat.N_QUADS
    store.load(io.StringIO(r), format=mime_type, base_iri=None, to_graph=None)

    print("RDF querying", datetime.datetime.now())
    sq = store.query(q)
    ql = list(sq)

    print("Length SPARQL results:  {}".format(len(ql)))

    if len(ql) > 0:
        # get the list of the variables from the query for ues in the dataframe
        vars = sq.variables
        value_list = [variable.value for variable in vars]
        df = pd.DataFrame(ql, columns=value_list)
        # df = df.applymap(lambda x: x.value if x is not None else None)
        df = df.applymap(extract_value)

        # ic(df)

        saveobject.write_data(o, df, ssl)

        return None

    return None


if __name__ == '__main__':
    main()
