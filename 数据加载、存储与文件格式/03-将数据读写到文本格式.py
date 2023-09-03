import pandas as pd
import numpy as np
data = pd.read_csv("examples/ex5.csv")
print("-----data-----")
print(data)

data.to_csv("examples/out.csv")

# 其他分割符
import sys
data.to_csv(sys.stdout, sep="|")

# 替换缺失值
data.to_csv(sys.stdout, na_rep="NULL", sep = "|")

# 禁用列和行
data.to_csv(sys.stdout, index=False, header=False)

# 只显示部分列
data.to_csv(sys.stdout, index=False, columns=["a", "b", "c"])

# Series的to_csv
dates = pd.date_range("1/1/2000", periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv("examples/tseries.csv")
print(pd.read_csv("examples/tseries.csv"))