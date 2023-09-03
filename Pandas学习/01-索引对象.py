import pandas as pd
import numpy as np
obj = pd.Series(range(3), index=["a", "b", "c"])
index = obj.index
print("-----index-----")
print(index)
print("-----index[1:]")
print(index[1:])
index[1] = "d"

labels = pd.Index(np.arange(3))
print("-----labels-----")
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print("----obj2-----")
print(obj2)
print(obj2.index is labels)

import numpy as np
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns=["year", "state", "pop"])
print("-----frame-----")
print(frame)
print("-----frame.columus----")
print(frame.columns)
print('Ohio' in frame.columns)
print("2003" in frame.index)

import pandas as pd
dup_labels = pd.Index(["foo", "foo", "bar", "bar"])
print(dup_labels)













