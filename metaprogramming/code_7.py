# What I've seen in code_6.py, it works but it's rather annoying.
# Can't it be simplified in some way ?

# Solutions:
# Ah, a problem involving class definitions
#   -> Class decorators
#   -> Metaclasses
#
# Let's explore both options.

# Class Decorators
# eg:
def add_signature(*names):
    def decorate(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorate

@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass

@add_signature('x', 'y')
class Point(Structure):
    pass

# OR
# Metaclass Solution
class StructMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        sig    = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _field = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)
