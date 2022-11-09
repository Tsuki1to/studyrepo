# 开发时间：30/9/2022 下午3:11
import numpy as np
a = np.zeros((3,2),
             #dtype=np.int32
             )
print(a)    #生成一3行，每行有2列的全是0的数组   #全等数列
print('=================全等数列========================')
print(np.ones((2,4)))  #生成一个2行，每行有4列全是1的数组   #全等数列
print('==============使用指定值进行填充=======================')
arr1 = np.full([3,2],fill_value=666,dtype='i4')   #np.full使用fill_value指定的值进行填充    #全等数列
print(arr1)

print('===========eye()函数=========对角线为1其余为0的数列=====其中参数N为行数，M为列数，默认（m=n）==========')
arr2 = np.eye(5,dtype='i4')
print(arr2)

print('=========================================')
print(np.arange(3,7))  #生成一个递增的数组
print(np.arange(1,11,1))
print('=========================================')
print('=================frombuffer()函数=========================')
s = b'itong is a good man'
print(np.frombuffer(s,dtype='S1',count=5,offset=2))   #count为读取数量，offset为从第几位开始读取
print('=============fromiter()函数，从可迭代对象返回一个数组========')
x = [1,2,3,4,5]
z= iter(x)
print(z)
print(type(z))
arr3 = np.fromiter(z,dtype='i4')
print(arr3)
print('=========================================================')
print(np.linspace(0,1,5))   #返回0至1之间的区间的5等分，生成5个元素的数组(等差数列
print(np.logspace(0,2,5))  #创建一个等比数列（默认log以10为底数
print('=========================================')
print(np.random.rand(5))    #生成一个长度为5，范围为0到1的一维数组
print(np.random.rand(2,4))   #生成一个2行，4列的随机数组
print(np.random.rand(3,2,2))  #生成一个三维数组
print(np.random.random(1))    #生成一个0到1之间的随机数（）中为size



