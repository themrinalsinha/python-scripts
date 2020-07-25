from random import randint
import time
import asyncio
from time import sleep

# syncronous function that takes 3.00 seconds
def randn():
    time.sleep(3)
    return randint(1, 30)

async def generatevalue():
    await asyncio.sleep(3)
    return randint(1, 30)

async def get_result():
    return await asyncio.gather(*(generatevalue() for _ in range(1000)))

if __name__ == "__main__":
    start = time.perf_counter()
    # this will take around 9 seconds to run all 3 calls
    r1 = randn()
    r2 = randn()
    r3 = randn()
    print(r1)
    print(r2)
    print(r3)
    elapsed = time.perf_counter() - start
    print(f"randn function took: {elapsed:0.2f} seconds")


    start = time.perf_counter()
    print(asyncio.run(get_result()))
    elapsed = time.perf_counter() - start
    print(f"async randn function took: {elapsed:0.2f} seconds")
