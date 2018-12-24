# @classmethod and @staticmethod in python

class MyClass:
    # Instance method:
    # -> can modify object instance state
    # -> can modify class state
    def method(self):
        return 'Instance method called', self

    # Class method:
    # -> Can't modify object instance state
    # -> Can modify class state
    @classmethod
    def classmethod(cls):
        return 'Classmethod called', cls

    # Static method:
    # -> Can't modify object instance state
    # -> Can't modify class state
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
# Now the key difference, Now let's not create instance of the class
print(MyClass.classmethod())
print(MyClass.staticmethod())

# The above 2 methods work fine, but when we try to do the same with regular method.
# print(MyClass.method())
# ---------------------------------------------

# classmethod
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return 'Pizza({})'.format(self.ingredients)

# print(Pizza(['cheese', 'tomatoes']))
# print(Pizza(['cheese', 'tomatoes', 'chicken']))
# print(Pizza(['cheese', 'tomatoes', 'chicken', 'mushrooms']))
    @classmethod
    def margerita(cls):
        return cls(['cheese', 'tomaoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

print(Pizza.margerita())
print(Pizza.prosciutto())
# ----------------------------------------------

class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius      = radius

    def __str__(self):
        return 'Pizza({})'.format(self.ingredients)

    def area(self):
        return self._circle_area(self.radius)

    # Basically a static method doesn't have access to the class or the object
    # instance at all, it's a pretty big limitation but it's also really good signal
    # but it's also a pretty goood way to show it's completely independet to show

    @staticmethod
    def _circle_area(r):
        return r ** 2 * 3.14

print(Pizza(4.5, ['cheese']).area())

# =================================

class TrapAtrist(object):
    _hits = [
        'Hit the floor',
        'Hit and run',
        'Hit Hit HIt'
    ]

    def __init__(self, name):
        self.name = name

    @classmethod
    def hits(cls):
        return cls._hits

x = TrapAtrist('Mrinal')
print(x.hits())
print(x._hits)
# Now, Let's try and modify it.
x._hits = ['apple', 'banana', 'cat']
# Now when we call the hits function it actually doesnot modify the thingself.
# It is because it is a classmethod
print(x.hits())
