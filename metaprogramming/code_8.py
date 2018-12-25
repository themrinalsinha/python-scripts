from inspect import Parameter, Signature

def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)

        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

# x = Stock()
# import pdb; pdb.set_trace()

# As you can see it is back to original 'simple' solution
# Signatures are created behind scenes.


# Advices
#
# _> Use a class decorator if the goal is to tweak classes that mght be unrelated.
# _> Use a metaclass if you're trying to perform actions in combination with inheritance
# _> Don't be so quick to dismiss techniques (eg: 'metaclasses suck so blah blah..)
# _> All of the tools are meant to work together.
