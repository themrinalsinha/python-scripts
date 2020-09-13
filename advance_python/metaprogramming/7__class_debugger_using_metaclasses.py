
def debug(func):
    def wrapper(*args, **kwargs):
        print("DEBUG: ", func.__qualname__)
        return func(*args, **kwargs)
    return wrapper

def debugmethods(cls):
    for key, value in vars(cls).items():
        if callable(value):
            setattr(cls, key, debug(value))
    return cls

class debugmeta(type):
    def __new__(cls, name, bases, cls_dict):
        print("\n", cls, name, bases, cls_dict)
        cls_obj = super().__new__(cls, name, bases, cls_dict)
        cls_obj = debugmethods(cls_obj)
        return cls_obj

class Base(metaclass=debugmeta):
    pass

class Spam(Base):
    pass

class Grok(Spam):
    pass

class Mondo(Grok):
    def a(self):
        pass

x = Mondo()
x.a()
