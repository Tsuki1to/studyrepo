# 开发时间：12/10/2022 下午3:28
import pandas as pd
import string

temp_list = {'name':'xiaohong','age':'male','tel':666}
t3 = pd.Series(temp_list)
print(t3)
print('\n')
'''索引的操作'''
print(t3.index)   #获取Series索引的遍历
print('\n')
for i  in t3.index:  #遍历
    print(i)
print('\n')
print(type(t3.index))  #获取类型
print('\n')
print(len(t3.index))   #获取长度
print('\n')
a = list(t3.index)  #创建索引的列表
print(a)
print(list(a[:2]))   #获取列表前两个值

'''值的操作'''
print('\n')
print(t3.values)  #获取Series数组的值
print('\n')
print(type(t3.values))   #<class 'numpy.ndarray'>
'''
Series由两个数组组成
一个数组构成对象的键（index（索引））
一个数组构成对象的值（values）
'''
'''ndarray中许多方法都可以在Series中应用'''
'''Series中具有where方法，但是与ndarray不同'''
a10 = {string.ascii_uppercase[i]:i for i in range(10)}
t1 = pd.Series(a10)
print(t1)
print(t1.where(t1>1))  #取数组中大于1的值，剩下的取NaN
print(t1.where(t1>1,10))  #数组中大于1的值不变，小于1的变为10