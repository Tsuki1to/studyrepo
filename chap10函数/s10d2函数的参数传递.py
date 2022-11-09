# 开发时间：12/9/2022 下午4:01
def calc(a,b):  #a，b称为形式参数，简称形参，形参的位置是在函数的定义处
    c=a+b
    return c

result=calc(10,20)  #10，20称为实际参数，简称实参，实参的位置是函数的调用处
print(result)

'''
参数传递为分为：
1，位置传递参数
2.名称传递参数
形参的名称可以与实参不同
'''

def fun(arg1,arg2):   #def为define：表示定义函数

    print('arg1=',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)
    #return

n1=11
n2=[11,22,33]
print('n1=',n1)
print('n2=',n2)
print('--------------------')
fun(n1,n2)
print(n1)
print(n2)

'''
在函数的调用过程中，进行参数传递
如果是不可变的对象，在函数体的修改不会影响到实参的值，arg1的修改为100，不会影响到n1的值
如果对象是可变的，在函数体中的修改会影响到实参的值，arg2的修改，append(10),会影响到n2的值
变化与否取决于对象是否可变

'''