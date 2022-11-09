# 开发时间：26/8/2022 下午3:53
'''
集合与列表、字典一样都属于可变类型的序列
集合是没有value的字典，只有键，没有值
'''
s={2,3,4,5,5,7,7}
print(s)  #集合中的元素不允许有重复

#第二种方式
s1=set(range(6))  #范围生成集合
print(s1,type(s1))
s2=set([1,2,4,5,5,5,6])  #列表生成集合
print(s2)
s3=set((1,2,4,5,65))  #元组生成集合
print(s3)
s4=set('python') #字符串生成集合
print(s4,type(s4))
s5=set({124,3,4,4,5})
print(s5,type(s5))

#定义一个空集合
s6={}  #<class 'dict'>
print(type(s6))
s7=set()  #<class 'set'>
print(type(s7))
