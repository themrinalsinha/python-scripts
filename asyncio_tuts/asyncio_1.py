# from asyncio import get_event_loop, coroutine

# async def my_coroutine():
#     print('Simple eventloop example.')

# def main():
#     # Define an instance of an event loop
#     loop = get_event_loop()

#     # Tell this eventloop to run until all the tasks assigned
#     # to it are completed. In this example just the execution
#     # of my_coroutine() coroutine.
#     loop.run_until_complete(my_coroutine())
#     # Tidying up our loop by calling close()

# if __name__ == '__main__':
#     main()

# # Coroutines -
# # So these coroutines are essentially lightweight versions of your
# # more traditional threads. By using these we essentially enale ourselves
# # to write asynchronous programs that are very similar to threads but they
# # run on top of a single thread.
# # We can define thred in 2 distinct ways.

# import asyncio

# async def myfunc_1():
#     print('Co-routine__1')

# @coroutine
# def myfunc_2():
#     print('Co-routine__2')

from asyncio import coroutine, get_event_loop

@coroutine
def myCoroutine():
    print('Simple event loop')

def main():
    loop = get_event_loop()
    loop.run_until_complete(myCoroutine())
    loop.close()

main()
