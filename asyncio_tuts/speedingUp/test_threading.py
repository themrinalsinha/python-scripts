import json
import threading
from urllib.request import urlopen, Request

def write_genre(file_name):
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """

    req = Request("https://binaryjazz.us/wp-json/genrenator/v1/genre/", headers={'User-Agent': 'Mozilla/5.0'})
    genre = json.load(urlopen(req))

    with open(file_name, "w") as new_file:
        print(f'Writing "{genre}" to "{file_name}"...')
        new_file.write(genre)

threads = []
for i in range(5):
    thread = threading.Thread(
        target=write_genre,
        args=[f"./data/new_file_{i}.txt"]
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

"""
We first start with a list. We then proceed to iterate 5 times, creating a new thread each time.
Next, we start each thread, append it to our "threads" list, and then iterate over our list one
last time to join each thread.

:CREATING THREADS IN PYTHON:
----------------------------
To create a new thread, use threading.Thread(). You can pass into it the kwarg (keyword argument)
target with a value of whatever function you would like to run on that thread. But only pass in
the name of the function, not its value (meaning, for our purposes, write_genre and not write_genre()).
To pass arguments, pass in "kwargs" (which takes a dict of your kwargs) or "args"
(which takes an iterable containing your args -- in this case, a list).

Creating a thread is not the same as starting a thread, however. To start your thread,
use {the name of your thread}.start(). Starting a thread means "starting its execution."

Lastly, when we join threads with thread.join(), all we're doing is ensuring the thread
has finished before continuing on with our code.
"""
