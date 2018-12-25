class Structure(object):
    _field = []
    def __init__(self, *args):
        for name, value in zip(self._field, args):
            setattr(self, name, value)

class Stock(Structure):
    _field = ['name', 'shares', 'price']

class Point(Structure):
    _field = ['x', 'y']

class Host(Structure):
    _field = ['address', 'port']

x = Stock('YES Bank', 50, 280.89)
import pdb; pdb.set_trace()
print(x.name, x.shares, x.price)

# Issues with this are:
# No support for keyword args
# >>> s = Stock('ACME', price=123.45, shares=50) //It will throw error.
# Missing calling signatures
# >>> import inspect
# >>> print(inspect.signature(Stock)) (*args)
