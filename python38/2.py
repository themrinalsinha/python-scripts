# Position-only parameters(/)
# source: https://www.python.org/dev/peps/pep-0570/?source=post_page---------------------------

# If you want to call a function in Python that accepts parameters
# then you can pass the arguments by position or by keyword.

# But what if we want to restrict the callers of our API to only call our function
# by passing in parameters by position? What if our parameter names do not make
# sense to the external world (for what ever reason) OR we might be planning to
# rename the parameters in the future AND we want to make our API backwards compatible?

# The positional-only parameter functionality “/” solves it.

def add(a, b, c, d=None, /):
    x = a+b+c
    if d: x += d
    return x

print(add(1,2,3))
# print(add(a=1, b=2, c=3, d=4)) # will throw error

# Subsequently, add(1,2,3) and add(1,2,3,4) are valid calls.
# add(a=1,b=2,c=3) or add(1,2,3,d=4) are all invalid calls.

# The result of the “/” parameter indicates that the function accepts positional-only
# parameters and thus the arguments must be mapped to the parameters based solely on their order.

