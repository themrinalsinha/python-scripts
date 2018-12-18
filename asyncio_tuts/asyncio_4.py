from time    import sleep
from asyncio import ensure_future, get_event_loop

async def myTask():
    sleep(1)
    print('Processing Task')

async def myTaskGenerator():
    for i in range(5):
        ensure_future(myTask())

loop = get_event_loop()
loop.run_until_complete(myTaskGenerator())
print("\nCompleted all tasks\n")
loop.close()
