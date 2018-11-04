# Pool:
# One can create a pool of processes which will carry out tasks submitted to it with the Pool class.
#
# A process pool object which controls a pool of worker processes to which jobs can be submitted.
# It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.

from time            import time
from multiprocessing import Pool

def sum_square(number):
    add = 0
    for i in range(number):
        add += i ** 2
    return add

def sum_square_with_mp(numbers):
    start_time = time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()
    end_time = time() - start_time
    print('Processing {} took {} time using multiprocessing.'.format(len(numbers), end_time))

def sum_square_no_mp(numbers):
    start_time = time()
    result = []
    for i in numbers:
        result.append(sum_square(i))
    end_time = time() - start_time
    print('Processing {} took {} time not using multiprocessing.'.format(len(numbers), end_time))

if __name__ == '__main__':
    # We'll create a pool object
    numbers = range(10000)

    sum_square_no_mp(numbers)
    sum_square_with_mp(numbers)
