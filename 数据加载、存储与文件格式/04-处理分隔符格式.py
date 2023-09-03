import pandas as pd
import csv

# f = open("examples/ex7.csv")
# reader = csv.reader(f)
#
# for line in reader:
#     print(line)

# 规整数据格式
with open("examples/ex7.csv") as f:
    lines = list(csv.reader(f))
print("-----lines-----")
# print(lines)
print("=====规整数据-----")
# 将这些行分为标题行和数据行
header, values = lines[0], lines[1:]
print(header, values)

# 用字典构造式和zip(*values)，后者将行转置为列，创建数据列的字典
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)