from time            import sleep
from multiprocessing import Process

square_result = []

def calc_square(numbers):
    print('Calculating Square numbers')
    global square_result
    for n in numbers:
        sleep(0.5)
        print('Square : ', n ** 2)
        square_result.append(n ** 2)
    print('Result : ', str(square_result)) #You can print with process.

if __name__ == "__main__":
    arr = [2, 4, 7, 5, 1]
    process_1 = Process(target=calc_square, args=(arr,))

    # Starts the process.
    process_1.start()

    # Wait till the process stops
    process_1.join()

    print('Done!')

# When you create a new process it will create a copy of square result,
# Every process has its own address space (Virtual Memory). Thus program
# variable as not shared between two process. You need to use interprocess
# communication (IPC) technique if you want to share data between two process. 