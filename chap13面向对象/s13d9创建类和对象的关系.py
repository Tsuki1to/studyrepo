# 开发时间：19/9/2022 上午11:47
class Person(object):
    #__new__用于创建对象
    def __new__(cls, *args, **kwargs):   #__new__用于创建对象
        print('__new__被调用了，cls的id值为{0}'.format(id(cls)))   #查看new方法中第一个参数cls的内存地址
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj

    #__init__用于初始化对象
    def __init__(self,name,age):    #__init__方法是为类对象中的实例对象赋值
        print('__init__方法被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age


print('Object这个类对象的id值为：{0}'.format(id(object)))
print('Person这个类对象的id值为：{0}'.format(id(Person)))
print('____________________________________________________')
#创建person中的实例对象

p1=Person('张三',20)   #创建实例对象，对类中的实例属性进行赋值（name='张三，age=20
print('p1这个Person类中的实例对象的id值为：{0}'.format(id(p1)))
