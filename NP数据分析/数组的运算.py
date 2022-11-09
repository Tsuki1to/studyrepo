# 开发时间：30/9/2022 下午3:20
import numpy as np

a = np.array([1,2,3])
b= np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#数组的尺寸相同时可以直接进行4则运算
a= np.array([[1,2],
             [3,4]])
b = np.array([[1,2],
              [3,4]])
print(a@b)   #[[ 7 10]
              #[15 22]]   a@b为矩阵乘法
              