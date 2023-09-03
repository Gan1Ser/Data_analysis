import numpy as np
data = np.random.randn(2,3)
print(type(data), '\n' ,data)
print("-----元素相乘-----")
data_mul = data * 10
print(type(data_mul), '\n' ,data_mul)
print("-----元素相加-----")
data_sum = data + data
print(type(data_sum), '\n' ,data_sum)
print('-----shape和dtype-----')
print(data.shape)
print(data.dtype)