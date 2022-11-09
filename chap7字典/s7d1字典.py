# 开发时间：26/8/2022 上午11:50
'''
字典：Python内置数据结构之一，与列表一样是一个可变序列
以键值对的方式储存数据，字典是一个无序的序列
1.scores={'张三':100,'lisi':98,'wangwu':45}
          键   值
2.dict(name='jack',age=20)  #调用内置函数
Python中字典是根据哈西key（hash）查找value所在位置
'''

#创建字典
scores={'zhangsan':100,'lisi':98,'wangwu':45}
print(scores)
print(type(scores))

#第二种方法：调用内置函数
student=dict(name='jack',age=20)
print(student)  #{'name': 'jack', 'age': 20}
                 #  键      值      键    值

#空字典
d={}
print(d)