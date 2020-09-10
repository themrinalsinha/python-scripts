

from inspect     import Signature, Parameter
from collections import OrderedDict

class Descriptor(object):
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, instance, owner):
        print(f"__get__ called --> {instance}, {owner}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"__set__ called --> {instance}, {value}")

    def __delete__(self, instance):
        print(f"__delete__ called --> {instance}")
        del instance.__dict__[self.name]

    def __repr__(self) -> str:
        return f"Descriptor ---> {self.name}"

class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Expected ---> {self.ty}")
        super().__set__(instance, value)


class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be less than 0")


class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs) -> None:
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError("Too big..")
        super().__set__(instance, value)

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names
    )

def _make_init(fields):
    code = f"def __init__(self, {', '.join(fields)}):"
    for name in fields:
        code += f'   self.{name} = {name}\n'
    return code

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class SizedString(String, Sized):
    pass

class StructMeta(type):

    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __name__(cls, name, bases, clsdict):
        fields = [key for key, val in clsdict.items()
                    if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name

        if fields:
            init__code = _make_init(fields)
            exec(init_code, globals(), clsdict)
        clsobj = super().__new__(cls, name, bases, dict(clsdict))
        return clsobj


class Structure(metaclass=StructMeta):
    fields = []

class Stock(Structure):
    name = SizedString(maxlen=8)
    shares = PositiveInteger()

if __name__ == "__main__":
    o = Stock()
    o.name = 'Mrinal Sinha'
    o.shares = 123
    print(o)
