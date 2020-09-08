# 3 ways of creating classes (without using metaclass)

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
