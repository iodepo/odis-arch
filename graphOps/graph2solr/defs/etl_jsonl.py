import json
import math
import sys
import lancedb
import numpy as np


def check_value(value):
    # Check if the value is None
    if value is None:
        return False

    if isinstance(value, str):
        # if value is a string
        if value.lower() == "nan":  # check if the string is "nan"
            return False

    if isinstance(value, str):
        # if value is a string
        if value not in [None, "", "nan", "NaN"] and not (isinstance(value, float) and math.isnan(value)):
            return True
        else:
            return False
    else:
        # assuming value is a list of strings or similar iterable
        check_list = []
        for item in value:
            if item not in [None, "", "nan", "NaN"] and not (isinstance(item, float) and math.isnan(item)):
                check_list.append(True)
            else:
                check_list.append(False)

        # Return True if all items pass the check, False otherwise
        return all(check_list)

def check_filter(value):
    if value is None:
        return False

    if isinstance(value, str):
        if value.lower() == "nan" or value == "":
            return False

    if isinstance(value, float) and math.isnan(value):
        return False

    if isinstance(value, list) and len(value) == 0:
        return False

    return True

def to_list(value):
    if isinstance(value, np.ndarray):
        # Convert ndarray to list which is serializable
        return value.tolist()
    else:
        return value


def jsonl_mode(source):
    print(f"JSONL mode: Processing data from lancedb table {source} to a file")

    dblocation = "./stores/lancedb"
    table_name = source

    # Connect to LanceDB
    db = lancedb.connect(dblocation)
    table = db[table_name]
    output_jsonl = f"./stores/solrInputFiles/{table_name}.jsonl"

    all_records = table.to_pandas().to_dict('records')

    # print(all_records[100])
    # sys.exit(0)

    for dict in all_records:
        for key, value in dict.items():
            if isinstance(value, float):
                dict[key] = str(value)

    # Open JSON(L) file for writing
    with open(output_jsonl, 'w') as jsonlfile:
        # Convert each row to JSON
        for row in all_records:
            # Remove: None, nan, NaNTType
            filtered_row = {key: value for key, value in row.items() if check_filter(value)}

            # convert numpay ndarray to list
            converted_row = {key: to_list(value) for key, value in filtered_row.items()}

            # filtered_row = {key: value for key, value in row.items() if value not in [None, "", "nan", "NaN"] and not (
            #             isinstance(value, float) and math.isnan(value))}
            try:
                # Add a new "keys" entry that contains all other keys
                converted_row["keys"] = [
                    key for key, value in converted_row.items()
                    if check_value(value)
                ]

                # Write the updated row JSON to the file with compact formatting
                jsonlfile.write(json.dumps(converted_row, separators=(',', ':')) + '\n')
            except Exception as e:
                print(f"Error processing row: {converted_row}, Exception: {str(e)}")

    print(f"Converted table {table_name} to {output_jsonl}")
