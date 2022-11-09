# 开发时间：30/9/2022 下午2:08
import numpy as np
#查看数组的形状
a=[1,2,3]
b=[[1,2,3],
   [4,5,6]
   ]
c=[[[1,2,3],
    [4,5,6]],
   [[7,8,9],
    [10,11,12]]
   ]
arr1=np.array(a)  #(3,) 表示为一维数组，一行只有3个元素
arr2=np.array(b)   #(2, 3)   表示为二维数组，有两列，每行3个元素
arr3=np.array(c)   #(2, 2, 3)

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
#查看数组的维度

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#查看数组的元素数量
print(arr1.size)
print(arr2.size)
print(arr3.size)

#查看每个元素的大小
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)


#查看元素的类型
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)


#建立指定数据类型的数组
a= np.array([1,2,3,4,5],dtype=np.int8)
print(a.itemsize,a.dtype)
#不同的数据类型所占用的内存空间是不同的，占用内存空间越大的数据类型取值越广
a= np.array([1,2,3,4,5],dtype=np.float64)
print(a.itemsize,a.dtype)

#字符串数组类型的大小
lst = list('a,b,c,d')
# a = np.array(lst)  #4 <U1
# a = np.array(lst,dtype=np.string_)   #1 |S1
print(a.itemsize,a.dtype)

str1 = np.array(['numpty','pandas','matplotlis','python'],dtype=np.string_)
print(str1.itemsize,str1.dtype)   #10 |S10  #按照数组中字符串元素最多的元素进行存储的

#修改类型
arr1 = np.array([1.5,2,3],dtype=np.float64)
print(arr1,arr1.dtype,arr1.size)  #[1.5 2.  3. ] float64
#类型转换
arr2 = arr1.astype(np.int32)
print(arr2,arr2.dtype,arr2.size)   #[1 2 3] int32
'''
int32==》float64 空间足够没问题
float64==> int32  空间不足，小数部分会被截去
string_  ==> float64 如果字符串数组表示的全是数字，也可以使用astype转化为数值类型
'''
arr3 = np.array(['1','2','3'])
arr4 = arr3.astype(np.float32)
print(arr4)

print('=============================================================================')
#将numpy数组转换成列表类型
arr5 =np.array([[1,2,3],
               [4,5,6]])
list2 = arr5.tolist()
print(list2,type(list2))   #[[1, 2, 3], [4, 5, 6]] <class 'list'>

'''
ndarray.tostring(     #numpy数组转换成字符串
ndarray.tobytes(     #numpy数组转换成字节
'''

arr7 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
bytes2 = arr7.tobytes()
# bytes2 = arr7.tostring()  tostring() is deprecated. Use tobytes() instead.
print(bytes2)  #b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00'


print('==============数据类型的向下传递===============================')
a = [1,False,3,4,5,'str']   #int-->float-->str  数组中有一个浮点就会全部转换为浮点，有一个字符串就会由字符串转换为字符换unicod类型
arr= np.array(a)
print(arr.dtype)


print('================对象类型==================')
a = [1,False,3.5,4,5,'str']
arr = np.array(a,dtype=np.object_)
print(arr.dtype)   #object
print(arr*2)   #各自类型数值*2