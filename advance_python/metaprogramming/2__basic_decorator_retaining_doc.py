"""
@wraps(func) helps in preventing the function docstring
otherwise it will only show the wrapper function.
"""

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        # fully qualified function name
        print(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper

@debug
def add(x, y):
    """ addition function """
    return x + y

@debug
def sub(x, y):
    """ substraction function """
    return x - y

def mul(x, y):
    """ multiplication function """
    return x * y

def div(x, y):
    """ division function """
    return x / y


# # without @wraps
# print(help(add))

add(2, 3)
