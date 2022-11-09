# 开发时间：9/8/2022 下午3:29
# '''
# 数据类型
# 数字：
# 1.整数：int（integer)[正整数、负整数、零]
# 2.小数：float
# '''
# n1=90
# n2=-76
# n3=0
# print(n1,type(n1))
# print(n2,type(n2))
# print(n3,type(n3))

#整数可以表示为二进制，十进制，八进制，十六进制
# print('十进制',118)  #默认为十进制
# print('二进制',0b1001001)  #二进制为0b开头
# print('八进制',0o1273)  #八进制为0o开头
# print('十六进制',0x2EDA)  #十六进制以0x为开头
#
# #浮点运算
# n1=1.1
# n2=2.2
# print(n1+n2)
# from decimal import Decimal
# print(Decimal('1.1')+Decimal('2.2')) #导入Decimal小数模块进行计算
#
# a=10
# b=20
# print(a+b) # 加法运算
#
# c=1.5
# print(c*5) #乘法运算
#
'''
文字：展示
字符串：str
表示方式为单引号’‘或者双引号“”
可以进行加乘，但是必须都是字符串。
+：合并两个字符串
*：一个字符串只能乘以一个数字，表示为重复多少次
'''
# 字符串
s='周润发'
print(s)
print('你好我叫zhourunfa')

# 三个引号可以进行多行赋值
a='''你好啊
欢迎来到我家
你们可以来救火吗
我家着火了'''
print(a)

# 仅支持字符串和字符串和字符串同类型之间进行计算
name='yitong'
type='handsome'
print(name+type)
print(name*5)

#