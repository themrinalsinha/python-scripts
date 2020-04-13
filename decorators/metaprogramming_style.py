
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


# decorators
"""
Metaclasses are often perceived as a very tricky and dangerous thing to play with,
and indeed they are seldom required in python, with the most notable exception
(no pun intended) being the Abstract Base Class provided by the collection module.

Decorators, on the other side, are a feature loved by many experienced programmers
and after their introduction the community has developed a big set of very interasing use cases.
"""
# # Example....

# @dec
# def func(*args, **kwargs):
#     pass

# or

# func = dec(func)
# ==================================================
def func():
    """
    setting custom function attribute in python
    """
    pass
func.attr = "a custom function attribute"
print(f'function attribute: {func.attr}')


class SomeClass(object):
    pass
SomeClass.attr = "a custom class attribute"
print(f'a custom class attribute: {SomeClass.attr}')
print('\n')
# ===================================================

# class based decorators without arguments
class CustomAttr(object):
    def __init__(self, func):
        self.attr = 'a custom function attribute'
        self.func = func

    def __call__(self):
        print(f'1. call method called: {self.attr}')
        self.func()
        print(f'2. post func exected')

@CustomAttr
def func():
    print('===> my function :)')
    pass

func()
print('\n')
# =================================================

# class based decorators with arguments
