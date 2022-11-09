# 开发时间：9/10/2022 上午11:07
import numpy as np

arr1 = np.arange(12).reshape((3,4))
# print(arr1)   #[[ 0  1  2  3]
#                 [ 4  5  6  7]
#                 [ 8  9 10 11]]

#查看相关属性
print(arr1.ndim)  #
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)

#调整维度
print(arr1.reshape((4,3)))
print(arr1.resize())

