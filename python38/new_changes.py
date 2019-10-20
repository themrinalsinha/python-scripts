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

# # Better use
# print('\nwhile loop without walrus operator')
# inputs  = list()
# while True:
#     current = input('Write something: ')
#     if current == 'quit':
#         break
#     inputs.append(current)
# print('INPUTS: ', inputs)

# print('\nwhile loop with walrus operator')
# inputs = list()
# while (current := input('write something: ')) != 'quit':
#     inputs.append(current)
# print('INPUTS: ', inputs)


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


# ============================
# ==== More precise types ====
# ============================

# Python's typing system is quite mature at this point. However, in python3.8, some
# new features have been added to typing ao allow more precise typing.
# -> Literal types
# -> Typed dictonaries
# -> Final objects
# -> Protocols

print('\nsample typehint function')

def double(number: float) -> float:
    return 2 * number
print(double(4))
print(double("I'm not a float.."))
# As you can see above, double happily accepts string as an argument, even though
# that's not a float. There are libraries that can use types at runtime. but that
# is not that main use case for python's type system.
# NOTE: that are several static type checkers available, including Pyright, Pytype
# and Pyre. We'll use Mypy $ pip install mypy

# There are four new PEPs about type checking that have been accepted and included
# in Python 3.8. You’ll see short examples from each of these.

# PEP 586 introduce the Literal type. Literal is a bit special in that it represents
# one or several specific values. One use case of Literal is to be able to precisely
# add types, when string arguments are used to describe specific behavior. Consider the following example:

print('\nExample of Lateral Type check')
def draw_line(direction: str) -> None:
    if direction == 'H':
        print('*' * 10)
    elif direction == 'V':
        print('*\n' * 10)
    else:
        raise ValueError(f'invalid direction {direction!r}')

print('\ndrawing Horizontal line')
draw_line('H')

print('\ndrawing vertical line')
draw_line('V')

# if i pass 'up' as value that program will pass the static type checker,
# even though, 'up' is an invalid direction. The typechecker only checks that 'up'
# is a string, It would be more precise to say that direction must be either the lateral
# string "H" for horizontal or "V" for vertical

from typing import Literal

def draw_line(direction: Literal['H', 'V']) -> None:
    if direction == 'H':
        print('*' * 10)
    elif direction == 'V':
        print('*\n' * 10)
    else:
        raise ValueError(f'invalid direction {direction!r}')
print(draw_line('up'))

# By exposing the allowed values of direction to the type checker, you can now be warned
# about the error.
# $ mypy draw_line.py
# draw_line.py:15: error:
#     Argument 1 to "draw_line" has incompatible type "Literal['up']";
#     expected "Union[Literal['horizontal'], Literal['vertical']]"
# Found 1 error in 1 file (checked 1 source file)

