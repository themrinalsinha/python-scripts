from asyncio import sleep, get_event_loop, ensure_future

async def myCoroutine():
    while True:
        await sleep(1)
        print('My Coroutine...')

async def secondCoroutine():
    while True:
        await sleep(1)
        print('Second Coroutine...')

loop = get_event_loop()

try:
    ensure_future(myCoroutine())
    ensure_future(secondCoroutine())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print('\nClosing loop\n')
    loop.close()
