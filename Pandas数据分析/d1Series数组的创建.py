# 开发时间：12/10/2022 上午10:44
import pandas as pd

s1 = pd.Series([1,21,56,84,25])
print(type(s1))
print(s1)
'''
0     1
1    21
2    56
3    84
4    25
dtype: int64
'''
#添加list(索引名称
t2 = pd.Series([1,2,5,4,58],index=list('abcde'))  #list为索引名称
print(t2)

'''通过字典添加Series'''
temp_list = {'name':'xiaohong','age':'male','tel':666}
t3 = pd.Series(temp_list)
print(t3)    #字典中的键就变成了索引名称，值就变成了数组中的值
'''
name    xiaohong
age         male
tel          666
dtype: object
'''