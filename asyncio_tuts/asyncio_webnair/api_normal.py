import time
from requests import Session

def download_site(url, session):
    with session.get(url) as response:
        print(f"READ {len(response.content)} from {url}")

def download_all_sites(sites):
    with Session() as session:
        for url in sites:
            download_site(url, session)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 100

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"\nDownload {len(sites)} in {duration} seconds")