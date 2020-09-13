from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        # fully qualified function name
        print(f"DEBUG: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    """ cls is a class """
    # IMP: vars(cls) gives you the class dictionary
    for key, value in vars(cls).items():
        if callable(value):
            setattr(cls, key, debug(value))
    return cls


@debugmethods
class Spam:
    def a(self):
        pass

    def b(self):
        pass

    def c(self):
        pass

    def d(self):
        pass

o = Spam()
o.a()
o.b()
# o.c()
o.d()
