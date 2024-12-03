#!/bin/bash

# Check if a command line argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# List of names
names=("baseQuery" "course" "dataset" "person" "sup_geo" "sup_temporal")

# Loop through each name and print the combination with the argument
for name in "${names[@]}"; do
 python3 mdp_v2.py  --ssl False  \
  --source "s3://ossapi.oceaninfohub.org/commons/ODIS-KG-MAIN/latest/$1_release.nq"  \
  --query "./queries/$name.rq"  \
  --output  "s3://ossapi.oceaninfohub.org/commons/OIH-PROD/latest/$1_$name.parquet"
done
