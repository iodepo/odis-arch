#!/bin/bash

input_directory="./output_md"
output_directory="./output_txt"

# Ensure the output directory exists
mkdir -p "$output_directory"

# Process each Markdown file
for file in "$input_directory"/*.md; do
    if [ -f "$file" ]; then
        base_name=$(basename "$file" .md)
        output_file="$output_directory/$base_name.txt"
        pandoc -f markdown -t plain "$file" -o "$output_file"
        echo "Processed $file to $output_file"
    fi
done
