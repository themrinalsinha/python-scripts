
# checking type of function
def func():
    """
    Since python pushes the oop to its max, it makes a point of always following
    the tenant everything is an object, So python functions are objects.
    """
    pass
print(f"Type of function: {type(func)}")
print(f"Type of type of function: {type(type(func))}")
print(f"Bases of type of function: {type(func).__bases__}")


# callables
"""
while python has the well-defined function class seen in the above example, it
relies more on the presence of the __call__ method. That is, in python any object
can act as a function, provided that it has this method, which is invoked when the
object is "called"
"""
def func_callable():
    pass
print(f"Function is callable: {func_callable.__call__}")
