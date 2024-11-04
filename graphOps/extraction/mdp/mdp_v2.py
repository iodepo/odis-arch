import argparse
import datetime
import io
import sys
import warnings
import pandas as pd
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

    args = parser.parse_args()

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

    sq = load_queries.read_file(qu)
    # print(sq)

    # Load graph
    print("RDF downloading", datetime.datetime.now())
    dg = readSource.read_data(u)
    print("RDF loading", datetime.datetime.now())

    df = graphProcessor(dg, sq)

    # Save
    if df is None:
        print("No graphs found")
    else:
        print(df.info())
        saveobject.write_data(o, df)


# get the value of a triple object from pyoxigraph
def getvalue(x):
  return x.value

# Process the graphs
def graphProcessor(dg, q):
    print("RDF aligning", datetime.datetime.now())
    r = graphshapers.contextAlignment(dg)


    print("RDF Loading", datetime.datetime.now())
    store = Store()
    mime_type = "application/n-quads"
    store.load(io.StringIO(r), mime_type, base_iri=None, to_graph=None)

    print("RDF querying", datetime.datetime.now())
    sq = store.query(q)
    qr = list(sq)

    print("Length SPARQL results:  {}".format(len(qr)))

    if len(qr) > 0:
        df = pd.DataFrame(qr)
        df = df.applymap(lambda x: x.value if x is not None else None)

        column_names = list(map(getvalue, sq.variables))
        df.columns = column_names

        return df
    return None


if __name__ == '__main__':
    main()
