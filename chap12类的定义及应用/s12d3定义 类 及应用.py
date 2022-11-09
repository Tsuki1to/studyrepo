# 开发时间：14/9/2022 下午11:21
class Student:   #student为类的名称（类名）由一个或者多个单词组成，每个但系的首字母大写，其余小写
   native_place='吉林'   #直接写在类里的变量，称为类属性
   def __init__(self,name,age):
       self.name=name   #self.name 称为实体属性，进行了一个赋值的操作，将局部变量的name赋值给了实体属性
       self.age=age


   def eat(self):   #实例方法    def在类之外定义的叫函数，在类之内定义的叫实例方法
       print('学生在吃饭')
   @staticmethod
   def method():
       print('静态方法')
   @classmethod
   def cn(cls):
       print('类方法')

#python中一切皆对象

'''
类的组成：
类属性
实力方法
静态方法
类方法

'''
#创建student类的对象
stu1=Student('张三',21)
stu1.eat()   #调用类中的定义的eat方法  对象名.方法名（）
print(stu1.name)
print(stu1.age)

print('-------------------')
Student.eat(stu1)  #35行和30行代码功能相同，都是调用Student中的eat方法
                  #类型.方法名（类的对象）=====》就是方法定义处的self
