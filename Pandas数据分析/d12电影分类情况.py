# 开发时间：18/10/2022 上午11:58
import pandas as pd
import string
import numpy as np
from matplotlib import pyplot as plt
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',150)
print('='*100)
file_path  = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)
# print(df.head())
# print(df['Genre'])
'''
先筛选所有的电影类型
建立一个全部是0的数组
列名为分类名
如果一条数据中的分类出现过，就将数组中的0变为1
'''
#第一步：提取所有电影的分类类型
#提取所有电影的类型，按照','分离开，并转换成列表
Movie_Genre = df['Genre'].str.split(',').tolist()
# print(Movie_Genre)
#双循环提取处单独的列表中单独分类名称
Movie_Genre_list = [i for j in Movie_Genre for i in j]
#将电影分类列表中进行去重操作
Genre_list = list(set(Movie_Genre_list))
#最终得到不重复的所有电影分类的类型
# print(Movie_Genre_list_set)

#建立一个全部为0的数组，行索引为电影的编号，列索引为所有电影的分类
#电影具有的分类，所在分类的列数据就会变为1
Zreos_list = pd.DataFrame(np.zeros((df.shape[0],len(Genre_list))),columns=Genre_list)
print(Zreos_list)

# print(Movie_Genre_res_temp)
for i in range(df.shape[0]):
    Zreos_list.loc[i,Movie_Genre[i]] = 1
    #Zeros_list.loc[0,'Sci——Fi,Actoin']
    #在全是0的数组中遍历，对应行数只有相应的分类列

Zreos_list = Zreos_list.astype('i8')
# print(Zreos_list.head())
#统计每种电影分类的数量
Zero_count = Zreos_list.sum(axis=0)

#排序
Genre_Total = Zero_count.sort_values()
# print(Genre_Total)
# print(type(Genre_Total))
# _x = Genre_Total.index
# _y = Genre_Total.values
# #画图
# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x)
# plt.show()