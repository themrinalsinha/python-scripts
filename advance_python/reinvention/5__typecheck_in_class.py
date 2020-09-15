"""
Now, as we seen in the previous example, now we don't want
to write setter functions in our class, so how can we do that.
without writing setter function and defining properties in our class
"""

from inspect   import signature
from functools import wraps

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

class PositiveInteger(Integer, Positive):
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

def checked(func):
    _signature  = signature(func)
    _annotation = func.__annotations__

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = _signature.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in _annotation:
                _annotation[name].check(value)
        return func(*args, **kwargs)
    return wrapper

class Base:
    # 3.6+ feature
    @classmethod
    def __init_subclass__(cls) -> None:
        # Applying check decorator
        for name, val in cls.__dict__.items():
            if callable(val):
                setattr(cls, name, checked(val))

        # Instantiate the contracts
        for name, value in cls.__annotations__.items():
            contract = value()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)

    def __init__(self, *args):
        ann = self.__annotations__
        assert len(args) == len(ann), f"Expected {len(ann)} arguments"

        # 3.6+ Ordered dictionary feature
        for name, value in zip(ann, args):
            setattr(self, name, value)

    def __repr__(self) -> str:
        args = ','.join(repr(getattr(self, name)) for name in self.__annotations__)
        return f"{type(self).__name__}({args})"


# complete type checking python
class Player(Base):
    # python 3.6+ class annotation feature
    name: NonEmptyString
    x   : Integer
    y   : Integer

    def left(self, dx: PositiveInteger):
        self.x -= dx

    def right(self, dx: PositiveInteger):
        self.x += dx

print(Player.__annotations__)
