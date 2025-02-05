import csv
import json
import argparse

# Currently works with SPARQL output rolled up into collections per ID

def csv_to_jsonl(input_csv, output_jsonl):
    """
    Convert a CSV file to a JSONL file, using the first row as column names.

    Args:
        input_csv (str): Path to the input CSV file
        output_jsonl (str): Path to the output JSONL file
    """
    # Read the CSV file
    with open(input_csv, 'r') as csvfile:
        # Use csv.reader to read all rows
        csv_reader = csv.reader(csvfile)

        # Read the header (first row) as column names
        headers = next(csv_reader)

        # Open JSONL file for writing
        with open(output_jsonl, 'w') as jsonlfile:
            # Convert each row to a JSON line
            for row in csv_reader:
                # Create a dictionary using headers as keys and row values
                row_dict = dict(zip(headers, row))

                # Write each row as a JSON line
                jsonlfile.write(json.dumps(row_dict) + '\n')

    print(f"Converted {input_csv} to {output_jsonl}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Convert CSV to JSONL')
    parser.add_argument('input', help='Input CSV file path')
    parser.add_argument('output', help='Output JSONL file path')

    # Parse arguments
    args = parser.parse_args()

    # Perform conversion
    csv_to_jsonl(args.input, args.output)

# Allow script to be run directly
if __name__ == "__main__":
    main()
