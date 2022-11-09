# 开发时间：19/9/2022 下午1:12
#变量的赋值操作
class Cpu():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=Cpu()    #创建Cpu类的实例对象
cpu2=cpu1
print(cpu1)
print(cpu2)

print('类的浅拷贝Python中拷贝一般都是浅拷贝，拷贝时对象包含的子对象内容不拷贝，因此，源于拷贝对选哪个会引用一个子对象')
disk=Disk()   #创建一个硬盘类的实例对象
computer=Computer(cpu1,disk)  #创建一个计算机类的对象，对象中包含CPU和硬盘类的实例对象


import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)


print('_________________________________________________________________________')
print('深拷贝deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)