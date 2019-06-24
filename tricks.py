# ====== Trick 1 =====================
class A(object):
    def __init__(self):
        self.name = 'Hello'

a = A()
b = None
x = a and a.name or 0
y = b and a.name or 0
print(x)
print(y)
# ==================================

# Tuple can be mutable if it has a
# mutable elemnt linke list in it.

# ==================================
atoz = ''.join([chr(x) for x in range(ord('a'), ord('z'))])
print(atoz)

# trict
# counter < len(list) and counter + 1 or 0
# =================================

# cyclic function python
# c = cycle(list of employees)
# t.assign_to(next(c))
from itertools import cycle
x = cycle([1,2,3,4,5])
print(x)
# for i in x:
#     print(i)

# =================================
# for database
# Concurrency -- i. optimistic
#                ii. Pressimistic
# django omitmistic and Pressimistic
# approaches for Concurrency
# ================================

# Getting current process id
import os
print('Process ID: ', os.getpid())
# =================================

# Printing imported modules
import sys
imported_modules = [m.__name__ for m in sys.modules.values() if m]
print('Imported modules\n', imported_modules, '\n')
# =================================
name  = ['a', 'b', 'c', 'd']
index = [1, 2, 3, 4]
data  = zip(index, name)
print('zipped data: ', data)
print('unzipping data: ', *data)
