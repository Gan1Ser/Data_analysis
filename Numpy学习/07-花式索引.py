import numpy as np
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
# print(arr)

# print(arr[[4,3,0,6]])
# print(arr[[-1, -2, -3, -4]])
# print(arr[[1,5,7],[0,3,1]])
print(arr[[1,5,7,2]][:,[0, 3, 1, 2]])