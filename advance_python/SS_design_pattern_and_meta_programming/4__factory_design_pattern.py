

"""
factory design patterns
"""

class A(object):
    def __init__(self) -> None:
        pass

    def methodA(self):
        print("I am method A")

    def print(self):
        print("A")


class B(object):
    def __init__(self) -> None:
        pass

    def methodB(self):
        print("I am method B")

    def print(self):
        print("B")

"""
we have two classes A and B it can be more and when you want to
call them you have to create objects of it and call them one by one.
we'll see how factory design pattern helps us in solving the problem.
"""

# this is how you use factory design method

def get(obj=None):
    objs = dict(a = A(),
                b = B())
    return objs[obj]

a = get('a')
a.print()

b = get('b')
b.print()
