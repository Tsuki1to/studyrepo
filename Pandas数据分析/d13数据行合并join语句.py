# 开发时间：18/10/2022 下午6:42
#join语句是把行索引相同的数据合并到一起
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

#将两个数组进行合并
print(a1.join(t1))
print(t1.join(a1))
