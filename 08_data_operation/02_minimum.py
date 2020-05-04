# Minimum dimensions
import numpy as np
a = np.array([1, 2, 3, 4, 5], ndmin = 1)
print ('a:\n', a)
# [1 2 3 4 5]
b = np.array([1, 2, 3, 4, 5], ndmin = 2)
print ('b:\n', b)
# [[1 2 3 4 5]]
c = np.array([1, 2, 3, 4, 5], ndmin = 3)
print ('c:\n', c)
# [[[1 2 3 4 5]]]