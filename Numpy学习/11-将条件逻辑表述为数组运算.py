import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# 列表推导式的写法
result = [(x if c else y) for x, y, c in zip (xarr, yarr, cond)]
print(result)

# np.where写法
result = np.where(cond, xarr, yarr)
print(result)

arr = np.random.randn(4, 4)
print('-----arr-----')
print(arr)
bool_arr = arr > 0
print('-----bool_arr-----')
print(bool_arr)
# z = np.where(bool_arr, 2, -2)
z = np.where(bool_arr, 2, arr)
print('-----z-----')
print(z)