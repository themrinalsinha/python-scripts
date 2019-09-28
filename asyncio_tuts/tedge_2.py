# Coroutines:
# So these coroutines are essentially lightweight versions of your
# more traditional threads. By using these we essentially enable
# ourselves to write asynchronous programs that are very similar
# to threads but they run on top of a single thread. We can
# define coroutines in 2 distinct ways.

import asyncio

async def myFunc1():
    print('Coroutine 1')

@asyncio.coroutine
def myFunc2():
    print('Coroutine 2')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myFunc1())
    loop.run_until_complete(myFunc2())
    loop.close()