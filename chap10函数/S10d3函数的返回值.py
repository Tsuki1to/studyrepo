# 开发时间：12/9/2022 下午6:51
def fun(num):
    odd=[]  #存奇数
    even=[]  #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even


# 函数的调用
lst=[10,29,34,23,44,53,55]

print(fun(lst))

'''
函数的返回值
（1）如果函数没有返回值，函数执行完毕后，不需要给调用处提供数据，return可以省略不写
（2）如果函数的返回值是1个，直接返回类型
（3）如果函数的返回值是多个，返回结果为元组

'''
#1
def fun1():
    print('hello')
    #return
fun1()

#2
def fun2():
    return'hello'

res=fun2()
print(res)

#3
def fun3():
    return'hello','world'

res2=fun3()
print(res2)  #('hello', 'world')返回两个值在一个元组中

