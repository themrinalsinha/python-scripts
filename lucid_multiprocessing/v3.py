# LOCKS
# A lock or mutex is a synchronization mechanism for enforcing
# limits on access to a resource in an environment where there
# are many threads of execution.

from time            import sleep
from multiprocessing import Process, Lock, Value

# # CASE 1 : Regular function
# def add_500_no_mp(value):
#     for i in range(100):
#         sleep(0.01)
#         value += 5
#     return value

# def sub_500_no_mp(value):
#     for i in range(100):
#         sleep(0.01)
#         value -= 5
#     return value

# if __name__ == '__main__':
#     total = 500
#     print(total)

#     total = add_500_no_mp(total)
#     print(total)

#     total = sub_500_no_mp(total)
#     print(total)


# # CASE 2 : Here we are going to use Value() function to create a shared resourse.
# def add_500_no_lock(total):
#     for i in range(100):
#         sleep(0.01)
#         total.value += 5

# def sub_500_no_lock(total):
#     for i in range(100):
#         sleep(0.01)
#         total.value -= 5

# if __name__ == '__main__':
#     # total = 500 : Now rather then saying total value we'll create a share Value
#     # It take two arguments one datatype and another is value for it.
#     total = Value('i', 500) # 'i' is to denote integer and 500 as value

#     print("VALUE OBJ : ", total)
#     # Now we want to make use of this shared variable 'total'
#     # and the function will manipulate the shared resource and it'll cretea the process for each resource
#     # will run then and join them and we'll see what do we get in the end.

#     # now that we'll be passing value object the these function.
#     # In order to access the acutual value we've to use .value property.

#     add_process = Process(target=add_500_no_lock, args=(total,))
#     sub_process = Process(target=sub_500_no_lock, args=(total,))
#     # Now that we've created our two process for addition and subtracton
#     # for our two shared resource object. Now we'll just start...

#     add_process.start()
#     sub_process.start()

#     # Now to make sure that these processes are complated we need to run join().
#     add_process.join()
#     sub_process.join()

#     # Now in the end we'll print total.value() to see what we've run.
#     print(total.value)
#     # when we run it everytime we'll get different result since we initiated the process
#     # randomly here we are not defining the it should complete the addition process first
#     # and then run the subtractioon process. so in order to do so we need to user LOCK


# CASE 3 : Here we'll user Lock function to make sure that we'll first complete the first process and then the second one
def add_500_lock(total, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()
        # In order to make use of the lock, before we neen to add we'll acquire the lock
        # and once it's done we'll release the lock

def sub_500_lock(total, lock):
    for i in range(100):
        sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()

if __name__ == '__main__':
    total = Value('i', 500) # 'i' is to denote integer and 500 as value
    print("VALUE OBJ : ", total)

    # First, we'll create a Lock object
    # then we'll modify the function to take a lock objects
    lock  = Lock()

    add_process = Process(target=add_500_lock, args=(total, lock))
    sub_process = Process(target=sub_500_lock, args=(total, lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()

    print(total.value)



