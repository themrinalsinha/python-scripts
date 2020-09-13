from inspect import Parameter, Signature
from os import name


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

    def __str__(self) -> str:
        return f"{self.name} -> ({self.shares} | {self.price})"

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']

stock = Stock(name="Mrinal Sinha", shares=100, price=500)
print(stock)
