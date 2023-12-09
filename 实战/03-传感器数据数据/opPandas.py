import pandas as pd
from datetime import datetime

file_path = '221040100208李奥奇.csv'
data = pd.read_csv(file_path)

data['DataTime'] = pd.to_datetime(data['DataTime'], format='%Y%m%d%H%M%S')

current_date = datetime.now()
data = data[(data['DataTime'].dt.year == 2023) & (data['DataTime'] < current_date)]

data['w01001-Rtd'] = data['w01001-Rtd'].replace(0, data['w01001-Rtd'].mean())
data['w01012-Rtd'] = data['w01012-Rtd'].replace(0, data['w01012-Rtd'].mean())

max_w01001 = data['w01001-Rtd'].max()

q2_data = data[(data['DataTime'].dt.month >= 4) & (data['DataTime'].dt.month <= 6)]
median_w01001_q2 = q2_data['w01001-Rtd'].median()
median_w01012_q2 = q2_data['w01012-Rtd'].median()
max_median_q2 = max(median_w01001_q2, median_w01012_q2)

print(f"查询所有 w01001 传感器的最大值: {max_w01001}")
print(f"查询第2季度的 max(所有w01001传感器中位数，所有w01012传感器中位数): {max_median_q2}")

output_file_path = 'updated_221040100208李奥奇.csv'
data.to_csv(output_file_path, index=False)






