# 开发时间：11/10/2022 下午5:44
import numpy as np
t1 = np.arange(14).reshape(2,7)
t2 = np.arange(14,28).reshape(2,7)
print(t1)
print(t2)
print('\n')
print('='*15,'两种拼接方法','='*15)
#竖直拼接
print('竖直拼接')
t3 = np.vstack((t1,t2))
print(t3)
#水平拼接
print('水平拼接')
t4 = np.hstack((t1,t2))
print(t4)

'''交换'''
print(t1)
print('====行交换====')
t1[[0,1],:] = t1[[1,0],:]
print(t1)

print(t2)
print('====列交换=====')
t2[:,[0,1]] = t2[:,[1,0]]
print(t2)