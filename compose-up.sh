#!/bin/bash

set -e  # Exit immediately on error

# Define the paths to your Docker Compose files
METRICS_STACK_COMPOSE_FILE="docker-compose.yml"
EXAMPLE_APPS_PYTHON_COMPOSE_FILE="example_apps/docker-compose-python.yml"
EXAMPLE_APPS_GO_COMPOSE_FILE="example_apps/docker-compose-go.yml"

# Function to start Docker Compose stack with given compose file and extra arguments
start_compose_stack() {
    local COMPOSE_FILE="$1"
    echo "Starting Docker Compose stack from: $COMPOSE_FILE"
    docker compose -f "$COMPOSE_FILE" up -d "${@:2}"
}

# Start the metrics Docker Compose stack
start_compose_stack "$METRICS_STACK_COMPOSE_FILE" "${@}"

# Prompt user to choose between GO and PYTHON
echo "Which example would you like to run? Enter 'GO' or 'PYTHON':"
read -r EXAMPLE_CHOICE

# Wait for the first stack to be healthy (optional)
docker compose -f "$METRICS_STACK_COMPOSE_FILE" ps | grep -v Exit | wc -l

# Start the second Docker Compose stack
case "$EXAMPLE_CHOICE" in
    "GO")
        start_compose_stack "$EXAMPLE_APPS_GO_COMPOSE_FILE" "${@}"
        ;;
    "PYTHON")
        start_compose_stack "$EXAMPLE_APPS_PYTHON_COMPOSE_FILE" "${@}"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo "Both Docker Compose stacks started in detached mode."

exit 0
