# 开发时间：18/9/2022 下午4:31
#语法格式
'''
class 子类类名（父类1，父类2。。。。。）：
     pass
*如果一个类没有继承任何类，则默认继承object
*python支持多继承
*定义子类时，必须在其构造中调用父类的构造函数
'''

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,stu_no):
        super(). __init__(name,age)
        self.sut_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,Tor):
        super(). __init__(name,age)
        self.Tor=Tor

stu=Student('张三',20,'1000')
tea=Teacher('李四',20,10)
stu.info()
tea.info()

'''多继承'''

class A():
    pass
class B():
    pass
class C(A,B):  #C同时继承了A和B
    pass