# Making your python decorators even better, with functool.wraps

# a simple decorator - it takes a
# functions output and puts it into a string
def mydeco(func):
    def wrapper(*args, **kwargs):
        '''
        Just a fucking wrapper
        '''
        return f'{func(*args, **kwargs)}!!!'
    return wrapper

@mydeco
def add(a, b):
    '''
    This is an add function
    '''
    return a + b

@mydeco
def mysum(*args):
    '''
    This is my sum funciton
    '''
    return sum(args)

print(add(1, 2))
print(add.__doc__)
print(mysum(1, 2, 3, 4, 5))
print(mysum.__doc__)

# Fantastic! We get each function's result back, as a string, with
# the exclamation points the decorator worked, But there are few issues
# which we noticed, eg. if we ask for function name or doc it returns
# wrapper docstring or name, to fix this we use wraps from functools.

# There is a way to solve this partially, by assigning the __name__ and __doc__
# attributes in our decorator.
# eg:
def mydeco(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!!'
    wrapper.__name__ = func.__name__
    wrapper.__doc__  = func.__doc__
    return wrapper

@mydeco
def add(a, b):
    '''
    This is an add function
    '''
    return a + b

@mydeco
def mysum(*args):
    '''
    This is my sum funciton
    '''
    return sum(args)

print(add(1, 2))
print(add.__doc__)
print(mysum(1, 2, 3, 4, 5))
print(mysum.__doc__)
print('\n\n========================FUNCTOOLS.WRAPS=============================\n\n')

# The good news is that we've now fixed the naming adn the docstring
# problem. But the function signature is still the super-generic one,
# looking for both *args and **kwargs.

from functools import wraps

def mydec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper

@mydeco
def add(a, b):
    '''
    This is an add function
    '''
    return a + b

@mydeco
def mysum(*args):
    '''
    This is my sum funciton
    '''
    return sum(args)

print(add(1, 2))
print(add.__doc__)
print(mysum(1, 2, 3, 4, 5))
print(mysum.__doc__)
