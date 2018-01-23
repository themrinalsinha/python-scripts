# THREADING...!

from time import sleep, time

def calc_square(numbers):
    print('Calculating Squares')
    for num in numbers:
        sleep(0.5)
        print('Square : ', num ** 2)

def calc_cube(numbers):
    print('Calculating cubes')
    for num in numbers:
        sleep(0.5)
        print('Cubes : ', num ** 3)

a = [2, 3, 4, 5, 6, 7]
# Starting time.
t = time()
calc_square(a)
calc_cube(a)
print('Done in : ', time() - t)
print('All done !\n')

print('\n============ WITH THREADING ============\n')

from threading import Thread

array = [2, 3, 4, 5, 6]

t        = time()
thread_1 = Thread(target=calc_square, args=(array,))
thread_2 = Thread(target=calc_cube, args=(array,))

# Start the thread - it will execute the programs in parallel
thread_1.start()
thread_2.start()

# Will wait till the thread is done.
thread_1.join()
thread_2.join()

print('Done is : {} with threading', time() - t)
print('All done !\n')

# OUTPUT: """
# Calculating Squares
# Square :  4
# Square :  9
# Square :  16
# Square :  25
# Square :  36
# Square :  49
# Calculating cubes
# Cubes :  8
# Cubes :  27
# Cubes :  64
# Cubes :  125
# Cubes :  216
# Cubes :  343
# Done in :  6.008454084396362
# All done !


# ============ WITH THREADING ============

# Calculating Squares
# Calculating cubes
# Cubes :  8
# Square :  4
# Square :  9
# Cubes :  27
# Square :  16
# Cubes :  64
# Square :  25
# Cubes :  125
# Square :  36
# Cubes :  216
# Done is : {} with threading 2.50368332862854
# All done !
# """