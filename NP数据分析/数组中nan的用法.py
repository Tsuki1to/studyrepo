# 开发时间：11/10/2022 上午11:07
import  numpy as np
t2 = np.arange(21).reshape(3,7)
t2 = t2.astype(np.float32)
t2[2,2] = np.nan
print('\n')
print(t2)
#nan的特性：nan和nan不相等

np.nan = np.nan#False

t2[...,0] = 0
print('\n')
print(t2)
print('\n')
print(np.count_nonzero(t2))  #可以统计数组中不是零的数量
print(t2!=t2)  #数组中数字与本身都是相同，只有nan与nan不相同
print(np.count_nonzero(t2!=t2))  #就可以统计出数组中nan的个数
#另一个方法
print(np.isnan(t2)) #语句与t2!=t2相同
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
#nan在计算的时候与任何数计算结果都是nan
print(np.sum(t2))
print(np.sum(t2,axis=0))
print(np.sum(t2,axis=1))