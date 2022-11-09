# 开发时间26/9/2022 上午11:32
#第一种方式：print
fp=open('C:\\Users\\Yiton\\OneDrive\\PYcharmProject\\read.txt','w')
print('明天成就更好的你',file=fp)
fp.close()


#第二种方式使用文件的读写方式
with open('C:\\Users\\Yiton\\OneDrive\\PYcharmProject\\read.txt','w') as file:
    file.write('奋斗成为更好的你')