import duckdb
import lancedb
import ibis
import pyarrow as pa

ibis.options.interactive = True

ibis.set_backend("duckdb")
data = "../stores/files/results_sparql.parquet"
table = ibis.read_parquet(data)

with open("../SPARQL/duckdbSQL.sql", "r") as file:
    query = file.read()

# Define the aggregations
result = (
    table.group_by('id')
    .aggregate([
        table.g.group_concat().name('txt_g'),
        table.type.min().name('type'),
        table.name.group_concat().name('name'),
        table.name.group_concat().name('txt_name'),
        table.description.min().name('description'),
        table.description.group_concat().name('txt_description'),
        table.contenturl.group_concat().name('txt_distribution'),
        table.url.group_concat().name('txt_url'),
        table.temporalCoverage.group_concat().name('txt_temporalCoverage'),
        table.keywords.group_concat().name('txt_keywords'),
        table.courseName.group_concat().name('txt_courseName'),
        table.location.group_concat().name('txt_location'),
        table.iritype.group_concat().name('txt_iritype'),
        table.courseName_duplicated_0.group_concat().name('txt_courseName_duplicated_0'),
        table.wkt.group_concat().name('txt_wkt'),
        table.geom.group_concat().name('txt_geom'),
        table.lat.group_concat().name('txt_lat'),
        table.long.group_concat().name('txt_long'),
        table.place_name.group_concat().name('txt_place_name'),
        table.datePublished.first().name('txt_datePublished'),  # Changed to first()
        table.dateModified.first().name('txt_dateModified'),    # Changed to first()
        table.area.group_concat().name('txt_area'),
        table.length.group_concat().name('txt_length'),
        table.centroid.group_concat().name('txt_centroid'),
        table.geojson.group_concat().name('txt_geojson')
    ])
)

df = result.to_pandas()

result.to_parquet("ibisTesting.parquet")


