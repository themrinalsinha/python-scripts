import time
import asyncio
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 100

    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    end_time = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {end_time} seconds")