#dtype
import numpy as np
arr1 = np.array([1, 2, 3], dtype = np.float64)
arr2 = np.array([1.3, 2.1, 3.8], dtype = np.int32)
print(arr1, '\n' ,arr1.dtype)
print(arr2, '\n' ,arr2.dtype)

# astype转换dtype
arr = np.array([1.1, 2.2, 3.3, 4.6, 5.7])
print(arr.dtype)
int_arr = arr.astype(np.int64)
print(int_arr)
print(int_arr.dtype)

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype = np.string_)
print(numeric_strings)
arr_string = numeric_strings.astype(np.float64)
print(arr_string, arr_string.dtype)

# dtype另外的属性
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)
print(int_array.dtype)