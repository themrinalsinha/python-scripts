# Debug all the mehods of a class.

from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

# -> Can you decorate all methods at once, yes you can
# by using class decorator.
# -> one decorator application, covers all definition within the class, It even mostly works.

def debugmethods(cls):
    # cls is a class
    for key, value in vars(cls).items(): # 'vars' gives you class dictionary.
        if callable(value):
            setattr(cls, key, debug(value))
    return cls

@debugmethods
class Spam(object):
    def a(self):
        pass
    def b(self):
        pass

x = Spam()
print(x.a)
print(x.a())
print(x.b)
print(x.b())
# Basic Idea of class decorator is:
#   -> Walk through class dictionary
#   -> Identify callables (eg: methods)
#   -> Wrap with a decorator
#
# Limitations:
#   -> Only instance methods get wrapped.

