#!/bin/bash

# Define the color palette file for coloring the countries
gmt makecpt -Cjet -T0/10/1 -D > colors.cpt

# Create a simple world map using the Hammer projection centered on 0 longitude
gmt begin world_map png
  # Plot the coastlines, land areas, and ocean
  gmt coast -Rg -JH0/15c -Baf -W0.25p -Dc -A5000 -Glightgray -Slightblue

  # Get the list of all countries from the DCW dataset
  gmt coast -E+g -M > all_countries.txt

  # Randomly select 10 countries from the list
  selected_countries=$(shuf -n 10 all_countries.txt)

  # Plot each selected country with a random color from the color palette
  count=0
  for country in $selected_countries; do
    gmt coast -E${country}+g -Gp${count} -W0.25p
    count=$((count + 1))
  done
gmt end # show

# Clean up temporary files
#rm all_countries.txt colors.cpt
