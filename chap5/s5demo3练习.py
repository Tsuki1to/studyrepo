# 开发时间：23/8/2022 下午2:41
#计算1到100之间的偶数和
sum=0
a=1
while a<101:
    if a%2==0:  #if not bool(a%2):
       sum+=a
    a+=1
print('1到100之间的偶数和为',sum)

#计算1到100之间的奇数和
sum=0
a=1
while a<101:
    if a%2:   #a%2=0，所以布尔值为False。
       sum+=a
    a+=1
print('1到100之间的奇数和为',sum)

