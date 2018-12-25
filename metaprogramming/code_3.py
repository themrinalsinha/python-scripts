# Signatures (Python3 features)

# In python3 you can construct functions signature objects yourself.
# -> Build a function signaure object
# from inspect import Parameter, Signature
# fields = ['name', 'shares', 'price']
# parms  = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in  fields]
# sig    = Signature(parms)
#
# Signature are more than just metadata.

from inspect import Parameter, Signature
_fields = ['name', 'share', 'price']
_params = [Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD) for fname in _fields]
print(_params)

sig = Signature(_params)
print(sig)

