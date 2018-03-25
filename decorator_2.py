def decorator_func(function):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed -> {}'.format(function.__name__))
        return function(*args, **kwargs)
    return wrapper_func

# @decorator_func
# def display():
#     print('Display function ran.')

# @decorator_func
# def display_info(name, age):
#     print('Display info ({}, {})'.format(name, age))

# display_info('John', 25)

# ===========================================
# Decorator class.

class decorator_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Call method executed this -> {}'.format(self.func))
        return self.func(*args, **kwargs)

@decorator_class
def display_info(name, age):
    print('Display info ({}, {})'.format(name, age))

display_info('Mrinal Sinha', 23)