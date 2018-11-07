

def decorator_function(orignal_function):
    def wrapper_function(*args, **kwargs):
        print('Executed before {} function'.format(orignal_function.__name__))
        result = orignal_function(*args, **kwargs)
        print('Executed after {} function.\n'.format(orignal_function.__name__))
        print(result)
    return wrapper_function

@decorator_function
def display_function(name, age):
    print('Dispaly info ran with arguments ({}, {})'.format(name, age))

display_function('John', 12)
