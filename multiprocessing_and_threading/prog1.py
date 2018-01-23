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
