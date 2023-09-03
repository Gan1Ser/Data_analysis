import pandas as pd
# print("-----read_csv-----")
# df = pd.read_csv("examples/ex1.csv")
# print(df)

# 还可以使用read_table，并指定分隔符
# print("-----read_table-----")
# print(pd.read_table("examples/ex1.csv", sep=","))

# 并不是所有文件都有标题行
# print("-----read_csv默认列名-----")
# print(pd.read_csv("examples/ex2.csv", header=None))
# print("-----read_csv指定列名-----")
# print(pd.read_csv("examples/ex2.csv", names=['a', 'b', 'c', 'd', 'message']))

# 将message列做成DataFrame的索引
# names = ['a', 'b', 'c', 'd', 'message']
# print("-----指定names-----")
# print(pd.read_csv("examples/ex2.csv", names = names, index_col="message"))

# 将多个列做成一个层次化索引
# print("-----csv_mindex.csv-----")
# print(pd.read_csv("examples/csv_mindex.csv"))
# print("层次化索引")
# print(pd.read_csv('examples/csv_mindex.csv', index_col=["key1", "key2"]))

# 不是用固定的分隔符去分隔字段的（比如空白符或其它模式）
# print("-----ex3.txt-----")
# print(pd.read_csv('examples/ex3.txt'))
#
# print("规整")
# result = pd.read_table("examples/ex3.txt", sep="\s+")
# print(result)

# 用skiprows跳过文件的第一行、第三行和第四行
# print("原")
# print(pd.read_csv("examples/ex4.csv"))
# print("规整")
# print(pd.read_csv("examples/ex4.csv", skiprows=[0, 2, 3]))

# 缺失值处理
print("原")
print(pd.read_csv("examples/ex5.csv"))
print("规整")
print(pd.isnull(pd.read_csv("examples/ex5.csv")))
print("na_values")
print(pd.read_csv('examples/ex5.csv', na_values=['NULL']))
print("字典")
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(pd.read_csv('examples/ex5.csv', na_values=sentinels))

