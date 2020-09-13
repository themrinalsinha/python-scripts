
from functools import wraps, partial

def debug(prefix=""):
    def decorate(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@debug(prefix="****")
def add(x, y):
    return x + y
print(add(1, 3))


# IMPORTANT: to write above function in this manner
# reformulation of above function
def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

@debug(prefix="====> ")
def sub(x, y):
    return x - y

print(sub(1, 2))
