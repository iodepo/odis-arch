import polars as pl
import json
import argparse


def convert_csv_to_jsonl(input_csv: str, output_jsonl: str, csv_options: dict = None):
    """
    Convert a CSV file to JSONL format using Polars with robust schema handling.

    Args:
        input_csv (str): Path to input CSV file
        output_jsonl (str): Path to output JSONL file
        csv_options (dict): Optional dictionary of CSV reading options for Polars
    """
    # Set default options if none provided
    if csv_options is None:
        csv_options = {}

    # Default options for robust parsing
    default_options = {
        "has_header": True,
        "infer_schema_length": 100000,  # Increased sample size for better type inference
        "ignore_errors": True,  # Continue on parsing errors
        "try_parse_dates": True,  # Attempt to parse dates
        "null_values": ["NA", "null", "NULL", "", "0"],  # Common null values
    }

    # Merge provided options with defaults
    csv_options = {**default_options, **csv_options}

    try:
        # First, try to infer schema from a sample of the data
        sample_df = pl.read_csv(input_csv, n_rows=1000, **csv_options)
        schema = sample_df.schema

        # Convert all columns to string type to avoid parsing issues
        schema = {name: pl.Utf8 for name in schema.keys()}

        # Read the full CSV with the string schema
        df = pl.read_csv(
            input_csv,
            schema=schema,
            **csv_options
        )

        # Open output file and write each row as JSON
        with open(output_jsonl, 'w', encoding='utf-8') as f:
            for row in df.iter_rows(named=True):
                # Just dump the row directly since everything is already strings
                json.dump(row, f, ensure_ascii=False)
                f.write('\n')

        print(f"Successfully converted {input_csv} to {output_jsonl}")
        print(f"Number of records processed: {len(df)}")
        print(f"Columns: {', '.join(df.columns)}")

    except Exception as e:
        print(f"Error during conversion: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert CSV to JSONL.')
    parser.add_argument('input_csv', type=str, help='Path to the input CSV file.')
    parser.add_argument('output_jsonl', type=str, help='Path to the output JSONL file.')
    parser.add_argument('--encoding', type=str, default='utf-8', help='CSV file encoding.')
    parser.add_argument('--separator', type=str, default=',', help='CSV file separator.')

    args = parser.parse_args()

    convert_csv_to_jsonl(
        input_csv=args.input_csv,
        output_jsonl=args.output_jsonl,
        csv_options={
            "encoding": args.encoding,
            "separator": args.separator
        }
    )
