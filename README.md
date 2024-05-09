# Metrics Stack: Deploying Grafana with Common Metrics Services

This guide details setting up a metrics stack with Grafana preconfigured dashboards using Docker Compose. This is ideal for prototyping or learning purposes as it allows for quick deployment of the entire stack required for basic metrics.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Starting Services

- Run `docker compose up`.

## Accessing Grafana

- Navigate to http://localhost:3000 (assuming default port) in your web browser to access the Grafana UI.
Your preconfigured dashboards should be available within Grafana.

## Additional Notes

- This is an incomplete, unstable project at this stage.
- This approach keeps your dashboard files organized and easily accessible outside the container.
- You can add or remove dashboard JSON files from the ./grafana_dashboards directory to manage your available dashboards.

For further information on Grafana provisioning or dashboard creation, refer to the official Grafana documentation: https://grafana.com/docs/grafana/latest/