import numpy as np
import matplotlib.pyplot as plt

x = np.arange (0, 10)
print ('x:', x)
print ('2 binary:', bin(2))
print ('x binary:')
for x1 in x:
       print (bin(x1))
y = x ^ 2
print ('y:', y)
print ('y binary = x ^ 2:')
i = 0
for x1 in x:
       print ('{0:08b}'.format(y[i]),' = ','{0:08b}'.format(x1), '^', '{0:08b}'.format(2))
       i = i + 1
plt.plot(x, y)
plt.show()
