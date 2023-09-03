# 使用array函数，将序列型的对象（包括其他数组）转换成一个Numpy数组。
import numpy as np
data1 = [1, 2, 3.4, 7, 0]
arr1 = np.array(data1)
print(arr1.shape)

# 嵌套序列
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

# 全零/全一/空数组的创建
print('----全零数组-----')
data3 = np.zeros((18))
print(data3)
print('-----全一数组-----')
data4 = np.zeros((3,6))
print(data4)
print('-----空数组-----')
data5 = np.empty((2,3,3)) # 认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
print(data5)

# arange
print('-----arange-----')
data6 = np.arange(16)
print(data6)