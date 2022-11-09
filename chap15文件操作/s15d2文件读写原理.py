# 开发时间：20/9/2022 下午7:43
'''
1.Python操作文件
2.打开或者新建文件
3.读，写操作
4.关闭资源
'''

#打开文件中的1000.TXT

file=open('1000.txt','r')
print(file.readlines())
file.close()