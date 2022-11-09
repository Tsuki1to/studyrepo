# 开发时间：10/10/2022 下午5:53
import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
for i in np.nditer(a):
    print(i,end=',')
print('\n')
print('\n')
print('\n')
print('='*15,'遍历数组的转置','='*15)
print(a.T)
print('\n')
for i in np.nditer(a.T):
    print(i,end=',')  #虽然转置了但是遍历的读取方式是数据在内存中存储的方式，
                      #转置不改变内存的存储方式，所以两次遍历结果相同
print('\n')

b = a.T.copy(order='C')   #将数组转置后的结果进行存储就会改变数组在内存中的存储模式，
                           #并开启新的存储空间，遍历结果也就不相同

print(b)
for i  in np.nditer(b):
    print(i,end=',')