# =================================================================
# 3 ways of creating classes (without using metaclass)
# =================================================================

from typing import Any

# METHOD - 1
class A(object):
    def __init__(self) -> None:
        pass
a = A()
print(a)


# METHOD - 2
class B(object):
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        return super(B, cls).__call__(cls, *args, **kwargs)
b = B()
print(b)


# METHOD - 3
class C(object):
    def __new__(cls, *args: Any, **kwargs: Any):
        print("Creating an object")
        return super(C, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("Creating instance of class")
        super(C, self).__init__(*args, **kwargs)

c = C()
print(c)

# ====================================================================
# 3 ways of creating classes using metaclasses
# ====================================================================

# NOTE: by default all the objects in python inherits from "type", eg: print(type(int)) --> <type>

# METHOD - 4

# Defining a base class, inheriting from "type"
class D(type):
    def __call__(cls, *args, **kwargs):
        instance = super(D, cls).__call__(*args, **kwargs)
        return instance

    def __init__(cls, name, base, attr):
        super(D, cls).__init__(name, base, attr)

class E(metaclass=D):
    pass

e = E()
print(e)

# Or rewriting it differently
class Meta(type):
    def __new__(cls, *args, **kwargs):
        return super(Meta, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Meta, self).__init__(*args, **kwargs)

class MyClass(metaclass=Meta):
    def __init__(self) -> None:
        pass
mc = MyClass()
print(mc)
