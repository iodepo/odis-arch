import argparse
import re
import sys

import numpy as np
from dateutil import parser

from defs import readobject
from defs import saveobject


def main():
    # Params
    p = argparse.ArgumentParser(description="Process some arguments.")
    p.add_argument("--source", type=str, help="Source URL")
    p.add_argument("--output", type=str, help="Output file")

    args = p.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.output is None:
        print("Error: the --output argument is required")
        sys.exit(1)

    u = args.source
    o = args.output

    df = readobject.get_object(u)

    #process the dataframe
    print("Processing Stage: Temporal")

    if "temporalCoverage" in df.columns:
        df['temporalCoverage'] = df['temporalCoverage'].astype(
            'str')  # fine to make str since we don't use in the solr JSON
        df['dt_startDate'] = df['temporalCoverage'].apply(
            lambda x: re.split("/", x)[0] if "/" in x else np.nan)
        df['dt_endDate'] = df['temporalCoverage'].apply(
            lambda x: re.split("/", x)[1] if "/" in x else np.nan)
        df['n_startYear'] = df['dt_startDate'].apply(
            lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
        df['n_endYear'] = df['dt_endDate'].apply(
            lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
    else:
        print("NOTE:  no temporal data found")

    print(df.head())

    saveobject.write_data(o, df)

if __name__ == "__main__":
    main()