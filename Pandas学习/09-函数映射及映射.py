import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'),
                    index=["Utah","Ohio","Texas","Oregon"])
print("-----frame-----")
print(frame)
print("-----np.abs(frame)-----")
print(np.abs(frame))

# 另一个常见的操作是，将函数应用到由各列或行所形成的一维数组上。DataFrame的apply方法即可实现此功能：
# f = lambda x: x.max() - x.min()
# print("----frame.apply(f)----")
# print(frame.apply(f))
# print(frame.apply(f, axis="columns"))

# 传递到apply的函数不是必须返回一个标量，还可以返回由多个值组成的Series：
# def f(x):
#     return pd.Series([x.min(),x.max()], index=["min", "max"])
# print(frame.apply(f))

# 元素级的Python函数也是可以用的。假如你想得到frame中各个浮点值的格式化字符串，使用applymap即可：
format = lambda x: "%.2f" % x
#
# print(frame.applymap(format))

# 之所以叫做applymap，是因为Series有一个用于应用元素级函数的map方法
print(frame["d"].map(format))