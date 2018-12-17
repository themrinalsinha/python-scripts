# # Asyncio premitive of LOCK.

# import asyncio
# import random
# import time

# async def myWorker(lock):
#     print('Attempting to attain lock')
#     with await lock:
#         print('Currently locked...')
#         time.sleep(2)
#     print('Unlocked from critical section...')

# async def main():
#     lock = asyncio.Lock()
#     await asyncio.wait([myWorker(lock), myWorker(lock)])

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# print('\nAll workers completed...')
# loop.close()


# ======================================================
# Queue

import asyncio
import time

async def newsProducer(myQueue):
    while True:
        await asyncio.sleep(1)
        print('Putting new item onto queue...')
        await myQueue.put(random.randint(1, 5))


async def newsConsumer(id, myQueue):
    while True:
        print('Consumer: {} attempting to get from queue'.format(id))
        item = await myQueue.get()
        if item is None:
            break
        print('Consumer: {} consumed article with id: {}'.format(id, item))

async def main(loop):
    myQueue = asyncio.Queue(loop=loop, maxsize=10)
    await asyncio.wait([newsProducer(myQueue), newsConsumer(1, myQueue), newsProducer(myQueue), newsConsumer(2, myQueuee)])


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print('\nAll workers completed...')
loop.close()
