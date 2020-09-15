"""
Now, as we seen in the previous example, now we don't want
to write setter functions in our class, so how can we do that.
without writing setter function and defining properties in our class
"""


from ast import Str


class Contract(object):
    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    # 3.6+ feature
    def __set_name__(self, cls, name):
        self.name = name

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

class String(Typed):
    type = str

class Float(Typed):
    type = float

class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, f"Value be > 0"
        super().check(value)

class NonEmpty(Contract):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, "Must be Non-Empty"
        super().check(value)

class NonEmptyString(String, NonEmpty):
    pass

class Player:
    name = NonEmptyString()
    x = Integer()
    y = Integer()

    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x    = x
        self.y    = y

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx
