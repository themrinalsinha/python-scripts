# Lock in multiprocessing
# eg: bathroom is a shared resource but not more than one people can access it so we apply lock at that place.
# Similarly, lock is used when two processes try to use shared resources (Memory, Files, Databases etc.)

import time
import multiprocessing

def deposit(balance):
    print('In deposit...')
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance):
    print('In withdraw...')
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

balance = multiprocessing.Value('i', 200)
lock    = multiprocessing.Lock()
d = multiprocessing.Process(target=deposit, args=(balance,))
w = multiprocessing.Process(target=withdraw, args=(balance,))

d.start()
w.start()
d.join()
w.join()

print(balance.value)
# Here everytime we print we are going to get different result.
# You will get this sequencing error, it may be that withdraw will execute first and then deposit