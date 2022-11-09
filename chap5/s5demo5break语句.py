# 开发时间：25/8/2022 下午1:03
#break用于结束循环结构，通常与分支结构if一起使用（满足条件后退出

# for xx in xx:
#     .....
#     if xx
#         break

# while(条件):
#     .....
#     if ....:
#         break

'''
从键盘录入密码，最多输入3次，如果输入正确就结束循环
'''
# for i in range(3):
#     pwd=input('请输入密码:')
#     if pwd=='888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确，还有'+str(2-i)+'次机会')


#使用while循环语句实现以上目的
a=0
while a<3:
    '''条件执行体（循环体）'''
    pwd=input('请输入密码：')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码错误')
    '''改变变量'''
    a+=1




