from collections import ChainMap
from functools   import wraps
from inspect     import signature


_contracts = {}

class Contract(object):
    @classmethod
    def __init_subclass__(cls) -> None:
        _contracts[cls.__name__] = cls

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

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

# def checked(func):
#     _signature  = signature(func)
#     _annotation = func.__annotations__

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         bound = _signature.bind(*args, **kwargs)
#         for name, value in bound.arguments.items():
#             if name in _annotation:
#                 _annotation[name].check(value)
#         return func(*args, **kwargs)
#     return wrapper

def checked(func):
    _signature  = signature(func)
    _annotation = ChainMap(
        func.__annotations__,
        func.__globals__.get('__annotations__',{})
    )

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = _signature.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            if name in _annotation:
                _annotation[name].check(value)
        return func(*args, **kwargs)
    return wrapper


class BaseMeta(type):
    @classmethod
    def __prepare__(cls, *args):
        return ChainMap({ }, _contracts)

    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class Base(metaclass=BaseMeta):
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
