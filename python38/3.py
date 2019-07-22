# For Debugging Ease, f-strings now support =
# source: https://bugs.python.org/issue36817?source=post_page---------------------------

# This is an improvement to the f-strings. The specifier “=” can be added to the f-strings now.

# f -strings are in the form of f'{expr=}' Notice the ‘=’. The equal sign essentially evaluates
# the expression and prints the result too.

# Let’s understand this with an example.

# Imagine there are two variables “input ”and “output”, and we want to print “input-output” along
# with the result. We can use the f-strings=

input  = 100
output = 50
print(f'{input-output=}')
# This would now print input-output=50.

# As a result, it could make the code neater as we do not need to copy the formula on the right
# hand side of the “=” to evaluate it, and the side effect is that it can be used extensively during debugging.


