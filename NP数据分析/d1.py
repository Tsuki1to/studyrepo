# 开发时间：30/9/2022 上午
import timeit

import numpy as np

# array = np.array([[123],
#                   [243]])
# print(array)
# print('number of dim:',array.ndim)
# print('shape:',array.shape)
# print('size:',array.size)

arr = np.arange(1,6)   #定义数组
print(arr)

#数组的运算
#让数组中每个元素+1

lst = [1,2,3,4,5]

#方法1用python的方法
# for i in range(len(lst)):   #len(lst)可以将列表中的元素遍历为整数
#     lst[i] +=1
#方法2
# lst=[i+1 for i in lst]
# print(lst)


#使用numpy的方法
arr = np.arange(1,6)   #定义数组
arr+=1
print(arr)

#numpy底层使用的是c语言进行编写，所以效率更高
#计算10000以内数字的和
#使用python的方法
# a=0
# b=1
# while b < 10000:
#     a+=b
#     b+=1
# else:
#     print(a)
#方法2
# a=list(range(10000))
# def test():
#     return sum(a)
# print(timeit.timeit(stmt=test,number=10000))
#
# #使用numpy的方法
# def test1():
#     a = list(range(10000))
#     b = np.array(a)
#     return np.sum(b)
# print(timeit.timeit(stmt=test1,number=10000))

