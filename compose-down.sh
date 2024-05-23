#!/bin/bash

set -e  # Exit immediately on error

# Define the paths to your Docker Compose files (same as compose-up.sh)
METRICS_STACK_COMPOSE_FILE="docker-compose.yml"
EXAMPLE_APPS_COMPOSE_FILE="example_apps/docker-compose-python.yml"

# Function to stop and remove containers from a given compose file
stop_and_remove_containers() {
    local COMPOSE_FILE="$1"
    echo "Stopping and removing containers from: $COMPOSE_FILE"
    docker compose -f "$COMPOSE_FILE" down "${@:2}"
}

# Stop and remove services from the second stack
stop_and_remove_containers "$EXAMPLE_APPS_COMPOSE_FILE" "${@}"

# Stop and remove services from the first stack
stop_and_remove_containers "$METRICS_STACK_COMPOSE_FILE" "${@}"

echo "Both Docker Compose stacks stopped and removed."

exit 0
