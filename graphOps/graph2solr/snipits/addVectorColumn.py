import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

db = lancedb.connect("../stores/lancedb")
source = "sparql_results_grouped_augmented"

# Get the embedding function from the registry
registry = get_registry()
embedding_function = registry.get("sentence-transformers").create(name="all-MiniLM-L6-v2")

class YourModel(LanceModel):
    description: str = embedding_function.SourceField()
    vector: Vector(embedding_function.ndims()) = embedding_function.VectorField()

# Assuming your table is called 'your_table'
existing_table = db[source]
existing_data = existing_table.to_pandas()   # use polars instead?

# Create a new table with the new schema
new_table = db.create_table("search", schema=YourModel)

# Add data to the new table with embeddings
new_table.add(existing_data.to_dict('records'))
