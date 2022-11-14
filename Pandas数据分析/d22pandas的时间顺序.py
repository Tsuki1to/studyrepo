# 开发时间：10/11/2022 下午6:19
import numpy as np
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
file_path = 'C:/Users/79395/Desktop/911.csv'
df = pd.read_csv(file_path)
# print(df.head(3))
# print(df.info())
temp_list = df['title'].str.split(':').tolist()
cate_list = list(set(i[1] for i in temp_list))
# print(cate_list)
table_zeros = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=(cate_list))
# print(table_zeros.head())
pd.value_counts(i[0] for i in (cate_list))

'''通过分组进行统计不同事件类型的发生次数'''
# data1 = df.groupby(by= 'title').count()['e'].sort_values(ascending=False)
# print(data1)