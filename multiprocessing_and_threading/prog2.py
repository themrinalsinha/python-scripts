# Multiprocessing...

# Here we are going to create two processes where one will calculate square
# and second one will create the cube. 

from multiprocessing import Process
from time            import sleep

def calc_square(numbers):
    print('Calculating squares')
    for n in numbers:
        sleep(0.2)
        print('Square : {}'.format(n ** 2))

def calc_cube(numbers):
    print('Calculating Cubes')
    for n in numbers:
        sleep(0.2)
        print('Cube : {}'.format(n ** 3))

if __name__ == "__main__":
    arr = [2, 6, 8, 5, 4]

    process_1 = Process(target=calc_square, args=(arr,))
    process_2 = Process(target=calc_cube, args=(arr,))

    # Starting the processes
    process_1.start()
    process_2.start()

    # Waits till the process start.
    process_1.join()
    process_2.join()

    print('Done !')