# 开发时间：17/10/2022 下午5:12
import pandas as pd
import numpy as np
import re
#设置行不限制数量
pd.set_option('display.max_rows',None)
#最后的的参数可以限制输出行的数量

#设置列不限制数量
pd.set_option('display.max_columns',None)
#最后的的参数可以限制输出列的数量

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',200)


file_path = './IMDB-Movie-Data.csv'
data = pd.read_csv(file_path)
# print(data)
# print(data.info())  #获取数据的基本信息
# print(data.head(1))  #获取数据中第一行的信息
#1000个所有电影的平均分
Rating_mean = data['Rating'].mean()
print(Rating_mean)
#导演信息提取到一个新的列表中
Dir_list = data['Director'].to_list()
'''
python内置，无序列表。无索引、无切片、作为一个无序的集合，set不记录元素位置或者插入点。
set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
'''
#将列表设置为不可重复的set（）类型
Dir_list = set(Dir_list) #就可以将数据中重复的导演信息进行合并
# print(len(Dir_list))  #输出得到合并后的导演数量信息
# print(len(data['Director'].unique()))  #去除列表中重复的语句
#所有电影的票房最大值和最小值
Max_Revenue = data['Revenue (Millions)'].max()
Max_Revenue_Movie = data['Revenue (Millions)'].argmax()
#data.argmax()可以得到数据中最大值的行索引
print('一千个电影中票房最高的是：',data.loc[Max_Revenue_Movie,'Title'])
print('票房为',Max_Revenue)
Min_Revenue = data['Revenue (Millions)'].min()
print(Min_Revenue)

#获取演员的数量
Actor_num_list = data['Actors'].str.split(',').to_list()
Actor_num = [i for j in Actor_num_list for i in j]
print(len(set(Actor_num)))
