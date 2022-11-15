# 开发时间：10/11/2022 下午6:19
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('max_colwidth',300)
file_path = 'C:/Users/79395/Desktop/911.csv'
df = pd.read_csv(file_path)
# print(df.head(20))
# print(df.info())
# temp_list = df['title'].str.split(':').tolist()   #先将title中的信息使用':'进行拆分
'''1.通过把两个分类中的两个类型分开可以获得更加精细的分类'''
# cate_list = list(set(i[0] for i in temp_list))   #将拆分后的信息的第一位信息从组中遍历出来，去重，合并成列表
#i[0]就是分组中第一个大类（3种），i[1]是分组中的第二个（更精细的分类）

# table_zeros = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=(cate_list))
# # print(table_zeros.head())
# # for i in cate_list:
# #     table_zeros[i][df['title'].str.contains(i)] = 1
# # sum_set = table_zeros.sum(axis=0)
# # sum_set = sum_set.astype('i8')
# # re = sum_set.sort_values(ascending=False)
# print(re)
'''2.通过在表格的末尾添加额外一列并进行分组统计的方式进行计数'''
# cate_list = [i[0] for i in temp_list]
# df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
# print(df.groupby(by='cate').count()['title'])

'''3.通过分组进行统计不同事件类型的发生次数'''
# data1 = df.groupby(by= 'title').count()['e'].sort_values(ascending=False)
# print(data1)

'''
统计出不同月份的紧急电话的次数的变化
使用内置的时间函数进行时间序列的处理
pd.date_range函数中包含的变量start(开始时间)period(生成时间的个数)end(结束的时间)freq(每个时间的间隔)
pd.to_datetime函数方法可以将时间字符串类型转化成pandas的时间序列
如果字符串不规范，无法识别为时间序列时，手动添加时间格式化，foramt=''
panda时间顺序的重采样：指将一个频率转化为另一个频率处理，高频率转化为低频率称为降采样，低频率转化为高频率称为升采样
使用pd.resample('')实现频率转化
'''
# print(pd.date_range(start='20221114',periods=10,freq='10D'))
# df['timeStamp'] = pd.to_datetime(df['timeStamp'])   #将数据中字符串的时间转换成pandas的时间顺序参数
# df.set_index('timeStamp',inplace=True)   #setindex设置新的index索引，(inplace=True)表示为在原表的基础上进行修改
# count_by_mounth = df.resample('M').count()['title']  #时间顺序的重采样，降采样，按照月份（M），并且统计title列的数量
# # print(count_by_mounth)
#画图
# _x = count_by_mounth.index
# _y = count_by_mounth.values
# _x = [i.strftime('%Y-%m-%d') for i in _x]
#
# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x,rotation = 45)
# # plt.show()


'''进一步统计不同月份不同类型的电话类型'''
df['timeStamp'] = pd.to_datetime(df['timeStamp'])   #将数据中字符串的时间转换成pandas的时间顺序参数
#添加列，表示分类
temp_list = df['title'].str.split(':').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
df.set_index('timeStamp',inplace=True)
   #先将title中的信息使用':'进行拆分
plt.figure(figsize=(20, 8), dpi=80)
#分组
for group_name,group_data in df.groupby(by='cate'):
    #对不同的分析类都进行绘图
    count_by_month = group_data.resample('M').count()['title']
    _x = count_by_month.index
    _y = count_by_month.values
    _x = [i.strftime('%Y-%m-%d') for i in _x]
    plt.plot(range(len(_x)),_y,label = group_name)


plt.xticks(range(len(_x)),_x,rotation = 45)
plt.legend(loc = 'best')
plt.show()






# print(count_by_mounth)