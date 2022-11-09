# 开发时间：10/10/2022 下午4:50
import numpy as np

a = np.array([95,96,86,65,66])
b= np.array([73,72,71,69,68])
print('='*10,'标准差','='*10)
print(np.std(a))
print(np.std(b))
print('='*10,'方 差','='*10)
print(np.var(a))
print(np.var(b))
print('='*10,'加权平均值','='*10)
print(np.average(a))#当数组中没有权重的时候加权平均值就是普通平均值
print(np.mean(a))

a_avergae= np.average(a,axis=0,weights=[0.1,0.2,0.2,0.1,0.3]) #weights为加权平均值中的权重
print(a_avergae)

#变异系数：标准差/平均值
np.std()/np.mean()