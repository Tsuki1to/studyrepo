# 开发时间：12/10/2022 下午2:52
import numpy as np
import string
import pandas as pd
a = {string.ascii_uppercase[i]:i for i in range(10)}
a1 = pd.Series(a)
print(a)
print(a1)  #dtype: int64
#创建一个pandas数组取值为a数组，索引名称取5:15
a2 = pd.Series(a,index=list(string.ascii_uppercase[5:15]))
#因为a的值是从1到9所以9以后没有值，就是NaN
print(a2)  #dtype: float64

