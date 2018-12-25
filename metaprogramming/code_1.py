# Problem: Structures

# This is how you generally deine classes.
# It looks very repetative and annoying...
class Stock:
    def __init__(self, name, shares, price):
        self.name   = name
        self.price  = price
        self.shares = shares

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Host:
    def __init__(self, address, port):
        self.address = address
        self.port    = port


# === Other way to do it =====
# This is a technique in the standard library, we'll just generialize things a little bit.
class Structure:
    _field = []
    def __init__(self, *args):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

class Stock(Structure):
    _field = ['name', 'shares', 'price']

class Stock(Structure):
    _field = ['x', 'y']

class Host(Structure):
    _field = ['address', 'port']
