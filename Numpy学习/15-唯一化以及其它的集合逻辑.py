import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
arr2 = np.unique(ints)
print(np.unique(ints))
print(type(arr2))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2,3,6]))