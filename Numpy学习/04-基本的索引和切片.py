import numpy as np

# 一维数组
arr = np.arange(10)
print(f'arr的值为{arr}')

# 索引操作
print(f'arr[5]的值为{arr[5]}')

# 切片操作
print(f'arr[5:8]的值为{arr[5:8]}')

# 切片赋值操作
arr[5:8] = 12
print(f'赋值后arr的值为{arr}')

# 验证作用在源数组上
print('-----作用在源数组上-----')
arr_slice = arr[5:8]
print(f'arr_slice的值为{arr_slice}')
arr_slice[1] = 12345
print(f'arr_slice的值为{arr_slice}')
print(f'此时arr的值为{arr}')

import numpy as np

# 二维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])

print(arr2d[0][2])
print(arr2d[0, 2])

# 三维数组
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f'arr3d的值为{arr3d}')
print('\n')
print(f'arr3d[0]的值为{arr3d[0]}')

old_values = arr3d[0].copy()
arr3d[0] = 42 # 标量赋值
# print(f'arr3d的值为{arr3d}')
# print('\n')
arr3d[0] = old_values # 赋值数组
# print(f'arr3d的值为{arr3d}')

old_values[:] = 42
print(arr3d[0])
# print(arr3d[0])

print(f'arr3d[1,0]的值为{arr3d[1,0]}')
print(f'arr3d[1]的值为{arr3d[1]}')
print(f'arr3d[0]的值为{arr3d[0]}')