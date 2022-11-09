# 开发时间：18/8/2022 下午4:14
#赋值运算符，运算顺序为从右到左 <---------
i=1+2
print(i)

a=b=c=39   #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('---------参数赋值--------')
a=20
a+=30  #相当于a=a+30
print(a)
a-=10  #相当于a=a-10
print(a)
a*=2   #相当于a=a*2
print(a)
print(type(a))
a/=3
print(a)
print(type(a))
a//=3
print(a)
print(type(a))
a%=3
print(a)

print('-----系列解包赋值-------')
a,b,c=20,30,40
print(a,b,c)
print("-------交换两个变量的值----------")
a,b=10,20
print('交换之前',a,b)
#交换
a,b=b,a
print('交换之后',a,b)



print('---------比较运算符-----------')
a,b=10,20
print('a>b吗',a>b)
print('a<b吗',a<b)
print('a<=b吗',a<=b)
print('a>=b吗',a>=b)
print('a==b吗',a==b)  #一个=为赋值，两个=为比较
print('a!=b吗',a!=b)   #!=为不等于
'''一个变量由三个部分组成：标识（id），类型（type），值（value）
==比较的值
比较对象使用 is
'''
a=10
b=10
print(a==b)  #True,说明a与b的Value相同
print(a is b)  #True，说明a与b的id相同
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))
print(a is not b)



