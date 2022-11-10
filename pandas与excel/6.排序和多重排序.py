# 开发时间：10/11/2022 下午12:36
import pandas as pd
file_path = './List.xlsx'
df = pd.read_excel(file_path,index_col='ID')
df.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])
print(df)
# Worthy_no = df[df['Worthy']=='no'].sort_values(by='Price')
# Worthy_Yes = df[df['Worthy']=='yes'].sort_values(by = 'Price')
# print(Worthy_no)
# print(Worthy_Yes)


