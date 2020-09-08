import asyncio
import aiohttp
import aiofiles

async def write_genre(file_name):
    """
    Uses generator from binaryjazz.us to write random
    genre to the name of the given file
    """

    async with aiohttp.ClientSession() as session:
        async with session.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/") as response:
            genre = await response.json()

    async with aiofiles.open(file_name, "w") as new_file:
        print(f"Writing '{genre}' to '{file_name}'...")
        await new_file.write(genre)

"""
For those not familiar with the async/await syntax that can be found in many other modern languages,
async declares that a function, for loop, or with statement must be used asynchronously. To call an
async function, you must either use the await keyword from another async function or call create_task()
directly from the event loop, which can be grabbed from asyncio.get_event_loop() -- i.e., loop = asyncio.get_event_loop().

Additionally:
    -> async with : allows awaiting async responses and file operations.
    -> async for : (not used here) iterates over an asynchronous stream.
"""

async def main():
    tasks = []
    for i in range(5):
        tasks.append(write_genre(f"./data/async_new_file_{i}.txt"))
    await asyncio.gather(*tasks)
asyncio.run(main())

"""
As you can see, we've declared it with "async." We then create an empty list called "tasks" to house our
async tasks (calls to Genrenator and our file I/O). We append our tasks to our list, but they are not
actually run yet. The calls don't actually get made until we schedule them with await asyncio.gather(*tasks).
This runs all of the tasks in our list and waits for them to finish before continuing with the rest of our program.
Lastly, we use asyncio.run(main()) to run our "main" function. The .run() function is the entry point for our program,
and it should generally only be called once per process.
"""
