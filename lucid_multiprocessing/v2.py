# Refer v1.py for detailed description

from os              import getpid
from time            import sleep
from multiprocessing import Process, current_process

def _square(nums):
    # print('OS assigned PID : {}'.format(getpid()))
    # print('Current Process name : {}'.format(current_process().name))
    for n in nums:
        print('Result : {}\n'.format(n ** 2))
        sleep(0.5)

if __name__ == '__main__':
    process_list = []
    # num = [90, 23, 1, 4, 98, 0]
    num = range(100)
    for n in range(50):
        process = Process(target=_square, args=(num,))
        process_list.append(process)
        process.start()
    # Here instead of looping across numbers we create a loop which run across all the processes.
    # this time we are passing the list of numbers to the function. we appeded all our processes to the process list.

    # We are going to use the join method which is available to proccess objects.
    # and essentially what is allows us to do is to wait for all the processes that we started to be complated before we
    # run any subsquient code. So before we print our print statement that says processes completed
    # we'll make sure all the processes are completed. So in order to do so..
    for p in process_list:
        p.join()

    print("Multiprocessing completed!")
