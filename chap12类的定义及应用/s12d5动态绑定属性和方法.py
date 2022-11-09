# 开发时间：16/9/2022 上午11:27
class Student:    #定义类对象（一个类对象中可以创建许多个实例对象，并且实例对象的值可以不同
    def __init__(self,name,age):    #括号中为局部变量

        self.name=name      #将局部变量赋值给实例变量
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('zhangsan',20)   #一个类对象中可以创建许多个实例对象，并且实例对象的值可以不同
stu2=Student('lisi',30)
#动态绑定：只给其中一个实例对象添加属性和方法（只给stu1添加性别属性
print('------为stu2添加性别属性----------')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)


print('------------------------------------')
stu1.eat()
stu2.eat()
print('-----------动态绑定方法------------')
def show():
    print('定义在类之外的，称为函数')
stu1.show=show  #动态绑定之前叫函数，绑定之后叫方法

stu1.show()

# stu2.show()   因为stu2没有动态绑定show方法，所以不能调用