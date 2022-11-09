# 开发时间：18/9/2022 下午9:52
print(dir(object))

class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass


#创建C类的对象
x=C('Jc',20)   #x是C类型的一个实例对象
print(x.__dict__)  #实例对象的属性字典
print(C.__dict__)  #类的属性和方法的字典
print('___________________')
print(x.__class__)  #<class '__main__.C'>会输出对象所属于的类型
print(C.__bases__)  #输出的是C得父类类型的元组（多继承A和B
print(C.__base__)  #输出第一个继承的类（类的基类
print(C.__mro__)  #类的层次结构
print(A.__subclasses__())  #查看类的子代列表