import numpy as np

# 一元通用函数
arr = np.arange(10)
print(f'arr的值为{arr}')
print(f'np.sqrt(arr)的值为{np.sqrt(arr)}')
print(f'np.exp(arr)的值为{np.exp(arr)}')

# 二元通用函数
x = np.random.randn(8)
y = np.random.randn(8)

print('-----x-----')
print(x)
print('-----y-----')
print(y)
print('-----maximum(x, y)-----')
print(np.maximum(x, y))

# 返回多个数组
arr = np.random.randn(7) * 5
print('-----arr-----')
print(arr)
print(np.sqrt(arr, arr))
remainder, whole_part = np.modf(arr)
print('-----remainder-----')
print(remainder)
print('----whole_part-----')
print(whole_part)