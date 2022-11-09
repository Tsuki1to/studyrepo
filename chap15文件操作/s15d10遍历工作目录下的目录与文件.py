# 开发时间：21/9/2022 下午11:06
import os
path=os.getcwd()   #获取当前工作目录
lst_file=os.walk(path)    #遍历目录及子目录下的所有文件
for dirpath,dirname,filename in lst_file:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('---------------------------')
    for dir in dirname:
        print(os.path.join(dirpath,dir))    #查看当前目录下有多少个子目录
    print('----------------------------------------')
    for file in filename:
        print(os.path.join(dirpath,file))  #查看目录及子目录下的所有文件
    print('*------------------------------------------------*')