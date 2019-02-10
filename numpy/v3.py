# Array's and function for plotting.

import numpy as np

# Creating grid point value
points = np.linspace(-10, 10, 201)
print('Grid points')
print(points)

# Another command to do the same is.
print('\nAnother method to generate grid point')
_points = np.arange(-10, 10.05, 0.1)
print(_points)

# ===========================================================
# The above two method is used to print/generate grid points.

# Lets plot sine curve.
sine = np.sin(points)
# show the sine plot on matplotlib graph
import matplotlib.pyplot as plt
plt.plot(points, sine)
plt.show()

# Working with quadratic on it.
quad_1 = points ** 2 + 2.0 * points + 5.0
plt.plot(points, quad_1)
plt.show()
