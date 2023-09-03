import numpy as np



arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
# 同尺寸数组算数运算
print('-----乘法-----')
mul_arr = arr * arr
print(mul_arr)
print('-----减法-----')
sub_arr = arr - arr
print(sub_arr)

# 数组与标量算数运算
print('-----标量与数组-----')
scalar_arr = 1 / arr
print(scalar_arr)

# 数组之间的比较
print('-----大小相同的数组之间的比较------')
arr2 = np.random.randn(2,3)
bool_arr = arr2 > arr
print(arr2)
print(bool_arr)
