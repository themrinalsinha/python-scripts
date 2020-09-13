"""
Variation: Debug Access
Rewriting part of the class itself...
"""

def debugattr(cls):
    _attributes = cls.__getattribute__

    def __getattribute__(self, name):
        print("GET: ", name)
        return _attributes(self, name)

    cls.__getattribute__ = __getattribute__
    return cls


@debugattr
class Point(object):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(p.y)
