# 开发时间：19/10/2022 下午2:20

import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)



file_path = './directory.csv'
df = pd.read_csv(file_path)
# print(df.head())

'''
如果想知道美国个中国哪个国家的门店较多，或者中国每个省份的门店的数量
就要将数据进行分组处理
1，将数据按照国家进行分类
2，将数据按照省份进行分类
pd.groupby(by='cloumns_name')对数据进行分组操作
pandas的count语句进行统计操作
'''
Country = df.groupby(by='Country')

#DataFrameGroupBy

# 对#DataFrameGroupBy类型的数据可以进行一下操作
# 1，遍历
# for i in Country:
#     print(i)
#     print('*'*100) #按照国家分组对数据内进行遍历
# t = df[df['Country']=='US']
# print(t)

# 2，调用聚合方法
# print(Country.count().sort_values(by='Brand',ascending=False))
# Country_count = Country['Brand'].count() #按照国家分组后的数据再按照品牌数量进行排序
# print(Country_count['US'])    #输出品牌排序后美国的数量
# print(Country_count['CN'])   #输出中国的门店数量

# print('='*50,'求中国各个省份的门店数量','='*50)
# China_City = df[df['Country']=='CN']
# China_City_Brand = China_City.groupby(by='City')
# China_count = China_City_Brand['Brand'].count()
# print(China_count.sort_values(ascending=False))
# print(China_count['郑州市'])

'''数据按照多个条件进行分组'''

Province_temp = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()   #对某几列进行分组
print(Province_temp.head())

t1 = df.groupby(by=['Country','State/Province'])['Country'].count()  #获取分组后某一部分的数据
print(t1.head())
#效果是一样的

# print(Province_temp['CN'].sort_values())
# 因为有两个分组条件，所以Province_temp是一个具有两列索引的Series



