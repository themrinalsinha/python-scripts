# Functools: it is for higher order function, it treats the functions as objects (arguments)
# manipulate the functions and return them as output.
# functools is used to make your code look more elegant and readable. (sometimes efficient)


# ======================================================================================
# functools.reduce() is used to apply a function to an iterable and reduce it to a single cumulative value.
from functools import reduce
items = [1, 2, 3, 4, 5]
# sum of list (rolling computation)
# 1 2 3 4 5
# 3 3 4 5
# 6 4 5
# 10 5
# 15
# to do this using reduce function.
# reduce(function, iterable, initializer)
sum_1 = reduce(lambda x, y: x + y, items)
max = reduce(lambda x, y: max(x, y), items)
# NOTE: if you don't provide initializer, it will take first element as initializer.
_sum = reduce(lambda x, y: x + y, items, 10) # with initializer
print(sum_1, max, _sum)

# ======================================================================================

# Magic functions for comparison
# __eq__ for ==
# __ne__ for !=
# __lt__ for <
# __le__ for <=
# __gt__ for >
# __ge__ for >=

class Car:
    def __init__(self, model, mileage) -> None:
        self.model = model
        self.mileage = mileage

    def __eq__(self, __o: object) -> bool:
        return self.mileage == __o.mileage

    def __lt__(self, __o: object) -> bool:
        return self.mileage < __o.mileage

    def __gt__(self, __o: object) -> bool:
        return self.mileage > __o.mileage

c1 = Car('BMW', 100)
c2 = Car('Audi', 200)

print(c1 == c2)
print(c1 < c2)
print(c1 > c2)

# We have implemented a basic class that have 3 magic functions for comparison.
# Now we can use these functions to compare the objects of this class.

# Now, our func doesn't support __le__ or __ge__ so if we try to compare using these functions
# it will throw an error.
# print(c1 <= c2) # TypeError: '<=' not supported between instances of 'Car' and 'Car'
# print(c1 >= c2) # TypeError: '>=' not supported between instances of 'Car' and 'Car'
# To solve this problem we can use functools.total_ordering decorator.


from functools import total_ordering

@total_ordering
class Car:
    def __init__(self, model, mileage) -> None:
        self.model = model
        self.mileage = mileage

    def __eq__(self, __o: object) -> bool:
        return self.mileage == __o.mileage

    def __lt__(self, __o: object) -> bool:
        return self.mileage < __o.mileage

    def __gt__(self, __o: object) -> bool:
        return self.mileage > __o.mileage

# NOW, we can compare using all the comparison operators. (<=, >=)
# This decorator will automatically implement the missing comparison operators.
# It will check if __eq__ is implemented, if not it will raise an error.

c1 = Car('BMW', 100)
c2 = Car('Audi', 200)

print(c1 == c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2) # it will automatically implement this function.
print(c1 >= c2) # it will automatically implement this function.

# PS: In order to use this decorator, you must implement __eq__ and __lt__ or __gt__.


# ======================================================================================

# Working with property and cached_property
# property is used to create a property of a class. It allows you to treat your class
# methods as class attributes.

class Marksheet:
    def __init__(self, *grades) -> None:
        self.grades = grades

    @property
    def total(self):
        print("Calculating total...")
        return sum(self.grades)

    @property
    def average(self):
        print("Calculating average...")
        return self.total / len(self.grades)

m = Marksheet(10, 20, 30, 40, 50)
print(m.grades)
print(m.total)
print(m.average)

# Now, if we try to access the total or average property multiple times, it will
# calculate the total and average multiple times.
# To avoid this, we can use cached_property from functools.

from functools import cached_property

class Marksheet:
    def __init__(self, *grades) -> None:
        self.grades = grades

    @cached_property
    def total(self):
        print("Calculating total...")
        return sum(self.grades)

    @cached_property
    def average(self):
        print("Calculating average...")
        return self.total / len(self.grades)

m = Marksheet(10, 20, 30, 40, 50)
print("[CP]: ", m.total)
print("[CP]: ", m.average)

# Now, if we try to access the total or average property multiple times, it will
# calculate the total and average only once.
# It will store the value in cache and will return the value from cache if we try to access it again.
print("\n")
# ======================================================================================

# Working with lru_cache
# lru_cache is used to cache the return value of a function.
# It will store the return value of a function and will return the value from cache if we try to call the function again.

# without lru_cache
def fib(n):
    if n < 2:
        return n
    print(f"Calculating fib({n})")
    return fib(n - 1) + fib(n - 2)
print("Without lru_cache")
print([fib(x) for x in range(10)])


# with lru_cache
from functools import lru_cache

@lru_cache(maxsize=1000) ## maxsize is optional (it means how many values you want to store in cache)
def fib(n):
    if n < 2:
        return n
    print(f"Calculating fib({n})")
    return fib(n - 1) + fib(n - 2)

print("With lru_cache")
print([fib(x) for x in range(10)])

# You can see the detail of lru_cache using <function_name>.cache_info()
print(fib.cache_info())
# CacheInfo(hits=28, misses=10, maxsize=1000, currsize=10)
# hits: number of times the value was returned from cache.
# misses: number of times the value was calculated.
# maxsize: maxsize of the cache.
# currsize: current size of the cache.

# NOTE: typed=True is optional. It will cache the value based on the type of the arguments.
print()
# ======================================================================================

# working with partial function from functools
# partial function is used to create a new function from an existing function.
# It will create a new function with the same name and docstring of the existing function.
# It will also copy the argument names of the existing function.
# It will also copy the annotations of the existing function.

def add(a, b):
    return a + b

print(add(10, 20))
# Now, if you want to pass only one argument to the add function
# you can do something like
def add_one(a):
    return add(a, 1)

print(add_one(10))

# The same thing can be done using partial function.

from functools import partial

add_one = partial(add, 10)
print(add_one(12))

add_two = partial(add, b=2)
print(add_two(10))

# *** IMPORTANT ***
# pass default value for a
add_x = partial(add, a=11)
# add_x(12) ## will raise error, because we are trying to pass two values for a.
print(add_x(b=12))
print()
# ======================================================================================

# working with wraps from functools
# wraps is used to copy the metadata of a function to another function.
# It will copy the name, docstring, argument names, annotations of the function.

def mylogger(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@mylogger
def add(a, b):
    """This function adds two numbers"""
    return a + b

print("without wraps")
print(add(10, 20))
print(add.__name__)
print(add.__doc__)
print()
# Now, if you want to copy the metadata of the add function to the wrapper function
# you can do something like

from functools import wraps

def mylogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is a wrapper function"""
        print(f"Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@mylogger
def add(a, b):
    """This function adds two numbers"""
    return a + b

print("with wraps")
print(add(10, 20))
print(add.__name__)
print(add.__doc__)
print()
# ======================================================================================

# working with singledispatch from functools
# singledispatch is used to create a generic function.
# It will create a generic function that can be used with different types of arguments.
# It will create a registry of different types of arguments and will call the appropriate function based on the type of the argument.

# without singledispatch example

def append_one(obj):
    if type(obj) == list:
        return obj + [1]
    elif type(obj) == str:
        return obj + "1"
    elif type(obj) == int:
        return obj + 1
    elif type(obj) == dict:
        obj.update({"1": 1})
        return obj
    elif type(obj) == set:
        return obj.union({1})
    else:
        raise TypeError(f"Type {type(obj)} not supported")

print("Without singledispatch and a func with a lot of if else")
print(append_one([2, 3]))
print(append_one({2, 3}))
print(append_one({2: 2, 3: 3}))
print(append_one("abc"))
print(append_one(10))

# with singledispatch: now we'll try to create generic function
# GENERIC FUNCTION: A function that can be used with different types of arguments.
# single dispatch: A form of generic function where the implementation is chosen based on the type of the first argument.
# example:
# [1, 2, 3, 4] -> [1, 2, 3, 4, 1]
# {2, 3, 4, 5} -> {1, 2, 3, 4, 5}
# {2: 2, 3: 3} -> {2: 2, 3: 3, "1": 1}
# "abc" -> "abc1"

from functools import singledispatch

@singledispatch
def append_one(obj):
    raise NotImplementedError("Unsupported type")

@append_one.register(list)
def _(obj):
    return obj + [1]

@append_one.register(set)
def _(obj):
    return obj.union({1})

@append_one.register(dict)
def _(obj):
    obj.update({"1": 1})
    return obj

@append_one.register(str)
def _(obj):
    return obj + "1"

@append_one.register(int)
def _(obj):
    return obj + 1

print("With singledispatch")
print(append_one([2, 3]))
print(append_one({2, 3}))
print(append_one({2: 2, 3: 3}))
print(append_one("abc"))
print(append_one(10))
