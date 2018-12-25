# Metaprogramming
# -> In a nutshell: code that manipulates code
# -> Common examples:
#       -> Decorators
#       -> Metaclasses
#       -> Descriptors
# -> Essentiall, it's doing things with code.
# -> Extensively used in frameworks and libraries.
# -> Better understanding of how python works.
#
# It solves major issue: DRY (Don't Repeat Yourself)
#       -> Highly repettive code sucks
#       -> Tedious to write
#       -> Hard to read
#       -> Difficult to modify

# Using and working with decorators.
def debug(func):
    # func is function to be wrapped.
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@debug
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y

add(5, 4)
sub(5, 4)
# Here decorators are ok, but they lose alot of information. like name
# or when you do help it shows wrappper into then actual info
# eg:
print(add)
# print(help(sub))


# to overcome that we use functools or to write decorators properl

