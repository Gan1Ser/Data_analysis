import numpy as np
# 一维数组
arr = np.arange(10)
print(f'arr[1:6]的值为{arr[1:6]}')

# 二位数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'arr2d的值为{arr2d}')
print(f'arr2d[:2]的值为{arr2d[:2]}')
print(f'arr2d[:2, 1:]的值为{arr2d[:2, 1:]}')
print(f'arr2d[1, :2]的值为{arr2d[1, :2]}')
print(f'arr2d[:2, 2]的值为{arr2d[:2, 2]}')
print(f'arr2d[:, :1]的值为{arr2d[:, :1]}')
arr2d[:2, 1] = 88
print(arr2d)
