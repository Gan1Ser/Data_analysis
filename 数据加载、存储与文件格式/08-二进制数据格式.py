import pandas as pd

frame = pd.read_csv("examples/ex1.csv")
print(frame)

print("转化为二进制格式存储")
frame.to_pickle("examples/frame_pickle")

print("读取pickle文件")
result = pd.read_pickle("examples/frame_pickle")
print(result)
