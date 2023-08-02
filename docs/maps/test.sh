#!/bin/bash
# GMT script to create a world map centered at 0° latitude, coloring Peru and Nigeria

# Set output file name
output_file="Peru_Nigeria"

# Download country boundaries data
gmt gmtget @earth_relief_03m -R-180/180/-90/90

# Download GADM data for Peru and Nigeria (unzip it and place the .gpkg files in your working directory)
# Source: https://gadm.org/download_country_v3.html

# Set the projection (Mollweide projection centered at 0° latitude)
proj="-JW0/10c"

# Set the region to cover the entire world
region="-R-180/180/-90/90"

# Create the base map with coastlines and country borders
gmt begin $output_file png
  gmt coast $proj $region -B -N1 -W1 -Dl -A10000 -Sskyblue -Ggray

  # Plot and color Peru (using ISO 3166-1 alpha-3 code)
  gmt plot  -Gred -W0.25p -t60 "gadm36_PER.gpkg"  

  # Plot and color Nigeria (using ISO 3166-1 alpha-3 code)
  gmt plot  -Ggreen -W0.25p  -t60 "gadm36_NGA.gpkg"  

gmt end show
