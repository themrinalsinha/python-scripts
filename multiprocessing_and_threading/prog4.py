# Sharing data between two processes using array and value in python

from multiprocessing import Process, Queue
from time            import sleep

result_1 = []

def calc_square(numbers):
    global result_1
    for num in numbers:
        sleep(0.5)
        result_1.append(num ** 2)
        print('Square : {}'.format(num ** 2))
    print('Inside process : {}'.format(str(result_1)))

numbers = [3, 6, 3, 1, 6, 7, 9]
process_1 = Process(target=calc_square, args=(numbers,))

process_1.start()
process_1.join()
print('Outer process : {}'.format(str(result_1)))

# ASSUME : """
# process 1 : Main Program : result = []
# process 2 : Child Process (calc_square) : result = [4, 9, 2, 5]
# Now how we can share data between two process, the answer is to use shared memory,
# Here the memory lives outside the processes
# """

# Process - 2
def calc_square_2(numbers, queue):
    for num in numbers:
        sleep(0.5)
        queue.put(num ** 2)
        print('Square : {}'.format(num ** 2))

numbers = [2, 4, 6, 7, 8, 8]
queue = Queue()
process_2 = Process(target=calc_square_2, args=(numbers, queue))
process_2.start()
process_2.join()

while queue.empty() is False:
    print('Outer Process : {}'.format(str(queue.get())))

# # NOTE:
# Multiprocessing queue:
# import multiprocessing
# q = multiprocessing.Queue()
# -> Live in shared memory.
# -> Used to share data between proceses.

# Queue Module:
# import Queue
# q = queue.Queue()
# -> Lives in in-process memory
# -> Used to share data between threads