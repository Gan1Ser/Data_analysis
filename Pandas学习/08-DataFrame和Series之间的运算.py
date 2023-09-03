# import numpy as np
# arr = np.arange(12.).reshape((3,4))
# print("-----arr-----")
# print(arr)
# print("-----arr[0]-----")
# print(arr[0])
# print("-----arr-arr[0]-----")
# print(arr-arr[0])
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(12.).reshape((4,3)),
                    columns=list("bde"),
                    index=["Utah", "Ohio", "Texas", "Oregon"])
series = frame.iloc[0]
print("-----frame-----")
print(frame)
print("-----series-----")
print(series)

# 默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列，然后沿着行一直向下广播
print("----frame-series-----")
print(frame-series)

# 如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运算的两个对象就会被重新索引以形成并集
series2 = pd.Series(range(3), index=["b", "e", "f"])
print("-----frame+series2-----")
print(frame+series2)

# 如果你希望匹配行且在列上广播，则必须使用算术运算方法。例如：
series3 = frame["d"]
print("-----frame-----")
print(frame)
print("-----series3-----")
print(series3)
print("-----frame.sub(series3, axis='index')")
print(frame.sub(series3, axis="index"))
