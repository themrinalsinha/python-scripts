import asyncio
import sys

loop = asyncio.get_event_loop()
print(loop)
asyncio.set_event_loop(loop)

if sys.platform != 'win32':
    watcher = asyncio.get_child_watcher()
    watcher.attach_loop(loop)


# Here is evidence that a loop is bound to a thread.
import asyncio
from threading import Thread

class LoopShowerThread(Thread):
    def run(self):
        try:
            loop = asyncio.get_event_loop()
            print(loop)
        except RuntimeError:
            print('No event loop!')

loop = asyncio.get_event_loop()
print(loop)

thread = LoopShowerThread()
thread.start()
thread.join()

# In essence, this code contains a threading.Thread subclass definition
# that fetches the loop policy scoped loop.
# Since we do not alter the DefaultLoopPolicy here, which holds one
# thread local loop, we can see that just calling asyncio.get_event_loop
# inside the LoopShowerThread is not enough to get a loop instance in a
# thread before instantiating it. The reason is that asyncio.get_event_loop
# simply creates a loop on the main thread.
