import pandas as pd

# 读取大文件时显示更加紧凑
pd.options.display.max_rows = 10
#
# result = pd.read_csv("examples/ex6.csv")
# print("-----result------")
# print(result)
# print("-----指定读取行数-----")
# print(pd.read_csv("examples/ex6.csv", nrows=5))

# 逐块读取文件，chunkersize
chunker = pd.read_csv("examples/ex6.csv", chunksize=1000)
print("-----逐块读取文件-----")
print(chunker)

print("-----通过地迭代将值计数聚合到key列中-----")
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece["key"].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])