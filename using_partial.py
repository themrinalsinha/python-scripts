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

# ==================================================================


def bg_task(method=None, a=4, b=5):
    print(method)
    if method is None:
        return partial(bg_task, a=a, b=b)

    def start(a, b, **kwargs):
        print('started called')

    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        print('in wrapper')
        return method(*args, **kwargs)
    wrapper.start = start
    return wrapper

@bg_task()
def add(a, b):
    return a + b

print(add.start(4, 3))
