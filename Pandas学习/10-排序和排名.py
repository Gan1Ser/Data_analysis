import numpy as np
import pandas as pd
#
# obj = pd.Series(range(4), index=["d", "a", "b", "c"])
# print("-----obj.sort_index()")
# print(obj.sort_index())

# 对于DataFrame，则可以根据任意一个轴上的索引进行排序：
# import numpy as np
# import pandas as pd
#
# frame = pd.DataFrame(np.arange(8).reshape((2,4)),
#                     index = ["three", "one"],
#                     columns = ["d", "a", "b", "c"])
# print("-----frame.sort_index()-----")
# print(frame.sort_index())
# print("-----frame.sort_index(axis=1)----")
# print(frame.sort_index(axis=1))
# print("-----frame.sort_index(axis=1, ascending=False)")
# print(frame.sort_index(axis=1, ascending=False))

# 若要按值对Series进行排序，可使用其sort_values方法
# obj = pd.Series([4, 7, -3, 2])
# print("-----obj.sort-values()-----")
# print(obj.sort_values())

# 在排序时，任何缺失值默认都会被放到Series的末尾
# obj = pd.Series([4, np.nan, 7, -3, 2])
# print(obj.sort_values())

# frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1], "c": [9, -10, 3, 4]})
# print("-----frame-----")
# print(frame)
# print("----frame.sort_values(by='b')-----")
# print(frame.sort_values(by='b'))

# 要根据多个列进行排序，传入名称的列表即可
# print("----frame.sort_values(by=['a', 'b'])-----")
# print(frame.sort_values(by=['a', 'b']))
# print("----frame.sort_values(by=['a'])-----")
# print(frame.sort_values(by=['a']))

# rank 排名
# obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
# print("-----obj.rank()-----")
# print(obj.rank())
# # 也可以根据值在原数据中出现的顺序给出排名
# print("----obj.rank(method = 'first')")
# print(obj.rank(method = 'first'))
# # 降序排名
# print("-----obj.rank(ascending=False, method='max')-----")
# print(obj.rank(ascending=False, method="max"))
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],'c': [-2, 5, 8, -2.5]})

print("-----frame-----")
print(frame)
print("-----frame.rank(axis='columns')")
print(frame.rank(axis=1))
