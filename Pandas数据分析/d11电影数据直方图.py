# 开发时间：18/10/2022 上午10:07
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('max_colwidth',200)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

file_path  = './IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)
# print(df.head())
# print(df.info())
'''
需求：
分析这么多电影的Runtime数据分布
'''
runtime_data = df['Runtime (Minutes)'].values
print(type(runtime_data))   #<class 'numpy.ndarray'>
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
mean_runtime = runtime_data.mean()
# print(max_runtime)
# print(min_runtime)
# print(mean_runtime)
#做直方图之前先计算组数
#组数 = （最大值 - 最小值）//组距
num_bin = (max_runtime - min_runtime)//5

#设置图形的大小
plt.figure(figsize=(20,8),dpi = 80)
plt.hist(runtime_data,num_bin)
plt.xticks(range(min_runtime,max_runtime+5,5))
plt.show()




