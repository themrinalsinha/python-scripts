# Coroutines declared with the async/await syntax is the preferred
# way of writing asyncio applications. For example, the following
# snippet of code (requires Python 3.7+) prints “hello”,
# waits 1 second, and then prints “world”:

import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
print("-" * 100)
# main() # --> RuntimeWarning: coroutine 'main' was never awaited

# To actually run a coroutine, asyncio provides three main mechanisms:
# - The asyncio.run() function to run the top-level entry point “main()” function (see the above example.)
# - Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second,
#   and then print “world” after waiting for another 2 seconds:
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(3, "hello, Mrinal Sinha")
    await say_after(3, "how are you ???????")
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
print("-" * 100)

# The asyncio.create_task() function to run coroutines concurrently
# as asyncio Tasks.
print("Running task conccurrently...")
async def main():
    task_1 = asyncio.create_task(
        say_after(3, "Hello, Mrinal Sinha")
    )

    task_2 = asyncio.create_task(
        say_after(3, "how are you ???????")
    )

    # wait until both tasks are completed
    print(f"started at {time.strftime('%X')}")
    await task_1
    await task_2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())