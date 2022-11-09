# 开发时间：21/10/2022 下午4:49
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)



file_path = './directory.csv'
df = pd.read_csv(file_path)

#使用matplotlib进行绘制门店排名数量前十的国家
data1 = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]
#groupby(by='Country')  #数据根据国家进行分组
#.count() 统计每个数据内容的数量
#['Brand'] 规定统计及排序在Brand列上的数据进行
#sort_values(ascending=False)  #正序进行排列
#[:10]  #取前十个值

#画图
_x = data1.index
_y = data1.values

plt.Figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)
plt.show()