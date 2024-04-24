import argparse
import gc
import re
import sys
import io
import warnings
import datetime
from functools import reduce
 
import kglab
import numpy as np
import pandas as pd
from dateutil import parser
from rdflib import ConjunctiveGraph  # needed for quads
import polars as pl
from tqdm import tqdm
from pyoxigraph import *

from defs import graphshapers
from defs import load_queries
from defs import readSource
from defs import polar_calls
from defs import regionFor
from defs import spatial
from defs import saveobject

warnings.simplefilter(action='ignore', category=FutureWarning)  # remove pandas future warning


def main():
    # Params
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--output", type=str, help="Output file")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.output is None:
        print("Error: the --output argument is required")
        sys.exit(1)

    u = args.source
    o = args.output

    # Load graph
    print("RDF download started", datetime.datetime.now())
    dg = readSource.read_data(u)
    print("RDF downloaded, starting load stage", datetime.datetime.now())

    mf = graphProcessor(dg)

    # # Reporting
    # print("Reporting Stage: The following is the current dataframe shape to exported")
    # print(mf.info())
    #
    # # Save
    # saveobject.write_data(o, mf)


def graphProcessor(dg):
    r = graphshapers.contextAlignment(dg)

    print("RDF loaded, starting query stage", datetime.datetime.now())

    store = Store()
    mime_type = "application/n-quads"
    store.load(io.StringIO(r), mime_type, base_iri=None, to_graph=None)
    print("RDF loaded, starting query stage", datetime.datetime.now())

    # Load Queries
    sfl = [
        "./queries/subjectsTypes.rq",    # q1
        "./queries/template_dataset.rq",  # q2
        "./queries/baseQuery.rq",
        "./queries/course.rq",
        "./queries/dataset.rq",
        "./queries/person.rq",
        "./queries/sup_geo.rq",
        "./queries/sup_temporal.rq"
    ]

    qlist = load_queries.read_files(sfl)

    # conduct initial query for types and associated subject IRIs
    qr = list(store.query(qlist['q1']))

    print("Length of SPARQL query results:  {}".format(len(qr)))

    qrl = []
    for r in qr:
        qrl.append([r['id'].value, r['type'].value])

    # print(qr[0])
    # print(qr[0]['id'].value)
    # print(qr[0]['type'].value)

    # for binding in qr:
    #     print("{}  {}".format(binding['id'].value, binding['type'].value))
    df = pl.from_records(qrl, schema=["id", "type"])
    print("Length of Polars data frame:     {}".format(len(df)))

    dsl = polar_calls.dataset_list(df, store, qlist)

    return 0


if __name__ == '__main__':
    main()
