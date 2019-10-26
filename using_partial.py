from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))
