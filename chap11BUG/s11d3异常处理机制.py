# 开发时间：14/9/2022 下午9:20
#两个整数除法运算
# a=int(input('请输入一个整数'))
# b=int(input('请输入第二个整数'))
# result=a/b
# print('结果为：',result)
#

#try......(可能异常情况和

#except.....(异常的代码
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:     #exception的难度从小到大
    print('对不起，除数不能为零')
except ValueError:             #越靠下的异常越严重
    print('只能输入整数')
print('程序结束')

