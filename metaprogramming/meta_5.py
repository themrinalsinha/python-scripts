def debugattr(cls):
    orig_getattribute = cls.__getattribute__
    def __getattribute__(self, name):
        print('GET: ', name)
        return orig_getattribute(self, name)
    cls.__getattribute__ = __getattribute__
    return cls

@debugattr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(p.y)

# Now let's say there are alot of class so now,
# you have to put the class decorator on all the classes
# so the solution to that is a Metaclass

# *****
# All values in Python have a type
# eg: x = 42; type(x) -> int
# eg: x = 'Hello'; type(x) -> str

# Types and classes
# Every type is defined by Classes, Classes define new types
# class Spam:
#   pass
# >>> s = Spam()
# >>> type(s)
#
# The class is the type of instance created
# The class is a callable that creates instances
# This class creates new "type" objects
#
# Types are their own class (builtin)
