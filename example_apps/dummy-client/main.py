import aiohttp
import asyncio

BASE_URL = "http://nginx:8080"

# Define the endpoints to request
ENDPOINTS = ["/slow_endpoint", "/fast_endpoint"]

async def request_endpoint(session, endpoint, frequency):
    while True:
        async with session.get(BASE_URL + endpoint) as response:
            response_text = await response.text()
            print(f"Requested {endpoint} from {BASE_URL}, Response: {response_text}")
        await asyncio.sleep(frequency)

async def main():
    async with aiohttp.ClientSession() as session:
        slow_tasks = [request_endpoint(session, ENDPOINTS[0], 0.1) for _ in range(100)] 
        fast_tasks = [request_endpoint(session, ENDPOINTS[1], 0.05) for _ in range(1000)]
        await asyncio.gather(*slow_tasks, *fast_tasks)

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
