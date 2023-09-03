import numpy as np
names = np.array(['chen', 'zhang', 'li', 'xu', 'zhao', 'chen'])
data = np.random.randn(6, 4)

print('-----names-----')
print(names)
print('-----data-----')
print(data)

print('-----Bool_Numpy-----')
bool_numpy = names == 'chen'
print(bool_numpy)
print('-----Bool索引-----')
print(data[bool_numpy])
print('-----Bool索引与切片等混用-----')
print(data[bool_numpy, :2])
print('\n')
print(data[bool_numpy, 1])
print('-----反转Bool结果-----')
print(data[~bool_numpy])
print('-----不一样的Bool结果-----')
bool_numpy = (names == 'chen') | (names == 'zhang')
print(bool_numpy)
print(data[bool_numpy])
print('-----通过Bool设置数值的值-----')
# data[data < 0] = 0
# print(data)
data[names != 'chen'] = 7
print(data)
