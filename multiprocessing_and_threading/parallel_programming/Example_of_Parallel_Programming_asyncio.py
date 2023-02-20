import aiohttp
import asyncio
import timeit

BASE_URL = "https://httpbin.org/uuid"

def exctimer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print("\nTOTAL TIME: ", sum(runs) / len(runs))
    return wrapper

async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response["uuid"])

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, BASE_URL) for _ in range(100)]
        await asyncio.gather(*tasks)

@exctimer(1, 5)
def func():
    asyncio.run(main())
