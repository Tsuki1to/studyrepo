# 开发时间：21/9/2022 下午10:48
import os
path=os.getcwd()  #获取当前目录
lst=os.listdir(path)    #获取路径下的所有文件和目录
for filename in lst:     #递归遍历目录下所有文件
    if filename.endswith('.py'):   #如果文件名字以.py为结尾的话
        print(filename)