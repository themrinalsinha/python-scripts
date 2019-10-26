from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))

# Partial function allows us to fix a certain number of arguments of a
# function and generates a new function.

# A normal function
def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# A partial function that calls f with
# a = 3, b = 1, and c = 4
g = partial(f, 3, 1, 4)
print(g(3))
