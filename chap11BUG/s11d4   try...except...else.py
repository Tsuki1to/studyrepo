# 开发时间：14/9/2022 下午9:48
try:
    a=int(input('请输入一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为：',result)
except BaseException as e:     #如果出错就执行except
    print('出错了', e)
else:
    print('结果为:', result)   #没有出错就执行else

finally:                  #不管出不出错最后都要执行finally（释放内存
    print('感谢您的使用')


