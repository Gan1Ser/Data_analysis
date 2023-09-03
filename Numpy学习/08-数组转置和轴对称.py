import numpy as np

# 转置T
arr = np.arange(15).reshape((3,5))
print(f'arr的值为：{arr}')
print(f'arr的值为：{arr.T}')

# 矩阵内积
arr = np.random.randn(6, 3)
print(f'arr的值为{arr}')
print(f'np.dot(arr.T, arr)的值为{np.dot(arr.T, arr)}')

# # 高纬数组转置
arr = np.arange(16).reshape((2, 2, 4))
print(f'arr的值为{arr}')
print(f'arr.transpose((1,0,2))的值为{arr.transpose((0, 2, 1))}')

# swapaxes
arr = np.arange(16).reshape((2, 2, 4))
print(f'arr.swapaxes(1,2)的值为{arr.swapaxes(1,2)}')