import pandas as pd
import numpy as np

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                  [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print("-----df-----")
print(df)

# 调用DataFrame的sum方法将会返回一个含有列的和的Series
print("-----df.sum()-----")
print(df.sum())

# 传入axis='columns'或axis=1将会按行进行求和运算
print("-----df.sum(axis=1)-----")
print(df.sum(axis="columns"))
print(df.mean(axis=1, skipna=False))

# 有些方法（如idxmin和idxmax）返回的是间接统计（比如达到最小值或最大值的索引）
print("-----df.idmix()-----")
print(df.idxmin())
print("-----df.idmax()-----")
print(df.idxmax())

# 另一些方法则是累计型的
print("-----df.cumsum()-----")
print(df.cumsum())

# 非累计非简约型
print("-----df.describe()-----")
print(df.describe())

# 对于非数值型数据，describe会产生另外一种汇总统计
obj = pd.Series(["a", "a", "b", "c"] * 4)
print("-----obj-----")
print(obj)
print("-----obj.describe()-----")
print(obj.describe())