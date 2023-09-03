import numpy as np

# dot()
x = np.array([[1., 2., 3.], [4., 5., 6.]]) # 2,3
y = np.array([[6., 23.], [-1, 7], [8, 9]]) # 3,2
# print(x.dot(y))

# print(np.dot(x, np.ones(3)))

print(x @ np.ones(3))

from numpy.linalg import inv, qr
import numpy as np
X = np.random.randn(5, 5)
mat = X.T.dot(X)

print("-----inv(mat)-----")
print(inv(mat))
print('-----mat.dot(inv(mat))')
print(mat.dot(inv(mat)))
print("-----qr(mat)-----")
q,r = qr(mat)
print(r)