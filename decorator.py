# Decorators
# A decorators is just a function that takes another function as an arguments and adds some kind of functionality.

def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('Display function ran...')

# # One way to using decorator
# decorated_display = decorator_function(display)
# decorated_display()

# Another way is to add @decorator_function on our display function

@decorator_function
def print_data():
    print('Hello there...')

print(print_data())