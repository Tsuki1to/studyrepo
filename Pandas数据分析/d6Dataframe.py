# 开发时间：12/10/2022 下午8:32
#pd.Series是一维的
#pd.Dataframe是二维的，是Series的容器
import numpy as np
import pandas as pd
import string
a = pd.DataFrame(np.arange(15).reshape((3,5)))
print(a)
'''
    0   1   2   3   4
0   0   1   2   3   4
1   5   6   7   8   9
2  10  11  12  13  14
行索引，横向，表明不同行，index，0轴,axis=0
列索引，纵向，表明不同列，columns,1轴，axis=1
'''
b = pd.DataFrame(np.arange(15).reshape(3,5),index=list(string.ascii_uppercase[:3]),columns=list(string.ascii_uppercase[-5:]))
print(b)
#除了直接创建Dataframe，也可以通过字典生成Dataframe数组
#字典1：一键多值
d1 = {'name':['xiaoming','xiaogang'],'age':['18','20'],'gender':['male','female']}
D1 = pd.DataFrame(d1)
print(D1)

#字典2：列表中多个字典
d2 = [{'name':'xiaoming','age':12,'gender':'male'},{'name':'xiaogang','gender':'female'},{'name':'xiaomei','age':18}]
t2 = pd.DataFrame(d2)
print(t2)  #未传入值的内容为NaN

#Dataframe读取数据
# df = pd.read_excel('./douban.xlsx')
# t3 = pd.DataFrame(df)
#
# print(t3)
df = pd.read_csv('./douban.csv')
data_list = []
for i in df:
    print(i)
#     temp = {}
#     temp['片名'] = i['片名']
#     temp['评分'] = i['评分']
#     temp['导演'] = i['导演']
#     temp['主演'] = i['主演']
#     data_list.append(temp)
# t1 = pd.DataFrame(data_list)
# print(t1)

