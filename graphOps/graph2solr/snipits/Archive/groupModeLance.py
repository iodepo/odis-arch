
def group_mode_lance(source, sink):
    """Handle group mode operations"""
    print(f"Group mode: Processing data from {source} to {sink}")
    # Add group-specific logic here

    db = lancedb.connect("./stores/lancedb")
    table = db.open_table(source)
    arrow_table = table.to_arrow()

    # r = duckdb.query("SELECT * FROM arrow_table LIMIT 10")
    # print(r)

    conn = duckdb.connect()
    conn.register("arrow_table", arrow_table)

    # Explain test (not needed)
    # explain_query = "EXPLAIN SELECT * FROM arrow_table LIMIT 10"
    # result = conn.sql(explain_query)
    # print(result)

    # Get the column names
    columns = conn.execute("PRAGMA table_info('arrow_table')").fetchall()
    column_names = [col[1] for col in columns]

    # Assuming 'ID' is the column you want to group by
    id_column = 'id'
    singleval_columns =  ['type', 'name', 'description', 'datePublished', 'dateModified']
    other_columns = [col for col in column_names if col != id_column]

    # Create list aggregation for other columns with unique values
    # Orig: f'STRING_AGG(DISTINCT {col} ) AS list_{col}' for col in other_columns
    agg_columns = ', '.join([
        f'STRING_AGG(DISTINCT {col} ) AS txt_{col}' for col in other_columns
    ])

    # Adjust the aggregation logic  NOTE:  this seems to have issues
    # agg_columns = ', '.join([
    #     # For specific columns, use FIRST_VALUE to get only the first value
    #     f' FIRST_VALUE({col} [ IGNORE NULLS]) AS {col}' if col in singleval_columns else
    #     # For other columns, use STRING_AGG to return a list
    #     f' STRING_AGG(DISTINCT {col}) AS txt_{col}' for col in other_columns
    # ])


    # Construct the full query
    # query_orig = f"""
    #     SELECT {id_column}, {agg_columns}
    #     FROM arrow_table
    #     GROUP BY {id_column}
    #     """

    # Read the SPARQL query from file
    with open("./SPARQL/duckdbSQL.sql", "r") as file:
        query = file.read()

    df = conn.execute(query).fetchdf()

    ## Add in the required indexed_id column based on the md5 hash of the id column.
    # Do this after grouping to avoiding make a list of hash ids
    def compute_md5(value):
        if value is None:
            return None
        return hashlib.md5(value.encode()).hexdigest()

    df['indexed_id'] = df['id'].apply(compute_md5)

    # Add a new column with today's date in ISO format
    df["indexed_ts"] = date.today().isoformat()

    # Add a new column with a constant string value "false"
    df["has_geom"] = "false"

    # Add a new column with a constant string value "false"
    df["txt_region"] = "Atlantic"

    ## Keys
    # Function to check for non-empty and non-None values
    # def non_empty_columns(row):
    #     return json.dumps([col for col in row.index if row[col] not in [None, ""]])

    # Apply the function to each row
    # df["keys"] = df.apply(non_empty_columns, axis=1)
    # df['keys'] = '"id","type","name","txt_name","description","txt_description","txt_keywords","has_geom"'

    # save results to a file (make an optional)
    df.to_csv(sink)

    # Create or get LanceDB table and write data
    table = db.create_table(f"{source}_grouped", data=df, mode="overwrite")
    print(table)