# H3 optimization options

## NOtes

*  python ./augmented2h3.py works but
*  python ./augmented2h3_polars.py does not work


Example generated grids
85091a37fffffff,85091b7bfffffff,85091e6ffffffff,8509184ffffffff,8509a917fffffff,8509adc7fffffff,8509a987fffffff,8509a907fffffff,

## Snipits

```python
from joblib import Parallel, delayed

# Parallelize the process_geojson function
def parallel_process_geojson(df, n_jobs=-1):
    # Use Parallel to apply the function in parallel
    results = Parallel(n_jobs=n_jobs)(
        delayed(process_geojson)(x) if x is not None else None for x in df['geojson_shapely']
    )
    # Assign the results back to the dataframe
    df['h3_cells'] = results
    return df

# Apply parallel processing
df = parallel_process_geojson(df)

```



```python
from concurrent.futures import ProcessPoolExecutor

def parallel_apply(df, func, column):
    with ProcessPoolExecutor() as executor:
        # Map the function to the column in parallel
        results = list(executor.map(func, df[column]))
    return results

# Apply parallel processing
df['h3_cells'] = parallel_apply(df, lambda x: process_geojson(x) if x is not None else None, 'geojson_shapely')

```


## Dask

```python
import dask.dataframe as dd

# Convert the pandas DataFrame to a Dask DataFrame
ddf = dd.from_pandas(df, npartitions=4)

# Apply the function in parallel
ddf['h3_cells'] = ddf['geojson_shapely'].map(lambda x: process_geojson(x) if x is not None else None)

# Compute the results back into a pandas DataFrame
df = ddf.compute()

```