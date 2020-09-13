
# ====== same kind of class with different attributes =======
class Stock:
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Address:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port     = port
# ===========================================================

"""
A better approach to the above problem:
-------------------------------------------------------------
So, rather than writing the code as we've written above we can
define a certian structure that we can use
"""
class Structure(object):
    _fields = []

    def __init__(self, *args):
        print(self._fields, args)
        for name, value in zip(self.__class__._fields, args):
            setattr(self, name, value)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']

stock = Stock("AAPL", 100, 12.5)
print(stock.name)
print(stock.shares)
print(stock.price)

"""
The downside of the above approach is that we loose the function
signature, and capability to pass argument as a kwargs etc..
"""
