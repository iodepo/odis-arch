#!/bin/bash

# Declare the array of objects
# objects=(item1 item2 item3 item4)  # Replace with your actual object names
#objects=(africaioc bmdc cioos edmerp edmo emodnet)
#objects=(inanodc invemardocuments invemarexperts invemarinstitutions invemartraining invemarvessels marinetraining medin nmdis obis obps oceanexpert oceanscape pdh pedp)
objects=(rda) # errors on final save

# Loop through the objects array
for object in "${objects[@]}"; do
  # Construct the command with object substitution
  command="python mdp.py --source \"s3://nas.local:54321/public/graphs/test1/${object}_release.nq\" --output \"./output/${object}.parquet\""

  # Execute the constructed command
  echo "Executing command: $command"  # Optional: Print the command for clarity
  start_time=$(date +%s)  # Get the current time in seconds

  eval $command

  end_time=$(date +%s)
  duration=$(echo "scale=2; ($end_time - $start_time) / 60" | bc) 
  echo "Time elapsed for ${object}: $duration minutes"
done

