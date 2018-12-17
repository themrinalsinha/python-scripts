from asyncio import sleep, ensure_future, gather, get_event_loop
from random  import randint

async def myCoroutine(id):
    process_time = randint(1, 5)
    await sleep(process_time)
    print('Coroutine: {} has successfully completed after {} seconds.'.format(id, process_time))

async def main():
    tasks = []
    for i in range(10):
        tasks.append(ensure_future(myCoroutine(i)))
    await gather(*tasks)

loop = get_event_loop()
loop.run_until_complete(main())
loop.close()
