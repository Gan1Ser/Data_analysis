import pandas as pd

xlsx = pd.ExcelFile("examples/ex1.xlsx")
print(xlsx)

result = pd.read_excel(xlsx)
print(result)

print("---------")
frame = pd.read_excel("examples/ex1.xlsx", "Sheet1")
print(frame)

print("---------")
writer = pd.ExcelWriter("examples/ex2.xlsx")
frame.to_excel(writer, "Sheet1")
writer._save()