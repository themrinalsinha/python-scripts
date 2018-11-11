import asyncio
import random
import time

async def my_routine(id):
    process_time = random.randint(1,10)
    await asyncio.sleep(process_time)
    print('Co-routine: {}, has successfully completed after {} seconds'.format(id, process_time))

async def temp_main():
    tasks = []
    for i in range(100):
        tasks.append(asyncio.ensure_future(my_routine(i)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(temp_main())
    loop.close()
    end_time = time.time() - start_time
    print('Total time taken : {} seconds'.format(end_time))
