
def prefix_decorator(prefix):
    def decorator_function(orignal_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, ' Executed before...')
            result = orignal_function(*args, **kwargs)
            print(prefix, ' Executed after...')
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TESTING: ')
def display_function(name, age):
    print('Display info ran with arguments ({}, {})'.format(name, age))

display_function('Mrinal', '23')
