import argparse
import sys

from defs import etl_batch, etl_augment
from defs import etl_group
from defs import etl_jsonl
from defs import etl_query
from defs import etl_table

def main():
    parser = argparse.ArgumentParser(description="Multi-mode data processing program")
    subparsers = parser.add_subparsers(dest="mode", help="Operation mode")

    # Query mode parser
    query_parser = subparsers.add_parser("query", help="Query mode operations")
    query_parser.add_argument("--source", required=True, help="Source file/location")
    query_parser.add_argument("--sink", required=True, help="Output destination")
    query_parser.add_argument("--query", required=True, help="SPARQL query file")
    query_parser.add_argument("--table", required=True, help="LanceDB Table name")

    # Group mode parser
    group_parser = subparsers.add_parser("group", help="Group mode operations")
    group_parser.add_argument("--source", required=True, help="Source file/location")
    group_parser.add_argument("--sink", required=True, help="Output destination")

    # Augment mode parser
    augment_parser = subparsers.add_parser("augment", help="augment mode operations")
    augment_parser.add_argument("--source", required=True, help="Source file/location")

    # JSONL mode parser
    jsonl_parser = subparsers.add_parser("jsonl", help="JSONL mode operations")
    jsonl_parser.add_argument("--source", required=True, help="Source file/location")
    # jsonl_parser.add_argument("--sink", required=True, help="Output destination")

    # Table mode parser
    table_parser = subparsers.add_parser("table", help="Table mode operations")
    table_parser.add_argument("--source", required=True, help="Source file/location")
    table_parser.add_argument("--sink", required=True, help="Output destination")

    # Batch mode parser
    batch_parser = subparsers.add_parser("batch", help="Batch mode operations")
    batch_parser.add_argument("--source", required=True, help="Source file/location")
    batch_parser.add_argument("--sink", required=True, help="Output destination")

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Mode selection
    mode_handlers = {
        "query": etl_query.query_mode,
        "group": etl_group.group_mode,
        "augment": etl_augment.augment_mode,
        "jsonl": etl_jsonl.jsonl_mode,
        "table": etl_table.table_mode,
        "batch": etl_batch.batch_mode
    }

    # Execute the selected mode with appropriate parameters
    if args.mode == "query":
        mode_handlers[args.mode](args.source, args.sink, args.query, args.table)
    elif args.mode == "jsonl":
        mode_handlers[args.mode](args.source)
    elif args.mode == "augment":
        mode_handlers[args.mode](args.source)
    else:
        mode_handlers[args.mode](args.source, args.sink)

if __name__ == "__main__":
    main()
