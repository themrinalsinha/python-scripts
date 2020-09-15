

class Contract:
    @classmethod
    def check(cls, value):
        pass

class Typed(Contract):
    type = None

    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f"Expected {cls.type}"
        super().check(value)

class Integer(Typed):
    type = int


class Player:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x    = x
        self.y    = y

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        Integer.check(value)
        self._x = value

p = Player('Guido', 0, 0)
print(p.x)
p.x = "123"


"""
p.x = '23'
p.left(-5)

OUTPUT:
Traceback (most recent call last):
  File "4__player.py", line 18, in <module>
    p.left(-5)
  File "4__player.py", line 10, in left
    self.x -= dx
TypeError: unsupported operand type(s) for -=: 'str' and 'int'
"""
