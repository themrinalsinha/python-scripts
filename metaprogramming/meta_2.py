# In normal decorator you loose the function name and
# other information, if you type help, it will show
# the name of wrapper function. so to avoide that we
# use functools.wraps it helps to copy all the meta info
# of the function like name and docstrings (apply wraps as a decorator to function).

from functools import wraps

def debug_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(func.__qualname__) # fully qualified name
        return func(*args, **kwargs)
    return wrapper

@debug_1
def add(x, y):
    return x + y

print(add(5, 4))
print(add)
print(help(add))
# Note: If you don't use @wraps, weird things happen
# Big picture here is, debuggin code is isolated to single location,
# this makes it easy to change (or to disalbe)

# Variation Logging
from functools import wraps
import logging
import os

# Optional Disable.

def debug(func):
    if 'DEBUG' not in os.environ:
        return func
    log = logging.getLogger(func.__module__)
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg)
        return func(*args, **kwargs)
    return wrapper
# Key Idea: Can change decorator independently of code that uses it.
