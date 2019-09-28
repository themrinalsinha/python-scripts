# Futures in asyncio are very much similar to the Future objects you would see within
# Python ThreadPoolExecutors or ProcessPoolExecutors and tt follows an almost identical
# implementation. Future objects are created with the intention that they will eventually
# be given a result some time in the future, hence the name. This is beneficial as it means
# that within your Python program you can go off and perform other tasks whilst you are
# waiting for your Future to return a result.

# Thankfully working with Futures in asyncio is relatively easy thanks to the ensure_future()
# method which takes in a coroutine and returns the Future version of that coroutine.

import asyncio

# Define a coroutine that takes in a future
async def myCoroutine(future):
    # simulate some 'work'
    await asyncio.sleep(1)
    # set the result of our future object
    future.set_result("My Coroutine-turned-future has completed")

async def main():
    # define a future object
    future = asyncio.Future()
    # wait for the completion of our coroutine that we've
    # turned into a future object using the ensure_future() function
    await asyncio.ensure_future(myCoroutine(future))
    # Print the result of our future
    print(future.result())

# Spin up a quick and simple event loop
# and run until completed
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# If you were to run this you should see that our program successfully
# turns our coroutine into a future object and prints out the result.

