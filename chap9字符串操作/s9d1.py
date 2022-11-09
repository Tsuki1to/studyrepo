# 开发时间：9/9/2022 下午12:06
print('apple'>'app')  #True
print('apple'>'banana')  #False


'''
比较规则：
两个字符串进行比较时，比较的是其ordinal value(原始值），调用内置函数ord()可以得到指定字符串的ordinal value
与内置函数ord（）对应的的chr（），调用内置函数chr（），就可以看到指定ordinal value的对应字符
'''
print(ord('a'),ord('b'))  #97，98
print('a'>'b')  #相当于97>98，所以False
print(chr(97),chr(98))
print(ord('赵'))  #互为相反值
print(chr(36213))   #互为相反值

'''
==与is的区别
==比较的是值（value）
is 比较的是id是否相等
'''
a=b='Python'
c='Python'
print(a==b)
print(b==c)

print(a is b)
print(b is c)
