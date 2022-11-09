# 开发时间：10/10/2022 上午10:26
import numpy as np

x = np.arange(8).reshape(4,2)
print(x)
'''
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
'''
print('=================')
y = x[[0,1,2],[0,1,0]]   #大括号前面的内容代表数组中行坐标的索引，后面大括号代表列坐标的索引
#所以上述坐标代表，第一行第一列数据，第二行第二列数据，第三行第一列数据
print(y)  #[0 3 4]
'''获取4*3数组中四个角值'''
a = np.arange(12).reshape(4,3)
print(a)
b = a[[0,0,3,3],[0,2,0,2]]
b1 =  b.reshape((2,2))
print(b1)

'''
创建一个8*8的黑白棋盘
'''
z = np.zeros((8,8),dtype=int)
z[0::2,0::2] = 1
z[1::2,1::2] = 1

print(z)

'''按照布尔值索引'''
w = np.arange(18).reshape((3,6))
w1 = w[w>6]
print(w1)   #通过布尔值索引出的数组为一维数组
'''提取数组中的奇数,并将奇数修改为-1'''
e = np.arange(15).reshape(3,5)
e[e%2!=0] = -1

print(e)
'''布尔索引去除不要的数据'''
arr = np.array([np.nan,1,2,3,np.nan])
print(arr)
print('\n')
print('======去除数组中非数字')
arr2 = arr[~np.isnan(arr)]
arr2 = arr2.astype(np.int32)
print(arr2)
'''多条件索引'''
#&和
#|或
x = np.arange(15).reshape(3,5)
print(x[(x>4)&(x<9)])  #索引x大于4并小于9的数值
print(x[(x<4)|(x>9)])   #索引x小于4并大于9的数值

'''选择第一行和最后一行的1,3,4列'''
x = np.arange(15).reshape(3,5)
print(x)
# x1 = x[[0,-1],[0,2,3]]  行和列数不相同会报错
#所以分别提取行和列
c = x[[0,-1],...]
l = x[...,[0,2,3]]
x2 = x(c,l)
x1 = x[[0,-1],...][...,[0,2,3]]

print(x1)

