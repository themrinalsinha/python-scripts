from functools import partial, wraps

def background_task(method=None, queue='default', timeout=600):
    print('METHOD: ', method)
    if method is None:
        return partial(background_task, queue=queue, timeout=timeout)

    def start(a, b, **kwargs):
        print('\nstart function called')
        print('start -> A -> ', a)
        print('start -> B -> ', b)
        print('start -> kwargs -> ', kwargs)

    @wraps(method)
    def wrapper(*args, **kwargs):
        print('\nwrapper function called')
        print('wrapper -> args -> ', args)
        print('wrapper -> kwargs -> ', kwargs)
    wrapper.start = start
    return wrapper

@background_task()
def add(a, b):
    return a + b

print(add(12, 12))
print(add.start(12, 12))

# ================= FUNCTOOLS.PARTIAL =================
# partial object - they are callable objects created by partial().
# They have 3 read-only attributes:
#   -> partial.func
#   -> partial.args
#   -> partial.keywords

# This function return a new partial object which when called will
# behave like func called with the positional arguments args and keyword
# arguments keywords. If more arguments are supplied to the call, they are
# appended to args. If additional keywords arguments are supplied, they
# extend and override keywords.

def partial(func, *args, **keywords):
    def newFunc(*fargs, **fkeywords):
        newKeywords = keywords.copy()
        newKeywords.update(fkeywords)
        return func(*(args + fargs), **newKeywords)
    newFunc.func = func
    newFunc.args = args
    newFunc.keywords = keywords
    return newFunc

# # IMPORTANT
# # The partial() is used for partial function application which 'freezes'
# # some portion of a functions arguments and/or keywords resulting in a new
# # object with a simplified signature.

# # Eg. partial() can be used to create a callable that behaves live the int()
# # function where the base arguments default to two.
# from functools import partial
# print('\nUSING PARTIAL FUNCTION//')
# basetwo = partial(int, base=2)
# print(basetwo.__doc__)
# print(basetwo('10010'))
