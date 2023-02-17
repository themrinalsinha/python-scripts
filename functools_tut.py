# Functools: it is for higher order function, it treats the functions as objects (arguments)
# manipulate the functions and return them as output.
# functools is used to make your code look more elegant and readable. (sometimes efficient)


# ======================================================================================
# functools.reduce() is used to apply a function to an iterable and reduce it to a single cumulative value.
from functools import reduce
items = [1, 2, 3, 4, 5]
# sum of list (rolling computation)
# 1 2 3 4 5
# 3 3 4 5
# 6 4 5
# 10 5
# 15
# to do this using reduce function.
# reduce(function, iterable, initializer)
sum = reduce(lambda x, y: x + y, items)
max = reduce(lambda x, y: max(x, y), items)
# NOTE: if you don't provide initializer, it will take first element as initializer.
_sum = reduce(lambda x, y: x + y, items, 10) # with initializer
print(sum, max, _sum)

# ======================================================================================
