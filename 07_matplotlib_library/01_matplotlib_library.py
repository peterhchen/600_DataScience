# Import Python Packages
import numpy as np
import matplotlib.pyplot as plt

# Computer x and y coordinates for point on sine curve
x = np.arange (0, 3 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.title ("sine/cosine wave form")

# plot the points by matplotlib
plt.plot (x, y)
plt.plot (x, z)
plt.show ()
