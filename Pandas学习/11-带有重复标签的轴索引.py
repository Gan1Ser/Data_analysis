import pandas as pd
import numpy as np
obj = pd.Series(range(5), index=["a", "a", "b", "b", "c"])
print("-----obj-----")
print(obj)
print("-----print(obj.index.is_unique)-----")
print(obj.index.is_unique)
print("-----obj['a']-----")
print(obj['a'])
print("-----obj['c']-----")
print(obj['c'])

# 这样会使代码变复杂，因为索引的输出类型会根据标签是否有重复发生变化。
# 对DataFrame的行进行索引时也是如此
df = pd.DataFrame(np.random.randn(4,3), index=["a", "a", "b", "b"])
print("------df-----")
print(df)
print("-----df.loc['b']-----")
print(df.loc['b'])