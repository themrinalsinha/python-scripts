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

# Fantastic!
print('\n\n=====================================================\n\n')

