import asyncio

async def sleeper(name, delay, repeat):
    for i in range(1, repeat + 1):
        await asyncio.sleep(delay)
    return name

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    futr = asyncio.gather(sleeper('A', 6, 1))
    loop.run_until_complete(futr)
