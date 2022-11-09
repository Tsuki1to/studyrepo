# 开发时间：20/9/2022 下午8:38
# file=open('1000.txt','r')
# print(file.read(1))   读至第几个字符read（size）
#print(file.readline())   #读第几行readline ()

#print(file.readlines())   #读取每一行，将每一行返回至列表


# file=open('c.txt','a')
# # file.write('gello')  #write(str)
# lst=['你好','hello','world']
# file.writelines(lst)    #writelines(lst)
# file.close()


file=open('c.txt','a')    #把文件的指针移动到一个新的地方，seek（），括号中为跳过的字符个数，一个中文为两个字符
file.write('hello')
file.flush()
file.write('world')
file.close()