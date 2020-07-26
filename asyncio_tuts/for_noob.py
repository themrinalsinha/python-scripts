# SOURCE: https://www.youtube.com/watch?v=6kNzG0T44SI

# Generator: A function that produces a sequence of result instead of single value, they contain one or more yield statement,
#            when you call a generator function a generator object is created but that object remains in paused state, it
#            doesn't just start running automatically.

# Example of generator
import asyncio
from types import coroutine


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(10):
    print(i)

# if you assign this function to some variable
x = countdown(5)
# normally, we expect a result here we can see that we have the generator object itself
# in a suspended state, calling "next" on it will execute every line upto and including
# our first yield but nothing further when we run next again
print(x) # ---> just prints the generator object
print(next(x)) # --> 5
print(next(x)) # --> 4
print(next(x)) # --> 3
print(next(x)) # --> 2
print(next(x)) # --> 1
# print(next(x)) # --> STOP ITERATION ERROR THROWN. since there is nothing more to yeild.
# --------------------------------------------------------------------------------------

# Generators to co-routines
# PEP-342 introduced yield as an expression, which meant that you could now use yield
# on the right side of an assignment, if you knew nothing of co-routine look example below
# Example of co-routine
def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)
# now the confusion arises if your only experience to date has been of the yield keyword in
# generator expression and generator functions, if you use yield more generally then you
# create a co-routine which do more than just generate values, but can also consume values
# sent to it, when you call a co-routine nothing happens..
f = finder('python')
print(f) # --> when we called this nothing happend actually, it actually just a generator object just as before.

# we can send values in our generator function using "send" method.
# So, let's send in some text including the word python as we've done here, the way this suppose to work is that
# the string that we've sent in becomes a sign to input text and then seeing as X is python and python is in this new
# string that we've passed in that string will be printed to the terminal.

# f.send("some text including python")

# and we just saw in the above example that no lines will get executed unless we call "next()" method on it.
# so, when you try to send a value like we are trying to send above eg:f.send("some text including python") it
# will throw an error TypeError: can't send non-None value to a just-started genetator
# so, we've to first send a None value this is called "Priming"
# Either: object.send(None) Or: next(object)
# either of it should be done at the very beginning.
f.send(None) # or next(f)
f.send("some text including python")
f.close()

# OR
g = finder("pattern")
next(g) # or g.send(None)
g.send("I like the pattern on your shirt")
g.close()

# the co-routine "close()" method shuts it down as it could otherwise run indefinitely and indeed this is what the
# interpreter calls during garbage collection, you can catch this tough with normal exception handling of the generator exit exception
# and this is if you need to implement specific cleanup code furthermore you can also raise exception inside a corouting with throw() method.

# g.throw(AttributeError, "Doesn't have to be an AttributeError, can be anything...")

# Now, that we've bit clarity about how generator works.

# Despite this similarity, co-routines are basicaly two distinct concepts generators, proudce data for iteration co-routing, it tend to consume values,
# co-routines are consuers of data.

def yielder(source):
    yield from source

def _yielder(source):
    for _ in source:
        yield _

_ = _yielder(range(10))
print(next(_))
print(next(_))
print(next(_))
print(next(_))

# there is a use of having yield to produce a value in a co-routine but it's not tied to iteration, if you've come across yield from before then you might
# have seen it explained away as merely being shorthand, for yielding values from an iterator, including other generators but it's real use lies in allowing
# delegation to a sub generator or in other words any next or send can be passed on to nested generators, acting as a tunnel that passed data back and forth
# and so this is at the heart of how co-routines operates, from python 3.5+ the preferred way on using asyncio is async/await function.

def greet(name):
    return "Hello " + name

async def _greet(name):
    return "Hello " + name

print(type(greet))
print(type(_greet))

# if we check the type of both our functions like greet or _greet we can see that both are type <function>
# Now, let's see what happens when we try to run them.
print(greet("Mrinal"))

# def run(coruotine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

async def print_msg():
    return await _greet("Mrinal Sinha")

asyncio.run(print_msg())

# an async fibonacci numbers function
async def fib(n):
    if n < 2:
        return 1
    else:
        return await fib(n - 1) + await fib(n - 2)

async def main():
    for n in range(10):
        print(await fib(n))

asyncio.run(main())
# =================================================
print("\nTESTING SYNC FUNCTION\n\n")

import time

def count():
    time.sleep(3)

def main():
    for _ in range(3):
        count()

t = time.perf_counter()
main()
e = time.perf_counter() - t
print(f"Time taken : {e:0.2f}")

print("\nTESTING ASYNC FUNCTION\n\n")

async def count():
    await asyncio.sleep(3)

async def main():
    await asyncio.gather(*(count() for _ in range(3)))

t = time.perf_counter()
asyncio.run(main())
e = time.perf_counter() - t
print(f"Time taken : {e:0.2f}")