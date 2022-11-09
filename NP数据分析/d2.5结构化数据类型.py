# 开发时间：8/10/2022 下午4:04
import numpy as np

student = np.dtype([('name','S20'),('age','i4'),('marks','f4')])  #创建数据类型student
arr = np.array([('yitong',18,99.99),('kaige',20,51.22),],dtype=student)
print(arr)
print(arr.dtype)
print(arr.ndim)

teacher = np.dtype([('name','U4'),('age','i4'),('salary','f4')])
b = np.array([('will',32,5000.12),
              ('tony',50,8000.51)],
             dtype=teacher)
print(b)
print(b['name'])
print(b['age'])
print(b['salary'])
'''当数组中有许多数据类型，想要分别读取每种不同的数据类型时
就要自己定义数据类型对数组中的数组进行读取
'''