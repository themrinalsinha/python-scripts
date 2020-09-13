"""
writing state of the art decorator function to capture log.
"""
from genericpath import exists
from typing import Any

import os
import sys
import logging
import datetime

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

        if not exists("logs"):
            os.makedirs("logs")

        logging.basicConfig(filename=f"logs/{func_name}.log", level=logging.DEBUG)
        logging.debug(message)

        return result

class Test(object):
    def __init__(self) -> None:
        pass

    @Logging
    def methodA(self):
        print("Hello from methodA")
        return True

    @Logging
    def method__B(self):
        print("hello from method__B")

t = Test()
t.methodA()
t.method__B()
