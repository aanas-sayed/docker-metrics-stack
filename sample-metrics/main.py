from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """An example function that takes some time."""
    print(f"Request called, sleeping for {t} seconds")
    time.sleep(t)

# Similarly ...
NUM_USERS = Gauge('concurrent_users', 'Number of concurrent users')

NUM_USERS.inc(50)

def handle_user_connection():
    """Another example function that increments or decrements the number of concurrent users."""
    # Logic to handle user connection and update NUM_USERS metric
    NUM_USERS.inc(random.randint(0,2))  # Increment the gauge by random int for each new user connection
    # ... (user interaction logic)
    NUM_USERS.dec(random.randint(0,1))  # Decrement the gauge by random int when the user disconnects

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        handle_user_connection()
