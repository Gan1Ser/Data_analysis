import pandas as pd
import numpy as np
obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print("-----obj-----")
print(obj)

print("----obj['b']------")
print(obj['b'])
print("----obj[1]------")
print(obj[1])
print("----obj[2:4]------")
print(obj[2:4])
print("----obj[['b', 'a', 'd']]------")
print(obj[['b', 'a', 'd']])
print("----obj[[1,3]]------")
print(obj[[1,3]])
print("-----obj[obj < 2]-----")
print(obj[obj < 2])


print(obj['b':'c'])
obj["b":"c"] = 5
print(obj)

data = pd.DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
print("-----data-----")
print(data)

print("-----data['two']-----")
print(data["two"])
print("-----data[['three', 'one']]-----")
print(data[['three', 'one']])

# 切片选择
print("切片选择")
print(data[:2])
# 布尔筛选
print("布尔筛选")
print(data[data["three"] > 5])
bools = data < 5
print("-----bools----")
print(bools)

data[data < 5] = 0
print(data)












































