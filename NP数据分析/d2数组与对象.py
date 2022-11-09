# 开发时间：30/9/2022 下午2:00
import numpy as np
#一维数组
a=[1,2,3,4]  #向量
array1=np.array(a)
print('array1',array1)
#二维数组
b=[[1,2,3],   #矩阵
   [2,3,4]
   ]
array2=np.array(b)
print('array2',array2)

#三维数组
c=[[[1,2,3]
    ,[2,3,4]],
   [[3,4,5],
    [4,5,6]]
   ]
array3=np.array(c)
print('array3',array3)