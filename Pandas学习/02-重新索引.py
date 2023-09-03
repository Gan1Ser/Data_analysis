import pandas as pd
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
# print("-----obj----")
# print(obj)1

# reindex
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
# print("-----obj2-----")
# print(obj2)

obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print("-----obj3-----")
print(obj3)

# method, ffill
obj4 = obj3.reindex(range(6), method="ffill")
print(obj4)

import pandas as pd
import numpy as np
frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=["a", "b", "d"], columns=['Ohio', 'Texas', 'California'])
print("-----frame-----")
print(frame)

frame2 = frame.reindex(["a", "b", "c", "d"])
print("-----frame2-----")
print(frame2)

# 列可以用columns关键字重新索引
states = ["Texas", "Utah", "California"]
print(frame.reindex(columns=states))
















