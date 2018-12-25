# Signature Binding

# # -> Argument Binding
# def func(*args, **kwargs):
#     bound_args = sig.bind(*args, **kwargs)
#     for name, val in bound_args.arguments.items():
#         print(name, '=', val)
# # -> sig.bind() binds positional/keyword args to signature
# .arguments in an OrderdDict of passed values

from inspect import Parameter, Signature
_fields = ['name', 'share', 'price']
_params = [Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD) for fname in _fields]
sign    = Signature(_params)

def foo(*args, **kwargs):
    bound = sign.bind(*args, **kwargs)
    for name, value in bound.arguments.items():
        print(name, value)

foo(1, 2, 3)
# Notice: both positional/keyword args work

