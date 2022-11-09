# 开发时间：8/10/2022 下午8:52
import numpy as np

A = np.arange(2,14)
print(A)
A = np.arange(2,14).reshape((3,4))
print(A)

print(np.argmin(A))   #数组中数值最小的索引，索引为数值在数组所在的位置
                     #返回为0，所谓最小值所在位置为第一位
print(np.argmax(A))
print(np.mean(A))   #求数组的平均值
print(A.mean())      #求数组的平均值
print(np.median(A))  #求数组的中位数
print(np.cumsum(A))  #数组的累加结果
print(np.diff(A))   #数值与后一个值之间的差值组成的数组
print(np.nonzero(A))  #找出数组中非零的数字
print(np.sort(A))   #数组的排序
print(np.transpose(A))   #矩阵转置，表示为数据矩阵沿着斜线对称轴翻转
print(np.clip(A,5,9))   #截取数组中的数值，在5,9之间，小于5取5，大于9取9
print(A)
print(np.mean(A,axis=1))   #按照高纬度到低纬度右下里的原则，二维数组，1轴为按照行来取平均值
print(np.mean(A,axis=0))    #0轴为按照列取平均值
print(np.median(A,axis=0))   #中位数