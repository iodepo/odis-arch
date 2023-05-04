#!/bin/bash

# Create a file with 10 random latitude and longitude points
echo "Longitude Latitude" > random_points.txt
for i in {1..10}; do
  # Generate random longitude between -180 and 180
  lon=$(awk -v min=-180 -v max=180 'BEGIN{srand(); print min+rand()*(max-min)}')
  # Generate random latitude between -90 and 90
  lat=$(awk -v min=-90 -v max=90 'BEGIN{srand(); print min+rand()*(max-min)}')
  echo "$lon $lat" >> random_points.txt
done

# Create a simple world map using the Hammer projection
gmt begin world_map2 png
  gmt coast -Rg -JH0/15c -Baf -W0.25p -Dc -A5000 -Glightgray -Slightblue
  # Plot the random points on the map
  gmt plot random_points.txt -Sc0.3c -Gred
gmt end show

# Clean up the temporary file
#rm random_points.txt

