from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

chart = plt.figure()

# 111: 1x1 grid, first subplot
# 234: 2x3 grid, 4th subplot
chart3d = chart.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data (0.08)

print('X:')
print(X)
print('Y:')
print(Y)
print('Z:')
print(Z)
chart3d.plot_wireframe(X, Y, Z, color='r', rstride=15, cstride=10)
plt.show()
