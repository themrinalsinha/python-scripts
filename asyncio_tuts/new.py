async def hi():
    print('Hello')

o = hi()
print(o)
print(type(o))

# to inspect if it is a coroutine module
import inspect
print(inspect.iscoroutine(o))

# in ordder to run a co-routine function, you have to run it.
o.send(None) # initally you have to pass none
# the above send function will throw an error of StopIteration.
# So, now the question is how wee can prevent this error....
# we'll have to write our own event loop or use an exising one...

# the default event loop provided by the asyncio is asyncio.get_event_loop()
import asyncio

# get the default event loop and it has a function called run_until_complete
loop = asyncio.get_event_loop()
o = hi()
loop.run_until_complete(o) # pass your co-routine object to it...
# co-routines are generally driven by event loops to prevent errors...

# event loops basically drives the coroutines, now we've understood what async does...
# Now, let's understand what await keyword does...so coroutines are not suppose to block each other,
# the real purpose of it is to use with the IO operations. which can potentially block if you run it
# asynchronously....but async code will not block each other...

async def sleep():
    await asyncio.sleep(3)
    print('***')

o = sleep()
f = o.send(None)
print(f) # <Future pending>
print(type(f)) # <Future pending>
# Now you can see f is different from what we got earlier with o.
