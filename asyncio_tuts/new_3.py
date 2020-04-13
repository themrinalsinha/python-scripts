import asyncio
import logging

logging.basicConfig(format="%(asctime)s %(message)s", datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

async def grandfather():
    log.info(f"Grandfather: START")
    await father()
    log.info(f"Grandfather: END")

async def father():
    log.info(f"Father: START")
    await child()
    log.info(f"Father: END")

async def child():
    log.info(f"Child: START")
    print(f'inside child...')
    await asyncio.sleep(2)
    log.info(f"Child: END")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info('MAIN: START run_until_complete')
    loop.run_until_complete(grandfather())
    log.info('MAIN: END   run_until_complete')
