#!/bin/bash

set -e  # Exit immediately on error

# Define the paths to your Docker Compose files (same as compose-up.sh)
EXAMPLE_APPS_PYTHON_COMPOSE_FILE="example_apps/docker-compose-python.yml"
EXAMPLE_APPS_GO_COMPOSE_FILE="example_apps/docker-compose-go.yml"

# Define an array of rest api servers
rest_servers=("rest-api-server-1" "rest-api-server-2" "rest-api-server-3" "rest-api-server-4" "rest-api-server-5")

# Choose a random index from the array
random_index=$(( $RANDOM % ${#rest_servers[@]} ))

# Get the name of the randomly selected rest api server
selected_server=${rest_servers[$random_index]}

# Prompt user to choose between GO and PYTHON
echo "Which example did you run? Enter 'GO' or 'PYTHON':"
read -r EXAMPLE_CHOICE

# Kill the selected server container
case "$EXAMPLE_CHOICE" in
    "GO")
        docker compose -f "$EXAMPLE_APPS_GO_COMPOSE_FILE" kill $selected_server
        ;;
    "PYTHON")
        docker compose -f "$EXAMPLE_APPS_PYTHON_COMPOSE_FILE" kill $selected_server
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

