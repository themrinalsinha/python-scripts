# ========================================
# ==== SIMPLE DEBUGGING WITH F-STRING ====
# ========================================

# f-string were introduced in python3.6 and have become very popular.
# they might be the most common reason for python libraries only being
# supported on version 3.6 and later. An f-string is a formatted string
# literal. you can recognize it by leading f

# eg 1
style = 'formatted'
print(f'This is a {style} string')

# eg 2
import math
r = 3.6
print(f'A circle with {r} has area {math.pi * (r ** 2):.2f}')

# NOTE: In python3.8, you can use assignment expression inside f-string.
# just make sure to surround the assignment expression with parenthesis.

r = 3.8
print(f'Diameter {(diam := 2*r)} gives circumference {math.pi*diam:.2f}')
# However, the real f-news in python3.8 is the new debugging specifier.
# you can now add = at the end of an expression, and it will print both
# the expression and its value.

python = 3.8
print(f'{python=}')
# this is a short-hand, that typically will be most useful when working
# interactively or adding print statement to debug your script. In earlier
# version of python, you need to spell out the variable or expresion twice
# to get the same information.
python = 3.7
print(f'python={python}')
name = 'Eric'
print(f'{name = }')

print(f'{name = :>10}')
# the >10 format specifier says that name should be right-aligned within
# a 10 character string. = works for more complex expression as well.
print(f'{name.upper()[::-1] = }')
