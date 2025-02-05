#!/bin/bash

# Check if input file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <input.jsonl>"
    exit 1
fi

# Input file path
INPUT_FILE=$1

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File $INPUT_FILE does not exist."
    exit 1
fi

# Counter for tracking processed lines
COUNTER=0

# Read the file line by line
while IFS= read -r line
do
    # Increment counter
    ((COUNTER++))

    # Create a temporary JSON file for this line
    TEMP_JSON=$(mktemp)
    # Wrap the JSONL line in an "add" envelope for Solr
    echo "$line" | jq '{add: {doc: .}}' > "$TEMP_JSON"

    # Run curl command with the temporary JSON file
    echo "Processing line $COUNTER..."
    curl -X POST \
         -H "Content-Type: application/json" \
         "http://localhost:8983/solr/gettingstarted/update?commit=true" \
         --data-binary "@$TEMP_JSON"

    # Check curl exit status
    if [ $? -eq 0 ]; then
        echo "Line $COUNTER uploaded successfully."
    else
        echo "Error uploading line $COUNTER."
    fi

    # Remove temporary file
    rm "$TEMP_JSON"

done < "$INPUT_FILE"

# TODO:  doesn't catch and report errors properly
echo "Finished processing $COUNTER lines from $INPUT_FILE"


