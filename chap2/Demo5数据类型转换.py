#coding:UTF-8 #中文编码声明
# 开发时间：16/8/2022 下午3:15
name='张三'
age='20'

print(type(name),type(age)) #说明name和age的数据类型不相同
print('我叫'+name+'今年,'+age+'岁')
print('我叫'+name+'今年,'+str(age)+'岁') #当将str类型与int类型进行连接时，报错，解决方法为将数据的类型转换

#不同类型之间转换
print('------------str()可以将其他类型转换成str类型的数据-------')
a=10
b=198.2
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(c)),type(str(b)),type(str(a)))

print('-----------int()可以把其他类型的数据转换成int类型--------')
s1='128'
f1=98.6
s2='88.9'
ff=False
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #将str转换成int类型，字符串为数字串
print(int(f1),type(int(f1)))  #将float转换成int类型，但是只截取整数部分，舍掉小数
# print(int(s2),type(int(s2))) #将str转换成int类型会报错，因为字符串中有小数为小数串
print(int(ff),type(int(ff)))
# print(int(s3),type(int(s3)))  #将str转成int类型时，字符串必须为数字串

print('---------float()可以将其他形式数据转换为float类型--------')
s1='128'
s2='88'
ff=False
s3='hello'
i=99
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(ff))
   #文字类字符串无法转换成float，整数,布尔转换成float类型末尾+.0