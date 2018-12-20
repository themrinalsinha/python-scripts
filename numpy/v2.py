import numpy as np

# To create zero array (we have to pass dimention and datatype of array)
zero_array = np.zeros((5, 3), dtype=np.int64)
print(zero_array)

# To create ones array.
ones_array = np.ones((5, 3), dtype=np.int64)
print(ones_array)

# To create a arry and certain shape with junk value.
empty_array = np.empty((5, 3), dtype=np.float64)
print(empty_array)

# To create array with just indices.
indices = np.indices((5, 3))
print('\n')
print(indices)

indices = np.indices((5, 3, 2))
print('\n')
print(indices)

# To create an identity matrix.
identi_1 = np.eye(5, dtype=np.int64)
print(identi_1)
# or another method is...
identi_1 = np.identity(5, dtype=np.int64)
print(identi_1)

# create a matrix with random indexes.
rand = np.random.random((3, 5))
print(rand)

rand = np.random.uniform(low=-5, high=5, size=(3, 5))
print(rand)
