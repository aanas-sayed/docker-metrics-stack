import requests
import time
import threading

# Define number of servers
NO_OF_SERVERS = 5

# Define the base URLs of your application servers
base_urls = []
for i in range(NO_OF_SERVERS):
    base_url = f"http://rest-api-server-{i}:8000"
    base_urls.append(base_url)

# Define the endpoints to request
ENDPOINTS = ["/", "/slow_endpoint", "/fast_endpoint"]


# Function to continuously request endpoints
def request_endpoints(base_url):
    while True:
        try:
            for endpoint in ENDPOINTS:
                response = requests.get(base_url + endpoint)
                print(
                    f"Requested {endpoint} from {base_url}, Response: {response.text}"
                )
            time.sleep(1)  # Adjust the interval between requests as needed
        except Exception as e:
            print(f"Error occurred: {e}")


# Start requesting endpoints for each server in separate threads
request_threads = []
for base_url in base_urls:
    request_thread = threading.Thread(target=request_endpoints, args=(base_url,))
    request_thread.start()
    request_threads.append(request_thread)

# Keep the main thread running
while True:
    time.sleep(1)
