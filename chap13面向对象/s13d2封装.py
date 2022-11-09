# 开发时间：16/9/2022 下午2:37
class Student:
    def __int__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以加了两个__
    def show(self):
        print(self.name,self.age)


stu=Student('张三',20)
stu.show()