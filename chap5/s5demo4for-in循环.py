# 开发时间：23/8/2022 下午4:26
for item in 'Python': #第一次取值为P，将P赋值给item，将item的值输出
    print(item)

#range()产生一个整数序列，——>也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不需要使用到自定义变量，可以将自定义变量写为”_“
for _ in range(5): #range()中表达为循环的次数
    print('人生苦短，我用Python')

print('------使用for_in循环计算1到100之间的偶数和-----')
sum=0
# for i in range(0,101,2):
#         sum+=i
# print(sum)

for i in range(1,101):
    if i%2==0:
        sum+=i
print('1到100之间的偶数和为',sum)