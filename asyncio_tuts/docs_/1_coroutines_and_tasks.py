# This outlines high-level asyncio APIs to work with coroutines and Tasks
# -----------------------------------------------------------------------

# COROUTINES
# it declared with the async/await syntax is the preferred way of writing asyncio application

import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('world\n\n')

asyncio.run(main())

# To actually run a coroutine, asyncio provides three main mechanism:
# - the asyncio.run() function to run the top-level entry point main() function
# - Awaiting on a coroutine. The following snippet of code will print "hello" after waiting
#   for 1 second, and then print "world" after waiting for another 2 seconds

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}\n\n")

asyncio.run(main())

# - The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks
# Let's modify the above example and run two say_after coroutines concurrently:
async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    # wait until both tasks are completed (should take around 2 sec)
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}\n\n")

asyncio.run(main())
# Note that expected output now shows that the snippet runs 1 second faster than before:

# AWAITABLES
# we say that an object is an awaitable object if it can be used in an await expression.
# Many asyncio APIs are designed to accept awaitables.

# There are three main types of awaitable objects:
# - coroutines
# - tasks
# - futures

# python coroutines are awaitables and therefore can be awaited from other coroutines
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but now waited, so it won't run at all
    nested()

    # Let's do it differently now and await it:
    result = await nested()
    print(result)

asyncio.run(main())

# Important: In this documentation the term coroutine can be used for two closely related concepts:
# - a coroutine function: as `async def` function.
# - a coroutine object: an object returned by calling a coroutine function

# Tasks
# Tasks are used to schedule coroutines concurrently.
# when a coroutine is wrapped into a Task with function like asyncio.create_task() the
# coroutine is automatically scheduled to run soon
import asyncio

async def nested():
    return 42

async def main():
    # schedule nested() to run soon concurrently with main()
    task = asyncio.create_task(nested())

    # task can now be used to cancel nested or can simply be
    # awaited to wait until it is complete
    await task

asyncio.run(main())
# ----------------------------------------------------------------------------------
