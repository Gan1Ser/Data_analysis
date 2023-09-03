import pandas as pd
import numpy as np
from pandas import Series, DataFrame

Series
obj = pd.Series([4, 7, -5, 3])
print(obj)
arr = obj.values
print(arr)
print(type(arr))
print(obj.index)

obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(obj2)
print(obj2.index)

print(obj2['a'])
obj2['d'] = 6
print(obj2[["c", "a", "d"]])
print("-----bool过滤-----")
print(obj2[obj2 > 2])
print("-----标量运算-----")
print(obj2 * 2)
print("-----矢量运算-----")
print(np.exp(obj2))

print('b' in obj2)
print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
# print(obj3)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print(obj4.index)

print(pd.isnull(obj4))
print(pd.notnull(obj4))

print(obj4.isnull())
print(obj4.notnull())

print('-----obj3-----')
print(obj3)
print('-----obj4-----')
print(obj4)
print('-----obj3 + obj4-----')
print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
obj4.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj4)

# DataFrame
import pandas as pd
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# print(frame)

print(frame.head())

frame1 = pd.DataFrame(data, columns=["year","state","pop"])
print(frame1)

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four','five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2.year)
print(frame2["state"])

print(frame2.loc["three"])

frame2["debt"] = 16.5
print(frame2)

frame2["debt"] = np.arange(6.)
print(frame2)
val = pd.Series([2, 3, 4], index=["three", 'two', 'six'], name='month')
frame2['debt'] = val
print(frame2)
frame2["eastern"] = frame2["year"] == 2003
print(frame2)

del frame2['eastern']
print(frame2)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)

print(frame3.T)
frame3 = pd.DataFrame(pop, index=[2001, 2002, 2003])
print(frame3["Ohio"][:-1])

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
frame4 = pd.DataFrame(pdata)
print(frame4)

print(frame3)
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3.values)

