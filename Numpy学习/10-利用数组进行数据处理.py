import numpy as np

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print('-----xs-----')
print(xs)
print('-----ys-----')
print(ys)
print('-----xs**2+ys**2-----')
z = xs ** 2 + ys ** 2
print(z)

import matplotlib.pyplot as plt
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
plt.title('Image plot of $\sqrt{x^2 + y^2}$ for a grid of values')
plt.show()