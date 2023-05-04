#!/bin/bash

# Specify the file to read
filename="sources.txt"

# Check if the file exists
if [[ ! -f "$filename" ]]; then
  echo "File not found: $filename"
  exit 1
fi

## try
## Manually create the destination directory path
# mkdir -p /destination/directory/path
## Use the cp command to copy the source directory to the destination
#cp -r /source/directory/path /destination/directory/path

# Loop through each line in the file
while IFS= read -r line; do
  # Use the 'echo' command to print each line
  echo "$line"
  mkdir -p ./$line
  #du -skh ../../$line
  cp -r  ../../$line/* ./$line
done < "$filename"

