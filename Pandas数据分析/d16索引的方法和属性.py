# 开发时间：19/10/2022 下午4:51
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)



file_path = './directory.csv'
df = pd.read_csv(file_path)
Country = df.groupby(by='Country')
Province_temp = df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
# print(Province_temp)
# print(Province_temp.set_index('Brand')) #把XXX作为索引
# print(Province_temp.set_index('Brand').index)
# print(Province_temp.set_index('Brand',drop = False)) #把列做为行索引，并且不删除列
