# Things cover
# -> Using assignement expression to simplify some code constructs
# -> Enforcing position-only arguments in your own functions
# -> Spedifying more precise type hints
# -> Using f-string for simpler debugging

# =======================================================
# ==== The walrus in the room: Assignment Expression ====
# =======================================================

# The biggest change in python3.8 is the introduction of assignment
# expressions. They are written in new notion (:=)
# NOTE: Assignemnt expression allows you to assign and return a value
# in the same expression. Eg:
print('\nwithout using assignment operator')
walrus = False
print(walrus)

# In python 3.8, you're allowed to combine these two statements into one,
# using walrus operator:
print('\nwith using assignment operator')
print(walrus := True)

# Better use
print('\nwhile loop without walrus operator')
inputs  = list()
while True:
    current = input('Write something: ')
    if current == 'quit':
        break
    inputs.append(current)
print('INPUTS: ', inputs)

print('\nwhile loop with walrus operator')
inputs = list()
while (current := input('write something: ')) != 'quit':
    inputs.append(current)
print('INPUTS: ', inputs)


# ===================================
# ==== Positional-Only Arguments ====
# ===================================

# The built-in function float() can be used for converting text strings
# and numbers to float objects, consider the following example.
print(float('3.8'))

# >>> help(float)
# class float(object)
#  |  float(x=0, /)
#  |
#  |  Convert a string or number to a floating point number, if possible.

# Look closely at the signature of float(). Notice the slash(/) after the parameter.
# It turns out that while the one parameter of float() is called x, you're not allowed
# to use its name.

# >>> float(x="3.8")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: float() takes no keyword arguments

# eg:
print('\nwithout positional argument')
def incr(x):
    return x+1
print(incr(3.8))
print(incr(x=3.8))

print('\nwith positional argument')
def incr(x, /):
    return x+1
print(incr(3.8))
try:
    print(incr(x=3.8))
except Exception as e:
    print(e)

# by adding / after x, you specify that x is a position-only argument. you can combine
# regular arguments wit position-only ones by placing the regular arguments after that slash.

# What happend when / is placed between two arguments.
print('\nWhen / is placed between two arguments ')
def greet(name, /, greeting='Hello'):
    return f'{greeting}, {name}'

print(greet('Mrinal'))
print(greet('Mrinal', greeting='Hi'))
try:
    print(greet(name='Mrinal', greeting='Hey'))
except Exception as e:
    print(e)
# in greet(), the slash is placed between name and greeting, this means that name is a
# position-only argument, while greeting is a regular argument that can be passed either
# by position or by keyword

# position-only arguments nicely complement keyword-only arguments, in any-version of
# python3, you can specify keyword-only arguments using the star(*). any argument after
# must be spcified using a keyword.
print('\nkeyowrd only argument')
def to_fahrenheit(*, celsius):
    return 32 + celsius * 9/5

try:
    print(to_fahrenheit(40))
except Exception as e:
    print(e)
print(to_fahrenheit(celsius=40))
# celcius is a keyword-only argument, so python raises an error if you try to spedify
# it based on position, without the keyword.
