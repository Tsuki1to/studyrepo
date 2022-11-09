# 开发时间：14/9/2022 下午5:53
#常见BUG类型
#1
age=input('请输入你的年龄')
# if age>=18:   数据类型没有转换，str数据无法与18进行比较
if int(age)>=18:
    print('成年人')

#2

# while i <10:
#     print(i)

i=0
while i<10:
    print(i)
    i+=1    #i没有赋值，循环体中i没有变化将死循环


#3  索引越界index Error
lst=[11,22,33,44]
# print(lst[4])
print(lst[3])  #输出列表中第四个元素

#4  append方法使用不熟练
lst=[]
# lst=append['a','b','c']
lst.append('a') #append添加方式，并且一次只能添加一个元素
lst2=['b','c']
lst.extend(lst2)  #extend可以一次添加多个元素

print(lst)


