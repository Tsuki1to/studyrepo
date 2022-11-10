# 开发时间：2/11/2022 下午6:01
import pandas as pd
file_path = './books.xlsx'
'''方法1'''
# df = pd.read_excel(file_path,index_col='ID')
# df['Price'] = df['Listprice'] * df['Discount']
'''方法2'''
books = pd.read_excel(file_path,index_col= 'ID')
for i in books.index:
    books['Price'].at[i] = books['Listprice'].at[i] * books['Discount'].at[i]
print(df)