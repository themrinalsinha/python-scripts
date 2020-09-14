import re
from inspect     import Signature, Parameter
from collections import OrderedDict


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete...")


class Typed(Descriptor):
    data_type = object

    def __set__(self, instance, value):
        if not isinstance(value, self.__class__.data_type):
            raise TypeError(f"Expected {self.__class__.data_type}")
        super().__set__(instance, value)


class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Must be >= 0")
        super().__set__(instance, value)


class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError("Too big...")
        super().__set__(instance, value)


class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError("Invalid String")
        super().__set__(instance, value)



class Integer(Typed):
    data_type = int

class Float(Typed):
    data_type = float

class String(Typed):
    data_type = str

class PositiveInteger(Integer, Positive):
    pass

class FloatPositive(Float, Positive):
    pass

class SizedString(String, Sized):
    pass

class SizedRegexString(SizedString, Regex):
    pass


def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names
    )


class StructureMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, cls_dict):
        fields = [key for key, value in cls_dict.items()
                    if isinstance(value, Descriptor)]

        for name in fields:
            cls_dict[name].name = name

        cls_obj = super().__new__(cls, name, bases, dict(cls_dict))
        signature = make_signature(fields)
        setattr(cls_obj, '__signature__', signature)
        return cls_obj


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            setattr(self, name, value)



# class Stock(Structure):
#     """
#     This is annoying, if you see, we've used "name" like for 3 times
#     for almost each attribute, we'll see how we can overcome this
#     repeation and how we push it further...

#     In order to solve this problem, we need a new metaclass...
#     """
#     _fields = ['name', 'price', 'shares']

#     name    = SizedRegexString("name", maxlen=5, pat='[A-Z]+$')
#     price   = Float("price")
#     shares  = PositiveInteger("shares")
# s = Stock(name="AAPL", price=101.0, shares=123)
# s = Stock(name="AAPL", price=101.0, shares=112)


class Stock(Structure):
    name   = SizedRegexString(maxlen=5, pat='[A-Z]+$')
    price  = Float()
    shares = PositiveInteger()

s = Stock(name="AAPL", price=101.0, shares=123)
print(s.name)
print(s.price)
print(s.shares)
