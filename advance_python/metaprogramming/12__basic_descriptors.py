from inspect import Parameter, Signature


class Descriptor:
    """
    A basic descriptor
    """
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        # del instance.__dict__[self.name]
        raise AttributeError("Can't delete...")


def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )


class StructureMeta(type):
    def __new__(cls, *args, **kwargs):
        cls_obj = super().__new__(cls, *args, **kwargs)
        signature = make_signature(cls_obj._fields)
        setattr(cls_obj, '__signature__', signature)
        return cls_obj


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    name   = Descriptor('name')
    shares = Descriptor('shares')
    price  = Descriptor('price')

s = Stock("ACME", 20, 92.1)
print(s.shares) # shares.__get__ method is called
s.shares = 50   # shares.__set__(s, 50)
del s.shares
