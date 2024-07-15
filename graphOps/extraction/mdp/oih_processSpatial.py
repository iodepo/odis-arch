import argparse
import sys

import numpy as np

from defs import graphshapers
from defs import readobject
from defs import saveobject
from defs import spatial
from defs import regionFor


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

    # process the dataframe
    print("Processing Stage: Geospatial centroid")

    df['filteredgeom'] = df['geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)

    print("Processing Stage: Geospatial centroid")
    df['centroid'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "centroid"))
    df['centroid'] = df['centroid'].astype(str)

    print("Processing Stage: Geospatial length")
    df['length'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "length"))

    print("Processing Stage: Geospatial area")
    df['area'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "area"))

    print("Processing Stage: Geospatial wkt")
    df['wkt'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "wkt"))
    df['wkt'] = df['wkt'].astype(str)

    print("Processing Stage: Geospatial geojson")
    df['geojson'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "geojson"))
    df['geojson'] = df['geojson'].astype(str)

    print(df.head())

    if "name" in df.columns:
        df['name'] = df['name'].astype(str)  # why is this needed?

        # TODO, incorporate Jeff's code as a Lambda function (will need to support multiple possible regions per entry)
    if "name" in df.columns:
        print("Processing region for name")
        df['nregion'] = df['name'].apply(lambda x: regionFor.name(x) if x else x)
    if "address" in df.columns:
        print("Processing region for address")
        df['aregion'] = df['address'].apply(lambda x: regionFor.address(x) if x else x)
    if "addressCountry" in df.columns:
        print("Processing region for addressCountry")
        df['cregion'] = df['addressCountry'].apply(
            lambda x: regionFor.countryLastProcessing(x) if x else x)
    if "wkt" in df.columns:
        print("Processing region for wkt")
        df['fregion'] = df['wkt'].apply(lambda x: regionFor.feature(x) if x else x)

    saveobject.write_data(o, df)

if __name__ == "__main__":
    main()