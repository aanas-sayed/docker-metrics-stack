from fastapi import FastAPI, Request
from prometheus_client import Summary, Counter, make_asgi_app
from starlette.middleware.base import BaseHTTPMiddleware
import random
import asyncio
import time

# Define metrics
REQUEST_TIME = Summary(
    "request_processing_seconds", "Time spent processing request", ["endpoint"]
)


# Define custom middleware to count requests
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Measure time taken for request processing
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        if request.url.path != '/metrics/':
            # Observe the time taken by each request
            REQUEST_TIME.labels(request.url.path).observe(process_time)
        return response


# Create app
app = FastAPI(debug=False)

# Apply the metrics middleware
app.add_middleware(MetricsMiddleware)


# Create endpoints
@app.get("/")
def hello_world():
    return "Hello, World!"


@app.get("/slow_endpoint")
async def slow_endpoint():
    # Simulate some slow processing
    await asyncio.sleep(random.random())
    return "Slow endpoint processed!"


@app.get("/fast_endpoint")
async def fast_endpoint():
    return "Fast endpoint processed!"


# Metrics are usually exposed over HTTP, to be read by the Prometheus server.
# The easiest way to do this is via start_http_server
#   from prometheus_client import start_http_server
#   start_http_server(8000)
# Alternatively, add prometheus asgi middleware to route /metrics requests
# using other libraries e.g. FastAPI.
# https://prometheus.github.io/client_python/exporting/
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
