import hashlib
from datetime import date

import ibis
import lancedb


def group_mode_new(source, sink):
    """Handle group mode operations"""
    print(f"Group mode: Processing data from {source} to {sink}")
    # Add group-specific logic here

    ibis.options.interactive = True

    ibis.set_backend("duckdb")
    data = "./stores/files/results_sparql.parquet"
    table = ibis.read_parquet(data)

    # Define the aggregations, I used both min and first, they should be the same, we will see.
    result = (
        table.group_by('id', 'type')
        .aggregate([
            table.g.min().name('txt_g'),
            table.name.collect().name('name'),
            table.name.collect().name('txt_name'),
            table.description.min().name('description'),
            table.description.collect().name('txt_description'),
            table.contenturl.collect().name('txt_distribution'),
            table.url.collect().name('txt_url'),
            table.temporalCoverage.collect().name('txt_temporalCoverage'),
            table.keywords.collect().name('txt_keywords'),
            table.courseName.collect().name('txt_courseName'),
            table.location.collect().name('txt_location'),
            table.iritype.collect().name('txt_iritype'),
            table.wkt.collect().name('txt_wkt'),
            table.geom.collect().name('txt_geom'),
            table.lat.collect().name('txt_lat'),
            table.long.collect().name('txt_long'),
            table.place_name.collect().name('txt_place_name'),
            table.datePublished.collect().name('txt_datePublished'),
            table.dateModified.collect().name('txt_dateModified'),
            table.area.collect().name('txt_area'),
            table.length.collect().name('txt_length'),
            table.centroid.collect().name('txt_centroid'),
            table.geojson.collect().name('txt_geojson')
        ])
    )

    df = result.to_pandas()

    ## DANGER ZONE
    ## The items that follow represent some corrections that should not happen

    ## Add in the required index_id column based on the md5 hash of the id column.
    # Do this after grouping to avoid making a list of hash ids
    def compute_md5(value):
        if value is None:
            return None
        return hashlib.md5(value.encode()).hexdigest()

    df['index_id'] = df['id'].apply(compute_md5)

    # Add a new column with today's date in ISO format
    df["indexed_ts"] = date.today().isoformat()

    # Add a new column with a constant string value "false"
    df["has_geom"] = "false"

    # Add a new column with a constant string value "false"
    df["txt_region"] = "Atlantic"

    df["json_source"] = '{"@context": "https://schema.org/", "@type": "Person", "name": "John Doe" }'

    ## END DANGER ZONE

    # df.to_csv(sink)  CSV not needed
    df.to_parquet("./stores/testgroupout.parquet")

    # Create or get LanceDB table and write data
    db = lancedb.connect("./stores/lancedb")
    db.create_table(f"{source}_grouped", data=df, mode="overwrite")