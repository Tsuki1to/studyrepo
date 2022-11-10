# 开发时间：2/11/2022 下午6:01
import pandas as pd
file_path = './books.xlsx'
'''方法1'''
# df = pd.read_excel(file_path,index_col='ID')
# df['Price'] = df['Listprice'] * df['Discount']
'''方法2'''
books = pd.read_excel(file_path,index_col= 'ID')
'''可以规定从xxx到xxx的行的计算'''
for i in books.index:
    books['Price'].at[i] = books['Listprice'].at[i] * books['Discount'].at[i]
# books['Listprice'] = books['Listprice'] +2
books['Listprice'] = books['Listprice'].apply(lambda x:x+2)  #同样实现了Listprice+2的目的
print(books)