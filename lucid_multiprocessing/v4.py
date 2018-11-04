# Logging

from time            import sleep
from logging         import INFO, DEBUG
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger

def add_500_lock(total, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()

def sub_500_lock(total, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()

if __name__ == '__main__':
    total = Value('i', 500) # 'i' is to denote integer and 500 as value
    print("VALUE OBJ : ", total)

    lock  = Lock()

    # Logging setup
    log_to_stderr() # It says go ahead and print all the logging information to the terminal as we run this code.
    # Now we'll create a logger object
    logger = get_logger()
    logger.setLevel(DEBUG) # this is essentially telling the logger what level do we actually want to see the information.


    add_process = Process(target=add_500_lock, args=(total, lock))
    sub_process = Process(target=sub_500_lock, args=(total, lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()

    print(total.value)
