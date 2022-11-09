# 开发时间：8/10/2022 下午8:26
import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(a)
print(b)
# c = a - b  #数组内各个数字相减
# c = a + b  #等于数组内各个数字相加
# c = a * b    #等于数组内各个数字相乘
# c = b **2  #等于数组内各个数字的平方
print(b)
# print(b<3)   #判断数组内的数字大小，输出值为布尔值

#numpy中的两种乘法
#1.普通相应数值之间的之间的乘法
a= np.array([[1,2],
             [3,4]])
b = np.array([[1,2],
              [3,4]])

c =a * b
print(c)
#2.矩阵乘法

c_dot=np.dot(a,b)
print(c_dot)
#或者
c_dot=a.dot(b)
print(c_dot)
#或者
c_dot=a@b
print(c_dot)

a = np.random.random([2,4])
print(a)
print(np.sum(a,axis=1))   #axis=1代表在同一行中求和
print(np.max(a,axis=0))   #axis=0表示为在同一列中求最大值
print(np.min(a,axis=1))
