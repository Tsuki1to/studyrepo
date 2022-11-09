# 开发时间：19/10/2022 上午11:33
import pandas as pd
import numpy as np
import string

t = np.zeros(10).reshape(2,5)
t1 = pd.DataFrame(t,index=list(string.ascii_uppercase[:2]),columns=list(string.ascii_lowercase[-5:]))
print(t1)
#两个数组形状不同，内容不同
a = np.ones(12).reshape(3,4)
a1 = pd.DataFrame(a,index=list(string.ascii_uppercase[:3]),columns=list('1234'))
print(a1)
'''
使用merge语句进行数据的列合并
'''
df1 = pd.DataFrame(np.ones(10).reshape(2,5),index=list('AB'),columns=list('abcde'))
df2 = pd.DataFrame(np.arange(9).reshape(3,3),columns=list('tal'))
print('merge合并就是取两个数组数据中的并集'
      '及两个数组终中共同有的数据')
print(df1)
print('='*100)
print(df2)
print('='*100)
print(df1.merge(df2,on='a'))
df1.loc['A','a'] = 100
print(df1)# df1的a列第一个值变成了100，a列就只有一个1，所以合并后只有一行
print(df1.merge(df2,on='a'))
'''merge在默认情况下，how = inner（内连接）'''
print(df1.merge(df2,on='a',how='outer'))
'''在how = outer时为外连接，取的是两个数组的交集，没有值的地方使用NaN补全'''
print(df1.merge(df2,on='a',how='left'))
'''how = left,左连接，以左边的数组为准'''
print(df1.merge(df2,on='a',how='right'))
'''how = right,右连接，以右边的数组为准'''