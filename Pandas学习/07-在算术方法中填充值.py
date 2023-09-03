import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
# df2.loc[1, 'b'] = np.nan
#
# print("-----df1-----")
# print(df1)
# print("-----df2-----")
# print(df2)
# print("-----df1 + df2-----")
# print(df1 + df2)
#
# # 使用df1的add方法，传入df2以及一个fill_value参数
# print("-----使用df1的add方法，传入df2以及一个fill_value参数-----")
# print(df1.add(df2, fill_value=0))

# print(1/df1)
# print(df1.rdiv(1))
print(df1.reindex(columns=df2.columns, fill_value=00))