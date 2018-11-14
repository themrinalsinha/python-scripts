import asyncio
from time import time

async def find_divisibles(xrange, div_by):
    print('\nFinding num in range {} divisible by {}'.format(xrange, div_by))
    located = []
    for i in range(xrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.000000001)

    print('Done w/ nums in range {} divisible by {}'.format(xrange, div_by))
    return located

async def main():
    div_1 = loop.create_task(find_divisibles(200000000, 30))
    div_2 = loop.create_task(find_divisibles(40000, 60))
    div_3 = loop.create_task(find_divisibles(600000, 10))
    await asyncio.wait([div_1, div_2, div_3])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
    loop.close()
