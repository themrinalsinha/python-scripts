# Asyncio allows you to easily write single-threaded concurrent programs that
# utilize something called coroutines, these coroutines are like a stripped down
# threads and don’t come with the same inherit performance issues that your
# full-fat threads would typically come with.

# Asyncio also does a very good job of abstracting away from us the complexities
# of things such as multiplexing I/O access over sockets and it also simplifies
# our jobs by providing an arsenal of synchronization primitives that enable us
# to make our programs thread-safe.

import asyncio

async def myCoroutine():
    print('Simple Event loop example')

def main():
    # Define an instance of event loop
    loop = asyncio.get_event_loop()
    # Tell this event loop to run until all the task assigned to it
    # are complete. In this example just the execution of our myCoroutine() coroutine.
    loop.run_until_complete(myCoroutine())
    # Tidying up our loop by calling close()
    loop.close()

if __name__ == '__main__':
    main()