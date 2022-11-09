# 开发时间：18/9/2022 下午6:09
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,stu_no):
        super(). __init__(name,age)    #调用父类方法super().
        self.stu_no=stu_no
    def info(self):      #方法重写
        super().info()
        print('学号为：',self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,Tor):
        super(). __init__(name,age)
        self.Tor=Tor
    def info(self):    #方法重写
        super().info()   #调用父类
        print('教龄为：',self.Tor)    #定义方法

stu=Student('张三',20,'1000')
tea=Teacher('李四',20,10)
stu.info()
tea.info()