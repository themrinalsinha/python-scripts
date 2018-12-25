from inspect import Parameter, Signature

# Signature utility function.
def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class Structure(object):
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'prices'])

class Point(Structure):
    __signature__ = make_signature(['x', 'y'])

class Host(Structure):
    __signature__ = make_signature(['hostname', 'port'])

# Now you can see that your classes are behaving much nicier.
# It has error checking inbuilt so if you miss certain parameters it will throw an error

s = Stock('Google', 123, 891.89)
print(s.name)

# you can also check signature of the class.
import inspect
print(inspect.signature(Stock))
print(inspect.signature(Point))
print(inspect.signature(Host))
