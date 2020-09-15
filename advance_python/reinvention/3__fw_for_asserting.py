



class Contract:
    @classmethod
    def check(cls, value):
        pass

# # ======= LOT OF SAME TYPE OF REPEATITION ===================
# class Integer(Contract):
#     @classmethod
#     def check(cls, value):
#         assert isinstance(value, int), "Expected Integer"

# class String(Contract):
#     @classmethod
#     def check(cls, value):
#         assert isinstance(value, str), "Expected String"

# class Float(Contract):
#     @classmethod
#     def check(cls, value):
#         assert isinstance(value, float), "Expected Float"

# # USAGE:
# # Integer.check(2)
# # Integer.check(2.7)
# # ============================================================

# we'll make a generalized class
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

class Nonempty(Contract):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, "Must be Non-Empty"
        super().check(value)

# if we put super().check(value) in our class methods then we can
# implement check like, call it "composition"
class PositiveInteger(Integer, Positive):
    pass

# ===============================================================

# Now, if we use these annotation in our function, it is not
# necessarily going to work. they don't do anything...

from inspect   import signature
from functools import wraps

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


@checked
def gcd(a: PositiveInteger, b: PositiveInteger):
    while b:
        a, b = b, a % b
    return a

gcd(1, 2)
gcd(2.1, 3.1) # it will fail...
# print(gcd.__annotations__)

"""
Now, in order to have these checks enabled
we might have to create a decorator
"""

