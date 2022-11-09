# 开发时间：23/8/2022 上午11:22
'''
内置函数：print(),input(),range()，无需前面的代码，可以直接使用
range()函数是用于生成一个整数序列
创建range()函数的三种方法：
1.range(stop)===>创建一个【0，stop）之间的整数序列，步长为1
2.range(start,stop)===>创建一个【start,stop）之间的整数序列，步长为1
3.range(start,stop,step)===>创建一个【start,stop)之间的整数序列，步长为step

'''
r=range(10)   #默认从0开始，默认相差1
print(r)   #range(0,10)
print(list(r))   #list用于查看range对象中的整数序列(列表)

#第二种方式
r=range(1,10)  #从1开始，到10结束（不包含10）
print(list(r))

#第三种创建方式，三个参数
r=range(1,10,2)
print(list(r))

'''判断指定的整数是否在序列中 in，not in'''
print(10 in r)  #10在r序列中
print(9 in r)  #9在r序列中
print(10 not in r)  #10不在r序列中
print(9 not in r)  #9不在r序列中

#range()的优点：占用内存少，不管多长，只占用三个参数（start,stop,step)
