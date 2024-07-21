import argparse
import os
import sys

import pandas as pd

# load mdp into a dataframe

def main():
    parser = argparse.ArgumentParser(description='Input CSV file from SPARQL Query')
    parser.add_argument('--source', type=str, help='source file (csv)')
    parser.add_argument("--outputdir", type=str, help="Output directory")

    args = parser.parse_args()
    fi = args.source
    od = args.outputdir

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.outputdir is None:
        print("Error: the --outputdir argument is required")
        sys.exit(1)

    df = pd.read_csv(fi, compression='gzip')

    # Make edges
    edges = df[['source', 'target', 'type']]

    # Make notes
    ids = pd.concat([df['source'], df['target']]).reset_index(drop=True)
    types = pd.concat([df['sType'], df['tType']]).reset_index(drop=True)
    nodes = pd.DataFrame({'Id': ids, 'SDOType': types})

    nodes.drop_duplicates()

    # Add sequential label
    # TODO, use schema:name as label and only add a label to those without name
    nodes['Label'] = ['Label ' + str(i) for i in range(len(nodes))]

    # output, named based on input
    bfn = os.path.splitext(os.path.basename(fi))[0].replace(".", "")
    ef = os.path.join(od, f'{bfn}EDGES.csv')
    nf = os.path.join(od, f'{bfn}NODES.csv')

    edges.to_csv(ef, index=False)
    nodes.to_csv(nf, index=False)

if __name__ == '__main__':
    main()
