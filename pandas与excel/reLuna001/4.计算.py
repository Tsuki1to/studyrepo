# 开发时间：2/11/2022 下午6:01
import pandas as pd
file_path = './books.xlsx'
df = pd.read_excel(file_path,index_col='ID')
df['Price'] = df['Listprice'] * df['Discount']
print(df)