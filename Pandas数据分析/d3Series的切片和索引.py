# 开发时间：12/10/2022 下午3:00
import pandas as pd
import string

temp_list = {'name':'xiaohong','age':'male','tel':666}
t3 = pd.Series(temp_list)
print(t3)

print('数组中的索引名称索引数组的值')
print(t3['name'])
print(t3['age'])
print(t3['tel'])

print('根据函数进行索引')
print(t3[0])
print(t3[1])
print(t3[2])

print('步移索引')
print(t3[1:])

print('布尔索引')
a = {string.ascii_uppercase[i]:i for i in range(10)}
a1 = pd.Series(a)
print(a1[a1>3])

# print('如果索引名称和与数组中不相符将返回NaN')  报错
# print(a1[['A','B']])