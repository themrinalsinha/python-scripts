
# for the solution implemented in 8__*.py
# we'll solve the problem of signature

from inspect import Parameter, Signature
from os import name


# # ====================== VERY VERY IMPORTANT =========================
# _fields = ['name', 'shares', 'price']
# params  = [ Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD) for fname in _fields]
# # now we can make signature out of these parameters
# sig = Signature(params)
# print(_fields, params, sig)
# # now we'll create a random function and bind this signature to it.
# def foo(*args, **kwargs):
#     bound = sig.bind(*args, **kwargs)
#     for name, value in bound.arguments.items():
#         print(name, value)

# # help(foo)
# foo(1, 2, 3) # or
# foo(name="APPL", shares=100, price=100)
# # foo(name="APPL", shares=100) # raise error price is missing
# # =====================================================================


# To implement the signature in our structure class
def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )

class Structure(object):
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__class__.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])

class Point(Structure):
    __signature__ = make_signature(['x', 'y'])

class Address(Structure):
    __signature__ = make_signature(['hostname', 'port'])


# NOW, as you can see both *args and **kwargs works
stock = Stock("AAPL", 100, 12.5)
print(stock.name)
print(stock.shares)
print(stock.price)

stock = Stock(name="GOOGL", shares=100, price=12.5)
print(stock.name)
print(stock.shares)
print(stock.price)
