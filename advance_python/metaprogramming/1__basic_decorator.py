# Simple debugging problem

def debug_1(func):
    """
    func is function to be wrapped, which will help in debugging
    Basic debug decorator function that prints the function name
    """
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@debug_1
def add(x, y):
    return x + y

@debug_1
def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

add(2, 3)

# help(add)
# """ OUTPUT
# Help on function wrapper in module __main__:

# wrapper(*args, **kwargs)
# """
