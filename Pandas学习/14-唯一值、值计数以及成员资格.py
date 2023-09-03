import pandas as pd
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

print("-----obj.unique()-----")
uniques = obj.unique()
print(uniques)

# value_counts用于计算一个Series中各值出现的频率
print("-----obj.value_counts()-----")
print(obj.value_counts())
# isin用于判断矢量化集合的成员资格，可用于过滤Series中或DataFrame列中数据的子集
print("-----obj-----")
print(obj)
print("-----obj.isin(['b', 'c'])-----")
print(obj.isin(["b", "c"]))
print("-----obj[mask]-----")
print(obj[obj.isin(["b", "c"])])

# 与isin类似的是Index.get_indexer方法，它可以给你一个索引数组，从可能包含重复值的数组到另一个不同值的数组
to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
unique_vals = pd.Series(["c", "b", "a"])
print(pd.Index(unique_vals).get_indexer(to_match))

# 树状图
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],'Qu2': [2, 3, 1, 2, 3],'Qu3': [1, 5, 2, 4, 4]})
print("-----data-----")
print(data)

# 将pandas.value_counts传给该DataFrame的apply函数，就会出现
print("柱状图")
result = data.apply(pd.value_counts).fillna(0)
print(result)