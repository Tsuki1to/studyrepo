# 开发时间：10/11/2022 上午11:31
conding ='gbk'
'''所有可以一行语句就可以表达的函数就可以使用lambda表达式'''

# def f(x):
#     return x *x
# print(f(5))
#
# f = lambda x:x*x
# print(f(5))
# '''lambda冒号前面的都是输入，冒号后面就是输出'''
# g = lambda x,y:x+y
# print(g(4,5))

# countries = []
# file = open('./countries_zh.csv','r',encoding= 'utf-8')
# for line in file:
#     line = line.strip()  #去掉两边的空格
#     arr = line.split(',')
#     name = arr[1]
#     capt = arr[2]
#     popu = int(arr[4])
#     countries.append((name,capt,popu))
#
# for country in countries:
#     countries.sort(key=lambda country: country[2])
#     print(country)

def quadratic(a,b,c):
    return  lambda x:a*x*x + b*x + c
print(quadratic(1,-1,2)(5))