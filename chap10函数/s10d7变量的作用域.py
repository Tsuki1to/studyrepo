# 开发时间：13/9/2022 下午1:58
#1
def fun(a,b):
    c=a+b   #c,就称为局部变量，因为c在函数体内进行定义的变量，a，b为函数的形参，作用范围也是函数的内部，相当于局部变量

    print(c)
# print(a)  a,c超出了起作用的范围（超出了作用域
# print(c)

#2
name='杨老师'   #name的作用范围为函数的内部和外部都可以使用======》称为全局函数
print(name)
#定义函数
def fun2():
    print(name)
#调用函数
fun2()

#3
def fun3():
    global age   #函数内部定义的变量为局部变量，当局部变量使用global声明时，这个变量就变成了全局变量。
    age=20
    print(age)

fun3()
print(age)



