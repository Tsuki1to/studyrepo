# 开发时间：18/9/2022 下午9:01
#多态就是具有多种形态
class Animal(object):
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃肉')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person():   #不用关心Person是否是Animal的子类，只要知道Person是否具有eat方法就可以使用
    def eat(self):
        print('人吃饭')

#在类之外定义一个函数
def fun(obj):
    obj.eat()

#开始调用函数
fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())