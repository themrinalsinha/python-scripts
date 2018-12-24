# Simple Mixins
# Python supports a simple type of multiple inheritance which allows
# the creation of Mixins. Mixins are a sort of class that is used to 'mix in'
# extra properties and methods into a class.

class Mixin1(object):
    def mix_1(self):
        return 'Mixin class 1'

class Mixin2(object):
    @property
    def mix_2(self):
        return 'Mixin class 2'

class MyClass(Mixin1, Mixin2):
    pass

obj1 = MyClass()
print(obj1.mix_1())
print(obj1.mix_2)

# However, in python the class hierarchy is define right to left, so in this
# case the Mixin2 class is the base class, extended by Mixin1 and finally by
# the BaseClass. This is usually fine because many times the mixin classes
# don't override each other's


# Mixins take various forms depending on the language, but at the end of the
# day they encapsulate behavior that can be reused in other classes.
#
# The delineation between using true inheritance and using mixins is nuanced,
# but it comes down to the fact that a mixin is independent enough that it
# doesn’t feel the same as a parent class. Mixins aren’t generally used on
# their own, but aren’t abstract classes either.

import logging

class LoggerMixin(object):
    @property
    def logger(self):
        name = '.'.join([self.__module__, self.__class__.__name__])
        return logging.getLogger(name)

# With this nicely encapsulated, we can now go around adding the following to our existing code.

class EssentialFunctioner(LoggerMixin, object):
    def do_the_thing(self):
        try:
            pass
        except BadThing:
            self.logger.error('Oh noes!')

class BusinessLogicer(LoggerMixin, object):
    def __init__(self):
        super().__init__()
        self.logger.debug('Giving the login the business')

# We wrote the functionality just once, but now we can use it everywhere! All we have
# to do is inherit from LoggerMixin and we can proceed using self.logger as if wee'd set
# that up in EssentialFunctioner and BusinessLogicer?



