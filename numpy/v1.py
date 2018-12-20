# Numpy is the fundamental package for scientific computing with python.
# -> A powerful N-dimmentional array object
# -> Sophisticated (broadcasting) function.
# -> tools for integrating c/c++ and fortran code.
# -> useful linear algebra, fourier transformation, and random number capabilities.

import numpy as np

# Numpy arrays
list_1 = [1.0, 2.0, 5.0, 32.5, 18.12] # regular array
print(type(list_1))

# converting regular array to np array.
np_array = np.array(list_1)
print(type(np_array))

# If you want to specifiy a certain type of array then
# you can define dtype
np_array_1 = np.array(list_1, dtype=np.float64)
print(np_array_1)

# here np_array or np_array_1 is an object of numpy. so we can use an apply lots of inbuild functions to it.

# To get dimension of array:-
print('Dimnesion: ', np_array.ndim)

# To get shape of array.
print('Shape: ', np_array.shape)

# To get size of array.
print('Size: ', np_array.size)

np_array = np.array([[1, 2, 3], [5, 6, 7], [4, 8, 9]])
print('\nDimension: {}\nShape: {}\nSize: {}'.format(np_array.ndim, np_array.shape, np_array.size))

# To get how much byte size does each element hold.
print('Itemsize: {} byte'.format(np_array.itemsize))

# To get size of total array.
print('Total Itemsize: {} bytes'.format(np_array.itemsize * np_array.size))

# to get datatype of array.
print('Datatype of array: ', np_array.dtype)
print('Datatype of array (name): ', np_array.dtype.name)
