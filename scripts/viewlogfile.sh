#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 filename"
  exit 1
fi

filename=$1

if [ ! -f $filename ]; then
  echo "Error: file not found - $filename"
  exit 2
fi

grep -o "{[^{}]*}" $filename | grep "\"file\":" | jq .

