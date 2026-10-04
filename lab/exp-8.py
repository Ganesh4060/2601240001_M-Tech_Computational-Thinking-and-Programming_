import asyncio
import aiohttp
import time

# Websites to crawl
URLS = [
    "https://example.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.google.com"
]

# Number of retry attempts
MAX_RETRIES = 3


# ---------------- SEQUENTIAL CRAWLER ----------------

def sequential_crawler():
    print("\n--- Sequential Web Crawler ---")

    start_time = time.perf_counter()

    for url in URLS:
        try:
            import requests

            response = requests.get(url, timeout=10)

            print(
                f"{url} -> Status: {response.status_code}"
            )

        except Exception as e:
            print(f"{url} -> Failed: {e}")

    end_time = time.perf_counter()

    return end_time - start_time


# ---------------- ASYNCHRONOUS CRAWLER ----------------

async def fetch(session, url):
    for attempt in range(1, MAX_RETRIES + 1):

        try:
            async with session.get(url, timeout=10) as response:

                await response.read()

                print(
                    f"{url} -> Status: {response.status}"
                )

                return response.status

        except Exception as e:

            print(
                f"{url} -> Attempt {attempt} failed"
            )

            if attempt < MAX_RETRIES:
                await asyncio.sleep(1)

    print(f"{url} -> Failed after {MAX_RETRIES} attempts")
    return None


async def asynchronous_crawler():

    print("\n--- Asynchronous Web Crawler ---")

    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:

        tasks = [
            fetch(session, url)
            for url in URLS
        ]

        await asyncio.gather(*tasks)

    end_time = time.perf_counter()

    return end_time - start_time


# ---------------- MAIN PROGRAM ----------------

async def main():

    sequential_time = sequential_crawler()

    async_time = await asynchronous_crawler()

    print("\n--- Performance Comparison ---")

    print(
        f"Sequential Time    : {sequential_time:.2f} seconds"
    )

    print(
        f"Asynchronous Time  : {async_time:.2f} seconds"
    )

    if async_time < sequential_time:
        print("Asynchronous crawler is faster.")

    else:
        print("Sequential crawler was faster in this run.")


if __name__ == "__main__":
    asyncio.run(main())