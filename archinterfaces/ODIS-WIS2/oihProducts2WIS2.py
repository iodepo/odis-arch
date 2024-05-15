# Imports and definitions
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning
import pandas as pd
import geopandas as gpd
from shapely import wkt
import s3fs
import pyarrow.parquet as pq
import shapely
import os
import re
import duckdb

createCmd = '''CREATE TABLE base (id VARCHAR, type VARCHAR, name VARCHAR, url VARCHAR, description VARCHAR, headline VARCHAR, g VARCHAR );
CREATE TABLE dataset (id VARCHAR, type VARCHAR, sameAs VARCHAR, license VARCHAR, citation VARCHAR, keyword VARCHAR, includedInDataCatalog VARCHAR, distribution VARCHAR, region VARCHAR, provider VARCHAR, publisher VARCHAR, creator VARCHAR);
CREATE TABLE sup_time (id VARCHAR, type VARCHAR, time VARCHAR, temporalCoverage VARCHAR, dateModified VARCHAR, datePublished VARCHAR, );

COPY base FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_baseQuery.parquet';
COPY dataset FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_dataset.parquet';
COPY sup_time FROM '/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_sup_temporal.parquet';

CREATE TABLE course AS SELECT * FROM read_parquet('/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_course.parquet',  union_by_name=true);
CREATE TABLE person AS SELECT * FROM read_parquet('/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_person.parquet',  union_by_name=true);
CREATE TABLE sup_geo AS SELECT * FROM read_parquet('/home/fils/src/Projects/OIH/odis-arch/graphOps/extraction/mdp/output/*_sup_geo.parquet',  union_by_name=true);
'''

sqlCmd = '''SELECT base_agg.id, base_agg.type_list, base_agg.name_list, dataset_agg.kw_list,
        base_agg.b_url, base_agg.b_desc, base_agg.b_headline, geo_agg.geom_list,
        temporal_agg.tc_list, temporal_agg.dp_list
FROM (
    SELECT id, STRING_AGG(DISTINCT type, ', ') AS type_list, STRING_AGG(DISTINCT name, ', ') AS name_list,
           any_value(url) AS b_URL, any_value(description) AS b_desc, any_value(headline) AS b_headline
    FROM base
    GROUP BY  id
) AS base_agg
JOIN (
    SELECT id, ANY_VALUE(includedInDataCatalog), STRING_AGG(DISTINCT keyword, ', ') AS kw_list
    FROM dataset
    GROUP BY  id
) AS dataset_agg
    ON base_agg.id = dataset_agg.id
JOIN (
    SELECT id,  STRING_AGG(DISTINCT geom, ', ') AS geom_list
    FROM sup_geo
    GROUP BY  id
) AS geo_agg
    ON base_agg.id = geo_agg.id
JOIN (
    SELECT id,  STRING_AGG(DISTINCT temporalCoverage, ', ') AS tc_list,  STRING_AGG(DISTINCT datePublished, ', ') AS dp_list
    FROM sup_time
    GROUP BY  id
) AS temporal_agg
ON   base_agg.id = temporal_agg.id
ORDER By base_agg.id;
'''


con = duckdb.connect()
con.execute(createCmd)  # load from url

df = con.execute(sqlCmd).fetchdf()

print(df.info())
