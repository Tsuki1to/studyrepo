# 开发时间：26/8/2022 下午2:53
#第一种
t=('python','world',98)
print(t)
print(type(t))


t2='python','world',98  #省略小括号
print(t2)
print(type(t2))

'''当元组中只有一个数据时后面使用，'''
t3=('python',)
print(t3)
print(type(t3))



#第二种
d=tuple(('python','world',98))
print(d)
print(type(d))

'''空元组的创建方式'''
lst=[]
lst1=list()

d={}
d2=dict()

t4=()
t5=tuple()
print('空列表',lst,lst1,'空字典',d,d2,'空元组',t4,t5)