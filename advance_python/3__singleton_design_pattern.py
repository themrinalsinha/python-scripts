
from typing import Any

class A(object):
    def __init__(self) -> None:
        pass

# this will create an object at a certain memory location
a = A()
print(a)

# this will create another object at different memory location
a1 = A()
print(a1)

# IMPORTANT:
# So, in some usecases, we don't want to created multiple instances
# of the object, we want to restrict the programmer from doing that.
# So, singleton design pattern helps you to create only 1 instance
# of the class at a time. It can only create one single instance at a time

class MetaClass(type):
    """
    this is singleton design pattern
    """
    _instance = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        if the instance already exists don't create new one
        """
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class A(metaclass=MetaClass):
    def __init__(self) -> None:
        pass

a = A()
print(a)

# this will not let new object to be created
a1 = A()
print(a1) # --> None
