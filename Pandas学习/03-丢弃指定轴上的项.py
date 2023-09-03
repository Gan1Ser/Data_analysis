import pandas as pd
import numpy as np
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
# print("-----obj-----")
# print(obj)

# new_obj = obj.drop("c")
# print("----now_obj-----")
# print(new_obj)

# new_obj1 = obj.drop(["a", "b"], inplace=True) # 列表
# print(new_obj1)

obj.drop(["a", "b"], inplace=True) # 列表
print(obj)

# import pandas as pd
# import numpy as np
# data = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
# print("-----data-----")
# print(data)
#
# # 用标签序列调用drop会从行标签（axis 0）删除值
# print(data.drop(['Colorado', 'Ohio']))
#
# # 通过传递axis=1或axis='columns'可以删除列的值：
# print(data.drop("two", axis=1))
# print(data.drop(["two", "four"], axis="columns"))


































