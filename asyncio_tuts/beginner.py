# Source: https://www.youtube.com/watch?v=6kNzG0T44SI

# Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(10):
    print(i)
# or
print()
c = countdown(10)
print(c)       # generator in suspended state.
print(next(c)) # calling next will print the values.
print(next(c))
print(next(c))
print(next(c))
print()
# in the end when there is nothing left in the generator
# it will raise StopIteration exception.


def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)

f = finder('python')
print(f)
# f.send('hello welcome to the world of python') # the text that we send in will get assigned to input text but if we do that it will throw error
# we just saw above that when we call function, it is starts off in suspended state,
# it's only when we call next it executes the function.

# IMPORTANT
# This first step is called priming:
# Priming can be done either using either "object.send(None)" or "next(object)"
f.send(None)
f.send('Hello world')
f.send('my name is python')
f.send('hello python')

# another way
print()
g = finder('go')
next(g)
g.send('Hello gopal')
g.send('Hello you you..')

f.close()
g.close()
# if we don't close the generators, it will run indefinitely.
# =============================================================================

# methods meant for co-routines are sometimes described for generators.
# Generators and co-routines are basically two distinct concepts, generators
# produce data for iteration, coroutines tend to consume values, they are consumers of data

# there is use of having yield produces value in a coroutines, but its not tied to
# iteration

# def yielder(source):
#     yield from source

# def _yielder(source):
#     for _ in source:
#         yield _

# _ = _yielder(iterable)
# next(_)
# =============================================================================

def greet(name):
    return 'Hello ' + name

async def _greet(name):
    return 'Hello ' + name

print(greet)
print(_greet)

print(greet('Mrinal'))  # runs normally
# print(_greet('Mrinal')) # corouting object

def run(coroutine):
    try:
        return coroutine.send(None)
    except StopIteration as e:
        return e.value

async def main():
    print(await _greet('Mrinal'))

run(main())
print()

async def main():
    names = ['Alabama', 'Bristol', 'Calgary']
    for name in names:
        print(await _greet(name))

run(main())
print()


async def fib(n):
    if n < 2:
        return 1
    else:
        return await fib(n-1) + await fib(n-2)

async def main():
    for n in range(10):
        print(await fib(n))

run(main())
# ===========================================================

import time

print()

def count():
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)

def main():
    for i in range(3):
        count()

t = time.perf_counter()
main()
t2 = time.perf_counter() - t
print(f'Total time elapsed: {t2:0.2f} seconds')

# ====================================================
# Now we'll do the same thing using asyncio
import asyncio

async def count():
    await asyncio.sleep(1)
    print(1)
    await asyncio.sleep(1)
    print(2)
    await asyncio.sleep(1)
    print(3)

async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())
