
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
