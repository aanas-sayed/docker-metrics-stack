#!/bin/bash

set -e  # Exit immediately on error

# Define the paths to your Docker Compose files (same as compose-up.sh)
COMPOSE_FILE="example_apps/docker-compose.yml"

# Define an array of rest api servers
rest_servers=("rest-api-server-1" "rest-api-server-2" "rest-api-server-3" "rest-api-server-4" "rest-api-server-5")

# Choose a random index from the array
random_index=$(( $RANDOM % ${#rest_servers[@]} ))

# Get the name of the randomly selected rest api server
selected_server=${rest_servers[$random_index]}

# Kill the selected server container
docker compose -f $COMPOSE_FILE kill $selected_server
