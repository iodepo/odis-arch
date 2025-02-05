import lancedb
from dateutil import parser
import re
import numpy as np

from datetime import datetime
import pandas as pd

def to_iso_date(date_str):
    """
Convert various date string formats to ISO format (YYYY-MM-DD).
Returns None if conversion fails.

Parameters:
date_str: String or datetime-like object representing a date

Returns:
str: ISO formatted date string (YYYY-MM-DD) or None if conversion fails
    """
    if pd.isna(date_str):
        return None

    if isinstance(date_str, (datetime, pd.Timestamp)):
        return date_str.strftime('%Y-%m-%d')

    # Try to handle year-only input
    try:
        # Remove any whitespace and check if it's a 4-digit year
        year_str = str(date_str).strip()
        if year_str.isdigit() and len(year_str) == 4:
            year = int(year_str)
            if 1000 <= year <= 9999:  # Reasonable year range check
                return f"{year}-01-01"
    except (ValueError, TypeError):
        pass

    # Common date formats to try
    date_formats = [
        '%Y-%m-%d',      # 2023-12-31
        '%d/%m/%Y',      # 31/12/2023
        '%m/%d/%Y',      # 12/31/2023
        '%d-%m-%Y',      # 31-12-2023
        '%m-%d-%Y',      # 12-31-2023
        '%Y/%m/%d',      # 2023/12/31
        '%d.%m.%Y',      # 31.12.2023
        '%B %d, %Y',     # December 31, 2023
        '%d %B %Y',      # 31 December 2023
        '%Y%m%d',        # 20231231
    ]

    for fmt in date_formats:
        try:
            return datetime.strptime(str(date_str).strip(), fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue

    return None

# Connect to LanceDB
db = lancedb.connect("../../stores/lancedb")
table = db.open_table("sparql_results")

# Convert to DataFrame and then to JSONL
df = table.to_pandas()
print(f"Converted {len(df)} records to pandas format")

# df['area'] = df['geom'].apply(lambda x: spatial.gj(str(x), "area"))

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

df['datePublished'] = df['datePublished'].apply(to_iso_date)
df['dt_startDate'] = df['dt_startDate'].apply(to_iso_date)
df['dt_endDate'] = df['dt_endDate'].apply(to_iso_date)

df.to_csv('temporal.csv', index=False)

# Create or get LanceDB table and write data
# table = db.create_table(f"{source}_geo", data=df, mode="overwrite")
# print(table)

print("End of Line")
