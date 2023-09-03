import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

# # # 通过标签选择一行和多列
# print("loc选择一行和多列")
# print(data.loc['Colorado', ['two', 'three']])
# # 用iloc和整数进行选取
# print("用iloc和整数进行选取")
# print(data.iloc[[1,2], [3,0,1]])

# 索引函数适用于一个标签或多个标签的切片
# print(data.loc[:"Utah", 'two'])
# print(data.iloc[:, :2][data.three > 3])
