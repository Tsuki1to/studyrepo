# 开发时间：20/9/2022 下午9:47
#os模块与操作系统与系统相关的一个模块
import os
#
#直接调用可执行文件
# os.startfile('E:\QQ\Bin\QQScLauncher.exe')

#os目录操作
print(os.getcwd())  #获取当前文件目录
lst=os.listdir('../chap15文件操作')   #返回当前文件目录中所有的文件和目录
print(lst)

# os.mkdir('newdir2')   #创建目录
# os.makedirs('A/B/C')    #创建多级目录
#os.rmdir('newdir2')    #删除目录
#os.removedirs('A/B/C')   #删除多级目录
# os.chdir('G:\\OneDrive\\PYcharmProject\\chap15文件操作')   更改当前工作目录