import re
from collections import OrderedDict


def _make_init(fields):
    """
    give a list of field names, make an __init__ method
    """
    code = f"def __init__(self, {','.join(fields)}):\n"
    for name in fields:
        code += f'   self.{name} = {name}\n'
    return code

def _make_setter(dcls):
    code = 'def __set__(self, instance, value):\n'
    for d in dcls.__mro__:
        if 'set_code' in d.__dict__:
            for line in d.set_code():
                code += '   ' + line + '\n'
    return code

class DescriptorMeta(type):
    def __init__(self, clsname, bases, clsdict):

        if '__set__' not in clsdict:
            # super().__init__(clsname, bases, clsdict)
            # make the set_code
            code = _make_setter(self)
            exec(code, globals(), clsdict)
            setattr(self, '__set__', clsdict['__set__'])
        else:
            raise TypeError('define set_code()')


class Descriptor(metaclass=DescriptorMeta):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    @staticmethod
    def set_code():
        return [
            'instance.__dict__[self.name] = value'
        ]


    def __delete__(self, instance):
        raise AttributeError("Can't delete...")


class Typed(Descriptor):
    data_type = object

    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.__class__.data_type):',
                'raise TypeError(f"Expected {self.__class__.data_type}")'
        ]


class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '   raise ValueError("Must be >= 0")'
        ]


class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if len(value) > self.maxlen:',
            '   raise ValueError("Too big...")'
        ]


class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if not self.pat.match(value):',
            '   raise ValueError("Invalid String")'
        ]


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


class StructureMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, cls_dict):
        fields = [key for key, value in cls_dict.items()
                    if isinstance(value, Descriptor)]

        for name in fields:
            cls_dict[name].name = name

        # making init function
        if fields:
            init_code = _make_init(fields)
            exec(init_code, globals(), cls_dict)

        cls_obj = super().__new__(cls, name, bases, dict(cls_dict))
        return cls_obj


class Structure(metaclass=StructureMeta):
    _fields = []

class Stock(Structure):
    name   = SizedRegexString(maxlen=5, pat='[A-Z]+$')
    price  = Float()
    shares = PositiveInteger()

s = Stock(name="AAPL", price=101.0, shares=123)
print(s.name)
print(s.price)
print(s.shares)

print(_make_setter(Descriptor))
print(_make_setter(PositiveInteger))









