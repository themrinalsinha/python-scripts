# Solution with Signatures

from inspect import Parameter, Signature

# Make a utility signature function then inforce __init__ function to use this signature.

def make_signature(names):
    signature = Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)
    return signature

class Structure(object):
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            setattr(self, name, value)
