import asyncio
import logging

logging.basicConfig(format="%(asctime)s %(message)s", datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

async def sleeper(name, delay, repeat):
    for i in range(1, repeat + 1):
        log.info(f"{name}: START ({i}/{repeat}) wait: {delay}s")
        await asyncio.sleep(delay)
        log.info(f"{name}: END ({i}/{repeat}) wait: {delay}s")
    return name

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    futr = asyncio.gather(sleeper("A", 6, 1),
                          sleeper("B", 2, 3),
                          sleeper("C", 0.5, 12))
    log.info("main: START run_until_complete")
    loop.run_until_complete(futr)
    log.info("main: END   run_until_complete")
