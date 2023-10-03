import pandas as pd
import numpy as np
frame = pd.DataFrame({"a": np.random.randn(100)})
store = pd.HDFStore("mydata.h5")
store["obj1"] = frame
store["obj1_col"] = frame["a"]

print(store)

print("------")
print(store["obj1"])
print(store["obj1_col"])

print("-----")
store.put("obj2", frame, format="table")
print(store.select("obj2", where=['index >= 10 and index <= 15']))
store.close()
print("-----")
frame.to_hdf("mydata.h5", "obj3", format="table")
print(pd.read_hdf("mydata.h5", "obj3", where=["index<5"]))
