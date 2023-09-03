import numpy as np

# sort()
arr = np.random.randn(6)
print('----arr----')
print(arr)
print("----arr.sort()----")
arr.sort()
print(arr)

#多维数组，sort(axis)
arr = np.random.randn(5, 3)
print("----arr-----")
print(arr)
print("-----arr.sort(1)----")
arr.sort(1)
print(arr)

# 计算分位数
import numpy as np
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])
import numpy as np
arr = np.array([6, 47, 49, 15, 42, 41, 7, 39, 43, 40, 36])
arr.sort()
print("Q1 = ", arr[int(len(arr) * 0.25)])
print("Q2 = ", arr[int(len(arr) * 0.5)])
print("Q3 = ", arr[int(len(arr) * 0.75)])

