# 开发时间：9/9/2022 下午2:58
'''
字符串为不可变类型
不具备增删改操作
切片操作将产生新的对象
'''

s='hello,Pyhton'
s1=s[:5]  #没有指定开始位置，默认起始位置为0
s2=s[6:]  #没有指定结束位置，默认结束位置为末尾
s3='!'
newstr=s1+s3+s2

print(s1)
print(s2)
print(s3)
print(newstr)
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('---------------------')
print(s[1:5:1])  #从1到5（不包含5），步长为1
print(s[::2])
print(s[::-1])
print(s[-6::1])  #倒数第6个开始正向截取切片