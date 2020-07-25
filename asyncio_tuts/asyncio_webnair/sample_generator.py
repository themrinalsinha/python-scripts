import time
import asyncio

def odd(start, stop):
    for odd in range(start, stop+1, 2):
        yield odd

async def square_odd(start, stop):
    for i in odd(start, stop):
        yield i

async def main():
    start = time.perf_counter()
    for x in odd(1, 1000000):
        print(x)
    elapsed = time.perf_counter() - start

    start1 = time.perf_counter()
    async for i in square_odd(1, 1000000):
        print(i)
    elapsed1 = time.perf_counter() - start1

    print(f"Generator took {elapsed:0.2f} seconds")
    print(f"Async Generator took {elapsed1:0.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())