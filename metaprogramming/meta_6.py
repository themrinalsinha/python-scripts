# Defining a New Metaclass.
#   -> You typically inherit from type and redefine __new__ or __init__

class mytype(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        return clsobj

# To use this metaclass.
class Spam(metaclass=mytype):
    pass

# Using a Metaclass
# -> Metaclasses get information about class definition at the time of definition
#       -> can inspect this data
#       -> can modify this data
# -> Essesntially, similar to class decorator
# Metaclasses propagate down hierarchies
#
# class Base(metaclass=mytype):
#   ....
#
# class Spam(Base): # metaclass=mytype
#   ....
#
# class Grok(Spam): # metaclass=mytype
#   ....
#
# Think of it as a genetic mutation

# Solution: Reprise
class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__name__(cls, clsname, bases, clsdict)
        clsobj = debugmethods(clsobj)
        return clsobj

# Idea:
# -> class gets created normally
# -> Immediately wrapped by class decorator

