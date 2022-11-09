# 开发时间：25/8/2022 下午1:50
'''
else循环的3种执行方法：
1.搭配if时，if或者else执行其中之一
2.搭配while时，循环体中没有遇到break，当循环完毕后执行else
3.搭配for In时，没有遇到break时，循环完毕后执行else
'''
#输入密码
# for i in range(3):
#     pwd=input('请输入密码：')
#     if pwd=='888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
# else:
#     print('对不起，三次密码均输入错误')
#
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('对不起，三次输入均错误')