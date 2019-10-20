# TYPEHINTS AND STATIC TYPING IN PYTHON

# NOTES:
# -> Python is dynamically typed language, so you don't have to actually specify datatypes
# -> In the example function below if we pass an integer it will work fine, but if we pass
#    numbers like 3.10 or '3' syntatically it is correct but it will throw an error
# -> how can we protect ourself from these dynamically typing bugs, using type hints
# -> what we have done in th_factorial function is type hint it is actually ignored by the
#    interperter, it actaully doest solves the problem.
# -> map_int_list(func, l) where func is a funcion and it is callable so you can define it
#    by importing callable from typing module.
# -> map_int_dict(func, d) Dict[Any, int], here Any means the key can be anything of type int
# -> NOTE: if you want to validate both int and float then in that case you will use union.

from typing import Callable, List, Dict, Any, Union


# eg normal function:
def factorial(num):
    if num < 0:
        return None
    if num == 0:
        return 1
    return num * factorial(num-1)

# eg function with typehint
def th_factorial(num: Union[int, float]) -> int:
    num = int(num)
    if num < 0:
        return 0
    if num == 0:
        return 1
    return num * factorial(num-1)

print(th_factorial(5.3))

def map_int_list(func: Callable, l: List[int]) -> List[int]:
    return [func(i) for i in l]

# print(map_int_list(th_factorial, [0,2,3,4,5,6]))

def map_int_dict(func: Callable, d: Dict[Any, int]) -> Dict[Any, int]:
    return {key: func(value) for key, value in d.items()}

print(map_int_dict(th_factorial, {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4}))


# To run this script in test
# $ pip install mypy
# $ python -m mypy typehints_and_static_typing.py
