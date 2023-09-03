import numpy as np

arr = np.random.randn(5, 4)
print('-----arr-----')
print(arr)
print('----arr.mean()-----')
print(arr.mean())
print('----np.mean(arr)-----')
print(np.mean(arr))
print('-----arr.sum()-----')
print(arr.sum())

# 加入维度参数
print('----arr.mean(axis=1)-----')
print(arr.mean(axis=1))
print('-----arr.sum(axis=0)-----')
print(arr.sum(axis=0))

# cumsum和cumprod方法
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print('-----arr.cumsum()-----') #累加
print(arr.cumsum())
print('-----arr.cumprod()-----') #累乘
print(arr.cumprod())

# 多维数组
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("-----arr-----")
print(arr)
print("-----arr.cumsum(axis=0)-----")
print(arr.cumsum(axis=0))
print("-----arr.cumprod(axis=1)-----")
print(arr.cumprod(axis=1))
