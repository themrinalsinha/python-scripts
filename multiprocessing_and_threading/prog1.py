from time import sleep

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

