#!/bin/bash
# GMT script to create a world map centered at 0° latitude, coloring Peru and Nigeria without using GeoPackage files

# Set output file name
output_file="PN"

# Set the projection (Mollweide projection centered at 0° latitude)
proj="-JW0/10c"

# Set the region to cover the entire world
region="-R-180/180/-90/90"

# Create the base map with coastlines and country borders
gmt begin $output_file png
  gmt coast $proj $region -B -N1 -W1 -Dl -A10000 -Sskyblue -Ggray

  # Color Peru (ISO 3166-1 alpha-3 code: PER)
  echo "PER" | gmt coast  -E+gred -W0.25p 

  # Color Nigeria (ISO 3166-1 alpha-3 code: NGA)
  echo "NGA" | gmt coast  -E+ggreen -W0.25p 

gmt end show
