# Decorators with Args

# calling convention
# @decorator(args)
# def func():
#   pass
#
# Evaluates as
# func = decorator(args)(func)

from functools import wraps

def debug(prefix=''): # Outer function defines variables for use in regular decorator.
    def decorator(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator
# in the above function, it works but there is alot of code repetation.
# Here there is code repetation.


# If you want to avoid code repetation, what you can do.

from functools import wraps, partial

def debugging(func=None, *, prefix=''):
    if func is None:
        return partial(debugging, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

# @debugging
@debugging(prefix='***')
def sub(x, y):
    return x - y

sub(5, 4)
