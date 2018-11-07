# Python has an additional and interesting feature called decorators to add functionality
# to an existing code. This is also called as metaprogramming as a part of the program tries
# to modify another part of the program at compile time.

# DEMO 1: simple way to impletment function
print('\n======== DEMO 1 =========\n')
def make_decorated(function):
    def inner_function():
        print('I got decorated')
        function()
    return inner_function

def simple_function():
    print("I am a simple function")

decor = make_decorated(simple_function)
decor()

# DEMO 2: Another way of doing DEMO 1
print('\n======== DEMO 2 =========\n')
def _make_decorated(function):
    def _inner_func():
        print('I got decorated...')
        function()
    return _inner_func

@_make_decorated
def _simple_function():
    print('I am a simple function...')

_simple_function()
