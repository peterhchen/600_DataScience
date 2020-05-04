# dtype parameter
import numpy as np
a = np.array([1, 2, 3], dtype=complex)
b = np.array([4+1j, 5+2j, 6+3j])
c = a * b
print('a\n', a)
# [1.+0.j 2.+0.j 3.+0.j]
print('b\n', b)
# [4.+0.j 5.+0.j 6.+0.j]
print('c\n', c)
# [4.+1.j 10.+4.j 18.+9.j]