from typing    import Any
from inspect   import signature
from functools import wraps

class Contract(object):
    @classmethod
    def check(cls, value):
        pass

class Typed(Contract):
    type = None

    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f"Expected type: {cls.type}"

class Integer(Typed):
    type = int

class String(Typed):
    type = str

class Boolean(Typed):
    type = bool

class Positive(Contract):
    @classmethod
    def check(cls, value):
        assert value > 0, "Value should be greater than 0"
        super().check(value)

class PositiveInteger(Positive, Integer):
    pass


# IMPORTANT
class Person(object):
    def __init__(self, age) -> None:
        self.age = PositiveInteger.check(age)


class Checked(object):
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.signature = signature(self.func)
        annotations    = self.func.__annotations__
        bind           = self.signature.bind(*args, **kwds)

        print(f"SIGNATURE  : ", self.signature)
        print(f"ANNOTATION : ", annotations)
        print(f"BIND       : ", bind)

        for name, val in bind.arguments.items():
            if name in annotations:
                annotations[name].check(val)
        return self.func(*args, **kwds)

@Checked
def funcc(a: PositiveInteger):
    print(f"AGE: {a}")


if __name__ == "__main__":
    # i = Integer.check(1212)
    # j = PositiveInteger.check('-1234')

    age = Person(123)

    funcc(123)
