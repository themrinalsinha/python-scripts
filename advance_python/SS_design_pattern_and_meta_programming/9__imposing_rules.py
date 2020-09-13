"""
Objective: How can we impose rules while creating classes with metaclass
---> class should only be created if first letter is capital otherwise throw error
---> class should have a constructor otherwise throw error
---> all methods should start with lowercase i.e function name should start with lower case
---> every function should be provided with a doc string otherwise class should not be created
---> there should be only one instance created of class implementing singleton design pattern
---> should not be able to add parameters at run time we use slots
---> using descriptors and decorators
"""

import os
import sys
import datetime
from typing import Any

class Meta(type):
    """ metaclass """
    _instances = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        """ implementing singleton design pattern """
        print("*args  :", args)
        print("**kwds :", kwds)

        name = kwds.get("name", None)
        if not name.__str__:
            raise ValueError("name should be string...")


        if cls not in cls._instances:
            cls._instances[cls] = super(Meta, cls).__call__(*args, **kwds)
            return cls._instances[cls]

    def __init__(cls, name, base, attr) -> None:
        """ defining your own business rule """
        if cls.__name__[0].isupper():
            """ create class only if first letter is capital """
            for k, v in attr.items():
                if hasattr(v, '__call__'):
                    if v.__name__[0] == '_' or v.__name__[0].islower():
                        """ check name function starts with _ or lower case """
                        if v.__doc__ is None:
                            raise ValueError(f"make sure to provide documentation check - {v.__name__}")
                    else:
                        raise ValueError(f"function should start with lower case : {v.__name__}")
        else:
            raise ValueError(f"class name should starts with lower case: {v.__name__}")

class Logging(object):
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """ wrapper function """
        start     = datetime.datetime.now()         # start time
        result    = self.func(self, *args, **kwds)  # function call
        func_name = self.func.__name__              # function name
        end_time  = datetime.datetime.now()         # end time

        message = f"""
            Function name  : {func_name},
            Execution time : {end_time - start},
            Memory Size    : {sys.getsizeof(self.func)},
            Date           : {start.date()}
        """

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logging.basicConfig(filename=f"logs/{func_name}.log", level=logging.DEBUG)
        logging.debug(message)

        return result

class Test(metaclass=Meta):
    __slots__ = ['name']

    def __init__(self, name) -> None:
        """ this is my init function """
        self.name = name
        super(Test, self).__init__()

    def method(self):
        """ i am a docstring """
        print("hello world !! :)")

if __name__ == "__main__":
    o = Test(name="mrinal")
