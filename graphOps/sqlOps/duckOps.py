import json
import duckdb
import pandas as pd
import shapely
from shapely import wkt
from shapely.geometry import Polygon, MultiPolygon, shape, mapping
import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

consoleCode = """CREATE TABLE base (id VARCHAR, type VARCHAR, name VARCHAR, url VARCHAR, description VARCHAR, headline VARCHAR, g VARCHAR );
CREATE TABLE dataset (id VARCHAR, type VARCHAR, sameAs VARCHAR, license VARCHAR, citation VARCHAR, keyword VARCHAR, includedInDataCatalog VARCHAR, distribution VARCHAR, region VARCHAR, provider VARCHAR, publisher VARCHAR, creator VARCHAR);
CREATE TABLE sup_time (id VARCHAR, type VARCHAR, time VARCHAR, temporalCoverage VARCHAR, dateModified VARCHAR, datePublished VARCHAR, );
CREATE TABLE course (id VARCHAR, type VARCHAR, txt_location VARCHAR);
CREATE TABLE person (id VARCHAR, type VARCHAR, address VARCHAR, txt_knowsAbout VARCHAR, txt_knowsLanguage VARCHAR);
CREATE TABLE sup_geo (id VARCHAR, type VARCHAR, placename VARCHAR, geotype VARCHAR, geompred VARCHAR, geom VARCHAR, lat VARCHAR, long VARCHAR, wkt VARCHAR, g VARCHAR, filteredgeom VARCHAR, centroid VARCHAR, length VARCHAR, area VARCHAR, geojson VARCHAR, fregion VARCHAR  );

COPY base FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_baseQuery.parquet';
COPY dataset FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_dataset.parquet';
COPY sup_time FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_sup_temporal.parquet';
COPY course FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_course.parquet';
COPY person FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_person.parquet';
COPY sup_geo FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/active/*_sup_geo.parquet';
"""

# removed from the select clause:  geo_agg.geojson,  base_agg.b_headline AS headline,
sql = """SELECT base_agg.id AS externalIds,
       base_agg.type_list AS type,
       base_agg.name_list AS title,
       dataset_agg.kw_list AS keywords,
       base_agg.b_url AS url,
       base_agg.b_desc AS description,
       geo_agg.geom_list,
       geo_agg.wkt_list,
       temporal_agg.tc_list,
       temporal_agg.dp_list
FROM (SELECT id,
             STRING_AGG(DISTINCT type, ', ') AS type_list,
             STRING_AGG(DISTINCT name, ', ') AS name_list,
             any_value(url)                  AS b_URL,
             any_value(description)          AS b_desc,
             any_value(headline)             AS b_headline
      FROM base
      GROUP BY id) AS base_agg
         JOIN (SELECT id, ANY_VALUE(includedInDataCatalog), STRING_AGG(DISTINCT keyword, ', ') AS kw_list
               FROM dataset
               GROUP BY id) AS dataset_agg
              ON base_agg.id = dataset_agg.id
         JOIN (SELECT id, STRING_AGG(DISTINCT geom, ', ') AS geom_list,
                      STRING_AGG(DISTINCT wkt, ', ') AS wkt_list,
                      STRING_AGG(DISTINCT geojson, ', ') AS geojson
               FROM sup_geo
               GROUP BY id) AS geo_agg
              ON base_agg.id = geo_agg.id
         JOIN (SELECT id, STRING_AGG(DISTINCT temporalCoverage, ', ') AS tc_list, STRING_AGG(DISTINCT datePublished, ', ') AS dp_list
               FROM sup_time
               GROUP BY id) AS temporal_agg
              ON base_agg.id = temporal_agg.id
ORDER By base_agg.id;
"""

duckdb.install_extension("httpfs")

# Instantiate the DuckDB connection
con = duckdb.connect()

# Load
con.execute(consoleCode)

# Query
df = con.execute(sql).fetchdf()

# print(df.info())

# Iterate through each row and save as GeoJSON
for idx, row in df.iterrows():
    row_df = pd.DataFrame([row])
    row_df.to_json(f'output/row_{idx}.json')

# save to pandas (should be geopandas?)
df.to_parquet('typeDataSetResults.parquet')
