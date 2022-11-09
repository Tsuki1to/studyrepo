# 开发时间：1/11/2022 上午10:24
#统计不同年份下的书的数量
#统计不同年份下书的平均评分情况

import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
file_path = './books.csv'
df = pd.read_csv(file_path)
# print(df.head())
'''
数据中年份数据有缺失，使用布尔判断保留数据中不为零的值
'''
data1 = df[pd.notnull(df['original_publication_year'])]
# data3 = data1.groupby(by='original_publication_year').count()['id']
# print(data3)
grounped1 = data1['average_rating'].groupby(by = data1['original_publication_year']).mean()
grounped2 = data1['average_rating'].groupby(by = data1['original_publication_year']).count().sort_values(ascending=False)
print(grounped1)  #数据中的平均分按照年份排序取平均值
# print(grounped2)   #数据中书按照年份排序查看本数