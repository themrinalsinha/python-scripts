# Now we'll make multiprocessing Queue class to
# communicate between different processes.

# Queue helps us to instantiate queue data structure from multiprocessing module
# It'll allow us to share that ds among various processes. So we can put things
# into this queue and also take it out of the queue.

from multiprocessing import Process, Queue
# with Process we'll create the function for both square and cube function.


def _square(numbers, queue):
    for i in numbers:
        queue.put(i ** 2)

def _cube(numbers, queue):
    for i in numbers:
        queue.put(i ** 3)

if __name__ == '__main__':
    numbers = range(5)
    queue   = Queue()

    square_process = Process(target=_square, args=(numbers, queue))
    cube_process   = Process(target=_cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())
