# 开发时间：12/9/2022 下午10:43
def fun(*args):   #（个数可变的位置参数）可变位置参数 ,不定长参数传递
    print(args)

fun(10)
fun(20,30)
fun(10,299,40)

#2
def func(**kwargs):   #(个数可变的关键词参数)关键字传参，通常以字典的形式保存（键值对）
    print(kwargs)

func(a=19)
func(a=19,b=9)

#  def print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)    print的定义
help(print)

''' 
定义函数过程中，*args和**kwargs都只能定义一个
混用时，个数可变的位置参数要在前面
def func(*args, **kwargs)
    pass
'''

#关于数据解包
s=[1,2,3]
d={
    'a':'zhangsan',
        'b':'20',
        'c':'100'
}
def jie(a,b,c):
    print(a)
    print(b)
    print(c)

jie(*s)   #*输入对象前加入星号即可对字符串进行拆解（就是位置传参
jie(**d)  #如果解包的字典，在输入对象前加**


