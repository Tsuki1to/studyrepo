# 开发时间：18/9/2022 下午10:12
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return self.name
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2   #实现了两个对象的加法（因为在Student类中，编写了__add__()特殊用法
print(s)
print('____________')
s=stu1.__add__(stu2)
print(s)

print('-------------------------------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print('------------实现对类中实例对象的长度输出-------------')
print(len(stu1))
print(stu1)