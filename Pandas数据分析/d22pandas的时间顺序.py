# 开发时间：10/11/2022 下午6:19
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
file_path = 'C:/Users/79395/Desktop/911.csv'
df = pd.read_csv(file_path)
print(df.head(3))
print(df.info())
