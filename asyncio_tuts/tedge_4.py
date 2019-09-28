# Multiple co-routines
# Let’s now try to take advantage of asyncio’s ability to run multiple
# coroutines concurrently. This will hopefully give you some idea as to
# how powerful asyncio is and how you can use it to effectively create
# incredibly performant Python programs running on a single-thread.

# Let’s start by creating a simple coroutine that takes in an id as its
# primary parameter. This will generate a random integer called process_length
# and wait for that length of time. It will then print out it’s id and how
# long it awaited for.

# Next within our main() method we will generate 10 tasks that and then await
# these tasks completion using the await asyncio.gather() function, passing
# in our list of tasks. Finally we’ll utilize the same event loop from the
# previous example in order to run our asyncio program.

import asyncio
import random

async def myCoroutine(id):
    process_time = 